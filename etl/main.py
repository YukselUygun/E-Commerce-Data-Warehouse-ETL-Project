import logging
import sys
import os
from extract import extract
from transform import transform
from load import load
from quality_checks import run_checks

current_dir = os.path.dirname(os.path.abspath(__file__))
# Bir üst klasör (Proje ana dizini: /app)
project_root = os.path.dirname(current_dir)
# Logs klasörü yolu (/app/logs)
log_dir = os.path.join(project_root, "logs")

os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, "etl.log")

# 2. LOGGER AYARLARI 
logger = logging.getLogger()
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()

# A) Dosyaya Yazma Ayarı
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(file_handler)

# B) Ekrana (Terminal/Docker Logs) Yazma Ayarı
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))
logger.addHandler(console_handler)

def run_etl():
    logging.info("🚀 ETL PIPELINE STARTED")

    try:
        # 1) EXTRACT
        raw_df = extract()
        
        # 2) TRANSFORM
        clean_df = transform(raw_df)
        
        # 3) QUALITY CHECKS
        run_checks(clean_df)
        
        # 4) LOAD
        load(clean_df)
        
    except Exception as e:
        logging.error(f"HATA: {str(e)}")
        print(f"❌ ETL sırasında hata oluştu: {e}")
        # Docker'ın hatayı anlaması için exit code 1 ile çık
        sys.exit(1)

    logging.info("🏁 ETL PIPELINE FINISHED")

if __name__ == "__main__":
    run_etl()