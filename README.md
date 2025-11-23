# 🚀 E-Commerce Data Warehouse & ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?logo=apache-airflow&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=power-bi&logoColor=black)

📖 Overview

Bu proje, ham ve karmaşık e-ticaret verilerini (CSV) alarak tamamen temizlenmiş, optimize edilmiş ve analitik işlemlere uygun bir Veri Ambarı (Data Warehouse) yapısına dönüştüren uçtan uca bir ETL Pipeline uygulamasıdır.

Proje kapsamında:

- Extract – CSV dosyalarından veri çekme
- Transform – Temizleme, düzenleme, normalizasyon, tip dönüşümleri
- Load – PostgreSQL üzerinde Kimball'a uygun Star Schema’ya yükleme
- Orchestrate – Airflow üzerinde otomatik zamanlama ve task yönetimi
- Visualize – Power BI ile interaktif dashboard oluşturma
  tamamen otomatik, tekrarlanabilir ve sürdürülebilir bir mimari ile uygulanmıştır.

## 🧠 Architecture

### Modern Data Stack

Bu proje modern veri mühendisliği standartlarına göre tasarlanmıştır.

```mermaid
graph LR
    A[📄 Raw Data (CSV Files)] -->|Extract| B(🐍 Python ETL Scripts)
    B -->|Transform| B
    B -->|Load| C[(🐘 PostgreSQL Data Warehouse)]
    C -->|Query| D[📊 Power BI Reports]

    subgraph 🐳 Dockerized Environment
        B
        C
        E[🌬️ Apache Airflow Scheduler] -.->|Orchestrates| B
    end

```

❓ Teknoloji Seçimleri – Neden Bu Araçlar?
🐳 Docker & Docker Compose

Neden?
— Ortam bağımlılıklarını ortadan kaldırmak ve projenin her makinede aynı şekilde çalışmasını sağlamak.

Sonuç:
— PostgreSQL, Airflow ve ETL scriptleri tamamen izole container’larda çalışır.

🌬️ Apache Airflow

Neden?
— ETL sürecinin manuel değil, otomatik ve hata toleranslı yönetilmesi için.

Sonuç:
— Günlük çalışan DAG, task bağımlılıklarını yönetir, hata durumunda log üretir.

🐘 PostgreSQL + Kimball Star Schema

Neden?
— Analitik (OLAP) işlemlerinin hızlı çalışması, raporların optimize edilmesi için.

Sonuç:
— Fact ve Dimension tabanlı profesyonel veri ambarı yapısı.

🐍 Python (Pandas, SQLAlchemy, Psycopg2)

Neden?
— Veri temizliği, transform işlemleri ve Bulk Insert için en esnek araç.

Sonuç:
— Düşük performanslı veriler temizlenir, sütun tipleri normalize edilir, hatalı satırlar ayıklanır.

🛠️ Tech Stack
Kategori Teknoloji
Dil Python 3.9
Orkestrasyon Apache Airflow 2.7
Veritabanı PostgreSQL 13
Konteyner Docker
BI Power BI
Python Kütüphaneleri Pandas, SQLAlchemy, Psycopg2, PyYAML

Data Warehouse Modeli
Veritabanı tasarımı Star Schema prensibine göre modellenmiştir.
🧩 Tablo Yapıları
Tablo Tipi Tablo Adı Açıklama
Fact fact_order Fiyat, adet, toplam tutar ve satış olayları
Dimension dim_customer Müşteri bilgileri, ülke, ID
Dimension dim_product Ürün adı, stok kodu, açıklama
Dimension dim_date Zaman analizlerine uygun tarih boyutu

Dashboard

Projenin son çıktısı Power BI'da hazırlanan interaktif analiz raporudur.
reports/ klasöründe yer alan dashboard ekran görüntüsü örnek olarak eklenmiştir.

🚀 Kurulum & Çalıştırma

Bu projeyi çalıştırmak için Docker Desktop kurulu olmalıdır.

🔽 1. Projeyi Klonlayın
git clone https://github.com/YukselUygun/E-Commerce-Data-Warehouse-ETL-Project.git
cd E-Commerce-Data-Warehouse-ETL-Project

🐳 2. Tüm Sistemi Ayağa Kaldırın
docker-compose up --build

Bu komut:
PostgreSQL’i oluşturur
Airflow Scheduler & Webserver kurulumunu yapar
ETL ortamını hazır hale getirir

🌐 3. Airflow Arayüzüne Giriş

Tarayıcınızdan:
👉 http://localhost:8080
Kullanıcı adı: admin
Şifre: admin

▶️ 4. ETL Pipeline'ı Çalıştırın

1- Airflow’da ecommerce_etl_pipeline DAG’ını bulun
2- Sol taraftan Unpause (anahtarı açın)
3- Sağ üstten Trigger DAG (▶) ile başlatın

Proje Klasör Yapısı
.
├── config/
│ └── config.yaml
├── data/
│ └── raw/
│ └── online_retail.csv
├── etl/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── quality_checks.py
├── dags/
│ └── ecommerce_etl_pipeline.py
├── logs/
├── docker-compose.yml
└── reports/

🧪 Veri Kalitesi Kontrolleri (Data Quality Checks)

Pipeline sonunda otomatik kalite kontrolleri uygulanır:

- Null kontrolü
- Tip dönüşüm kontrolü
- Negatif değer kontrolü
- Duplicate satır kontrolü
- Fact–Dimension foreign key uyumluluğu
- Hatalar loglara yazılır.

👨‍💻 Geliştirici

Yüksel Uygun
🔗 LinkedIn: (https://www.linkedin.com/in/yukseluygun/)
