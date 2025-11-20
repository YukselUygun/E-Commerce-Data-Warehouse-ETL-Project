import os 
import pandas as pd 
import logging

def extract(csv_path="../data/raw/online_retail.csv"):
    logging.info("Starting EXTRACT stage...")

    if not os.path.exists(csv_path):
        logging.error(f"Data file not found: {csv_path}")
        raise FileNotFoundError("CSV file missing!.")
    
    df = pd.read_csv(
        csv_path, 
        encoding='latin1',
        parse_dates=['InvoiceDate']
        )
    
    logging.info(f"Extracted {len(df)} rows from CSV")
    return df