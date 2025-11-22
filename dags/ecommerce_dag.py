from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

# 1. Genel Ayarlar
default_args = {
    'owner': 'yuksel',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# 2. Çevre Değişkenleri 

env_config = {
    "DB_HOST": "postgres",
    "DB_USER": "postgres",
    "DB_PASSWORD": "mysecretpassword",
    "DB_NAME": "ecommerce_dwh",
    "DB_PORT": "5432"
}

with DAG(
    dag_id='ecommerce_etl_pipeline',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    # GÖREV 1: Tabloları Sıfırla
    task_setup_db = BashOperator(
        task_id='setup_database',
        bash_command='python /opt/airflow/etl/setup_tables.py',
        env=env_config  
    )

    # GÖREV 2: ETL Kodunu Çalıştır
    task_run_etl = BashOperator(
        task_id='run_etl_process',
        bash_command='python /opt/airflow/etl/main.py',
        env=env_config  
    )

    task_setup_db >> task_run_etl