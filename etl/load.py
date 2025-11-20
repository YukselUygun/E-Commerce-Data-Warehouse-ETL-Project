import pandas as pd
from utils.db import get_engine
from sqlalchemy import text
import logging

def load(df):
    logging.info("📥 Load aşaması başladı (Optimize Edilmiş)...")
    engine = get_engine()

    # --- 0. HAZIRLIK: VERİ TİPLERİNİ GARANTİLE ---
    # Merge işlemlerinin hatasız olması için tipleri string yapıyoruz
    df["stock_code"] = df["stock_code"].astype(str).str.strip()
    df["customer_id"] = df["customer_id"].astype(str).str.split('.').str[0] # 12345.0 -> 12345
    df["description"] = df["description"].astype(str).str.strip()
    df["country"] = df["country"].astype(str).str.strip()
    
    # Tarih işlemleri
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    df["date_str"] = df["invoice_date"].dt.date  # Merge için string/date formatı

    # --- 1. DIMENSION TABLES YÜKLEME (Deduplication ile) ---
    
    # A) DIM PRODUCT
    logging.info("1/4: DimProduct hazırlanıyor...")
    # Stock code'a göre tekilleştiriyoruz. Aynı kod varsa ilkini al, diğerlerini at.
    dim_product = df[["stock_code", "description"]].drop_duplicates(subset=["stock_code"])
    
    # Veritabanını temizle (Setup çalıştırmayı unuttuysan diye güvenlik önlemi)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE fact_order, dim_product, dim_customer, dim_date RESTART IDENTITY CASCADE;"))
        conn.commit()

    # Dim Product Yükle
    dim_product.to_sql("dim_product", engine, if_exists="append", index=False, method="multi", chunksize=10000)
    logging.info(f"✅ DimProduct yüklendi: {len(dim_product)} adet.")

    # B) DIM CUSTOMER
    logging.info("⏳ DimCustomer hazırlanıyor...")
    dim_customer = df[["customer_id", "country"]].drop_duplicates(subset=["customer_id"])
    dim_customer.columns = ["customer_code", "country"] # DB kolon ismine uydurma
    dim_customer.to_sql("dim_customer", engine, if_exists="append", index=False, method="multi", chunksize=10000)
    logging.info(f"✅ DimCustomer yüklendi: {len(dim_customer)} adet.")

    # C) DIM DATE
    logging.info("⏳ DimDate hazırlanıyor...")
    # Date tablosu için gerekli kolonları seçip tekilleştir
    dim_date = df[["invoice_date", "year", "month", "day", "weekday"]].drop_duplicates(subset=["invoice_date"])
    # DB şemasındaki isimlerle eşleştirelim (date kolonu db'de 'date', df'de 'invoice_date' karışmasın)
    dim_date_ready = dim_date.copy()
    dim_date_ready["date"] = dim_date_ready["invoice_date"].dt.date
    dim_date_ready = dim_date_ready[["date", "year", "month", "day", "weekday"]] # Sütun sırası ve seçimi
    dim_date_ready = dim_date_ready.drop_duplicates(subset=["date"]) # Saat farkından oluşan çiftleri sil
    
    dim_date_ready.to_sql("dim_date", engine, if_exists="append", index=False, method="multi", chunksize=10000)
    logging.info(f"✅ DimDate yüklendi: {len(dim_date_ready)} adet.")

    # --- 2. ID'LERİ GERİ OKUMA (LOOKUP) ---
    logging.info("2/4: ID'ler veritabanından çekiliyor...")
    
    # Sadece ID ve Business Key'leri çekiyoruz
    db_products = pd.read_sql("SELECT product_id, stock_code FROM dim_product", engine)
    db_customers = pd.read_sql("SELECT customer_id, customer_code FROM dim_customer", engine)
    db_dates = pd.read_sql("SELECT date_id, date FROM dim_date", engine)

    # --- 3. MERGE (BİRLEŞTİRME) ---
    logging.info("3/4: Fact Tablosu oluşturuluyor (Mapping)...")

    # Product ID Ekle
    fact_df = df.merge(db_products, on="stock_code", how="left")
    
    # Customer ID Ekle
    fact_df = fact_df.merge(db_customers, left_on="customer_id", right_on="customer_code", how="left")
    
    # Date ID Ekle (Tarih formatına dikkat ederek)
    # db_dates['date'] object gelebilir, onu da date objesine çevirelim
    db_dates["date"] = pd.to_datetime(db_dates["date"]).dt.date
    fact_df["temp_date_join"] = fact_df["invoice_date"].dt.date
    
    fact_df = fact_df.merge(db_dates, left_on="temp_date_join", right_on="date", how="left")

    # --- 4. TEMİZLİK VE YÜKLEME ---
    logging.info("4/4: Fact tablosu veritabanına basılıyor...")

    final_fact = fact_df[[
        "invoice_no",
        "product_id",   # Merge'den gelen
        "customer_id_y", # Merge'den gelen (customer tablosundaki id)
        "date_id",      # Merge'den gelen
        "quantity",
        "unit_price",
        "total_price"
    ]].copy()

    final_fact.columns = ["invoice_no", "product_id", "customer_id", "date_id", "quantity", "unit_price", "total_price"]

    # Veri patlaması kontrolü (Hata ayıklama için)
    if len(final_fact) > len(df) + 100: # Ufak sapmalar olabilir ama milyonlar olamaz
        logging.error(f"❌ HATA: Satır sayısı patladı! Orjinal: {len(df)}, Oluşan: {len(final_fact)}")
        raise ValueError("Cartesian Product Hatası tespit edildi.")

    final_fact.to_sql("fact_order", engine, if_exists="append", index=False, method="multi", chunksize=5000)
    
    logging.info(f"🎉 FACT tablo başarıyla yüklendi! Toplam {len(final_fact)} satır.")