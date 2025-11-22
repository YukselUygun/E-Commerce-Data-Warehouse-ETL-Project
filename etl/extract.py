import os
import pandas as pd
import logging

def extract():
    logging.info("Starting EXTRACT stage...")

    # --- YOLU DİNAMİK BULMA ---
    # Şu anki dosyanın (extract.py) olduğu yer
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Proje ana dizini (/app)
    project_root = os.path.dirname(current_dir)
    # Hedef dosya: /app/data/raw/online_retail.csv
    csv_path = os.path.join(project_root, "data", "raw", "online_retail.csv")
    # --------------------------

    if not os.path.exists(csv_path):
        logging.error(f"Data file not found: {csv_path}")
        raise FileNotFoundError(f"CSV file missing at {csv_path}!")
    
    df = pd.read_csv(
        csv_path, 
        encoding='latin1',
        parse_dates=['InvoiceDate']
    )
    
    logging.info(f"Extracted {len(df)} rows from CSV")
    return df