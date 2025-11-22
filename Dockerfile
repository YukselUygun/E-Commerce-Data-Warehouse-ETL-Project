FROM apache/airflow:2.7.1

USER root

# 3. Gerekli sistem araçları
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# 5. Kütüphaneleri yükle 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt