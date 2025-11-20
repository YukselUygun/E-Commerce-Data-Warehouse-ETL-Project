import logging
from extract import extract
from transform import transform
from load import load
from quality_checks import run_checks

logging.basicConfig(
    filename="../logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def run_etl():
    logging.info("ETL PIPELINE STARTED")

    try:
        # 1) EXTRACT
        raw_df = extract()
        logging.info(f"Extract tamamlandı. Satır sayısı: {len(raw_df)}")

        # 2) TRANSFORM
        clean_df = transform(raw_df)
        logging.info(f"Transform tamamlandı. Satır sayısı: {len(clean_df)}")

        # 3) QUALITY CHECKS
        run_checks(clean_df)
        logging.info("Quality checks tamamlandı.")

        # 4) LOAD
        load(clean_df)
        logging.info("Load tamamlandı.")

    except Exception as e:
        logging.error(f"HATA: {str(e)}")
        print(f"❌ ETL sırasında hata oluştu: {e}")

    logging.info("ETL PIPELINE FINISHED")


if __name__ == "__main__":
    run_etl()
