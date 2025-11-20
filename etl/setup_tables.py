import logging
from sqlalchemy import text
from utils.db import get_engine

# Log ayarları
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

def create_tables():
    logging.info("🗑️ Tablo temizliği ve oluşturma işlemi başlıyor...")
    
    engine = get_engine()
    
    # Tablo oluşturma SQL komutları
    sql_commands = """
    -- 1) Önceki tabloları tamamen sil (DROP)
    DROP TABLE IF EXISTS fact_order CASCADE;
    DROP TABLE IF EXISTS dim_product CASCADE;
    DROP TABLE IF EXISTS dim_customer CASCADE;
    DROP TABLE IF EXISTS dim_date CASCADE;

    -- 2) Dimension Tables (Yeniden Oluştur)
    CREATE TABLE dim_product (
        product_id SERIAL PRIMARY KEY,
        stock_code VARCHAR(50),
        description TEXT
    );

    CREATE TABLE dim_customer (
        customer_id SERIAL PRIMARY KEY,
        customer_code VARCHAR(50),
        country VARCHAR(100)
    );

    CREATE TABLE dim_date (
        date_id SERIAL PRIMARY KEY,
        date DATE,
        year INT,
        month INT,
        day INT,
        weekday VARCHAR(20)
    );

    -- 3) Fact Table (Yeniden Oluştur)
    CREATE TABLE fact_order (
        order_line_id SERIAL PRIMARY KEY,
        invoice_no VARCHAR(50),
        product_id INT REFERENCES dim_product(product_id),
        customer_id INT REFERENCES dim_customer(customer_id),
        date_id INT REFERENCES dim_date(date_id),
        quantity INT,
        unit_price NUMERIC,
        total_price NUMERIC
    );
    """
    
    try:
        with engine.connect() as conn:
            conn.execute(text(sql_commands))
            conn.commit()
        logging.info("✅ Veritabanı SIFIRLANDI ve tablolar yeniden kuruldu.")
    except Exception as e:
        logging.error(f"❌ Hata oluştu: {e}")

if __name__ == "__main__":
    create_tables()