import yaml
import os
from sqlalchemy import create_engine

# Config dosyasının tam yolunu dinamik olarak buluyoruz
def load_config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    config_path = os.path.join(project_root, "config", "config.yaml")

    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def get_engine():
    config = load_config()
    db_conf = config["database"]
    
    # --- BURASI YENİ: Önce Environment Variable'a bak, yoksa config dosyasını al ---
    # Docker'da çalışırken os.getenv değerleri gelecek.
    user = os.getenv("DB_USER", db_conf["user"])
    password = os.getenv("DB_PASSWORD", db_conf["password"])
    host = os.getenv("DB_HOST", db_conf["host"])
    port = os.getenv("DB_PORT", db_conf["port"])
    db = os.getenv("DB_NAME", db_conf["dbname"])
    # ----------------------------------------------------------------------------

    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)