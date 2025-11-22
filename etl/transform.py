import pandas as pd

def transform(df):
    print("🔄 Transform aşaması başladı...")

    # COPY ekleme
    df = df.copy()

    # 1) Kolon isimlerini düzenleme
    df.columns = ["invoice_no", "stock_code", "description", "quantity",
                  "invoice_date", "unit_price", "customer_id", "country"]

    # 2) Boş değer temizliği
    df = df.dropna(subset=["customer_id", "description"])

    # --- YENİ EKLENECEK KISIM BAŞLANGIÇ ---
    # Customer ID'yi önce tamsayıya (int) çevirip .0'dan kurtarıyoruz, sonra string yapıyoruz.
    df["customer_id"] = df["customer_id"].astype(int).astype(str)
    
    # Stock code'u da garanti olsun diye string yapalım
    df["stock_code"] = df["stock_code"].astype(str)
    # --- YENİ EKLENECEK KISIM BİTİŞ ---

    # COPY ekledik: Filtreleme sonrası indexleri sıfırlayıp kopya alıyoruz
    df = df.reset_index(drop=True).copy()

    # 3) Tarih formatlama
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    df["year"] = df["invoice_date"].dt.year
    df["month"] = df["invoice_date"].dt.month
    df["day"] = df["invoice_date"].dt.day
    df["weekday"] = df["invoice_date"].dt.day_name()

    # 4) Total price hesaplama
    df["total_price"] = df["quantity"] * df["unit_price"]

    # 5) Son kolonları seçme
    df = df[[
        "invoice_no", "stock_code", "description", "quantity",
        "unit_price", "customer_id", "country", "invoice_date",
        "year", "month", "day", "weekday", "total_price"
    ]]

    print("✅ Transform tamamlandı.")
    return df