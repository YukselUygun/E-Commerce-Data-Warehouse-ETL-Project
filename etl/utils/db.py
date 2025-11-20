import yaml
import os
from sqlalchemy import create_engine

# Config dosyasının tam yolunu dinamik olarak buluyoruz
def load_config():
    # Bu dosyanın (db.py) bulunduğu klasörü bul
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Proje ana dizinine çık (etl/utils -> etl -> root)
    project_root = os.path.dirname(os.path.dirname(current_dir))
    # Config yolunu oluştur
    config_path = os.path.join(project_root, "config", "config.yaml")

    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def get_engine():
    config = load_config()
    db_conf = config["database"]
    
    user = db_conf["user"]
    password = db_conf["password"]
    host = db_conf["host"]
    port = db_conf["port"]
    db = db_conf["dbname"]

    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)