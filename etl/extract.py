import os
import pandas as pd
import logging

def extract():
    logging.info("Starting EXTRACT stage...")

    #  YOLU DİNAMİK BULMA 

    current_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.dirname(current_dir)
    csv_path = os.path.join(project_root, "data", "raw", "online_retail.csv")


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