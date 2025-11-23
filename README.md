# 🚀 E-Commerce Data Warehouse & ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?logo=apache-airflow&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=power-bi&logoColor=black)

## 📖 Proje Özeti

Bu proje, ham ve karmaşık e-ticaret verilerini (CSV) alarak tamamen temizlenmiş, optimize edilmiş ve analitik işlemlere uygun bir Veri Ambarı (Data Warehouse) yapısına dönüştüren **uçtan uca bir ETL Pipeline** uygulamasıdır.

### Proje Kapsamı

- **Extract** – CSV dosyalarından veri çekme
- **Transform** – Temizleme, düzenleme, normalizasyon, tip dönüşümleri
- **Load** – PostgreSQL üzerinde Kimball'a uygun Star Schema'ya yükleme
- **Orchestrate** – Airflow üzerinde otomatik zamanlama ve task yönetimi
- **Visualize** – Power BI ile interaktif dashboard oluşturma

Tüm bu adımlar tamamen otomatik, tekrarlanabilir ve sürdürülebilir bir mimari ile uygulanmıştır.

---

## 🏗️ Mimari (Architecture)

### Modern Veri Stack

```
                    ┌─────────────────────────────────────────┐
                    │   📄 Ham Veriler (CSV Dosyaları)       │
                    └──────────────────┬──────────────────────┘
                                       │ Extract
                                       ▼
                    ┌─────────────────────────────────────────┐
                    │        🐍 Python ETL Scripts            │
                    │    (Transform, Validate, Enrich)        │
                    └──────────────────┬──────────────────────┘
                                       │ Load
                                       ▼
                    ┌─────────────────────────────────────────┐
                    │  🐘 PostgreSQL Veri Ambarı (Star Schema)│
                    └──────────────────┬──────────────────────┘
                                       │ Query
                                       ▼
                    ┌─────────────────────────────────────────┐
                    │       📊 Power BI Raporları & Dashboard│
                    └─────────────────────────────────────────┘

                    🐳 Docker Ortamında Çalışan Bileşenler:
                    ├─ PostgreSQL Database
                    ├─ Apache Airflow Scheduler
                    └─ ETL Processing Engine
```

---

## 🔧 Teknoloji Seçimleri

### 🐳 Docker & Docker Compose

**Neden?**

- Ortam bağımlılıklarını ortadan kaldırma
- Projenin her makinede aynı şekilde çalışması

**Sonuç:**

- PostgreSQL, Airflow ve ETL scriptleri tamamen izole container'larda çalışır

### 🌬️ Apache Airflow

**Neden?**

- ETL sürecinin manuel değil, otomatik ve hata toleranslı yönetilmesi
- Task bağımlılıklarını yönetme

**Sonuç:**

- Günlük çalışan DAG, hata durumunda log üretir ve otomatik retry yapar

### 🐘 PostgreSQL + Kimball Star Schema

**Neden?**

- Analitik (OLAP) işlemlerinin hızlı çalışması
- Raporların optimize edilmesi
- Standart veri ambarı mimarisi

**Sonuç:**

- Fact ve Dimension tabanlı profesyonel veri ambarı yapısı

### 🐍 Python (Pandas, SQLAlchemy, Psycopg2)

**Neden?**

- Veri temizliği ve transform işlemleri için maksimum esneklik
- Bulk insert performansı

**Sonuç:**

- Düşük kaliteli veriler temizlenir, sütun tipleri normalize edilir, hatalı satırlar ayıklanır

---

## 📚 Tech Stack

| Kategori             | Teknoloji                            |
| -------------------- | ------------------------------------ |
| Programlama Dili     | Python 3.9                           |
| Orkestrasyon         | Apache Airflow 2.7                   |
| Veritabanı           | PostgreSQL 13                        |
| Konteynerizasyon     | Docker & Docker Compose              |
| BI Araçları          | Power BI                             |
| Python Kütüphaneleri | Pandas, SQLAlchemy, Psycopg2, PyYAML |

---

## 🧩 Veri Ambarı Modeli (Data Warehouse)

Veritabanı tasarımı **Star Schema** prensibine göre modellenmiştir.

### Tablo Yapıları

| Tablo Tipi    | Tablo Adı      | Açıklama                                    |
| ------------- | -------------- | ------------------------------------------- |
| **Fact**      | `fact_order`   | Fiyat, adet, toplam tutar ve satış olayları |
| **Dimension** | `dim_customer` | Müşteri bilgileri, ülke, ID                 |
| **Dimension** | `dim_product`  | Ürün adı, stok kodu, açıklama               |
| **Dimension** | `dim_date`     | Zaman analizlerine uygun tarih boyutu       |

---

## 📁 Proje Klasör Yapısı

```
e-commerce-dwh-etl/
├── config/
│   ├── config.example.yaml
│   └── config.yaml
├── data/
│   └── raw/
│       └── online_retail.csv
├── dags/
│   └── ecommerce_dag.py
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── quality_checks.py
│   ├── setup_tables.py
│   ├── main.py
│   └── utils/
│       └── db.py
├── sql/
│   └── 01_create_tables.sql
├── logs/
├── reports/
│   ├── e-commerce-sales.pbix
│   └── e-commerce-sales.png
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Kurulum & Çalıştırma

### ✅ Ön Koşullar

- Docker Desktop kurulu ve çalışır durumda olmalı
- Git kurulu olmalı
- İnternet bağlantısı

### 1️⃣ Projeyi Klonlayın

```bash
git clone https://github.com/YukselUygun/E-Commerce-Data-Warehouse-ETL-Project.git
cd e-commerce-dwh-etl
```

### 2️⃣ Tüm Sistemi Ayağa Kaldırın

```bash
docker-compose up --build
```

Bu komut:

- PostgreSQL veritabanını oluşturur
- Airflow Scheduler & Webserver kurulumunu yapar
- ETL ortamını hazır hale getirir
- Tüm servisleri başlatır

### 3️⃣ Airflow Web Arayüzüne Erişim

Tarayıcınızı açıp şuraya gidin:

```
http://localhost:8080
```

**Giriş Bilgileri:**

- Kullanıcı Adı: `admin`
- Şifre: `admin`

### 4️⃣ ETL Pipeline'ı Çalıştırın

1. Airflow arayüzünde `ecommerce_etl_pipeline` DAG'ını bulun
2. DAG'ı açın
3. Sol tarafta **Unpause** (mavi anahtarı açın)
4. Sağ üstte **Trigger DAG** (▶ butonu) ile başlatın
5. Pipeline'ın ilerleyişini DAG Graph View'dan izleyin

---

## 🧪 Veri Kalitesi Kontrolleri (Data Quality Checks)

Pipeline'ın yürütülmesi sırasında otomatik kalite kontrolleri uygulanır:

✅ **Null Değer Kontrolü** – Kritik alanlarında eksik veri denetimi  
✅ **Tip Dönüşüm Kontrolü** – Veri tiplerinin doğru dönüştürüldüğü kontrol  
✅ **Negatif Değer Kontrolü** – Fiyat, miktar gibi alanlarda negatif değer tespiti  
✅ **Duplicate Satır Kontrolü** – Tekrarlayan kayıt denetimi  
✅ **Foreign Key Uyumluluğu** – Fact-Dimension ilişkilerinin tutarlılığı  
✅ **Hata Loglama** – Tüm anomalilerin detaylı log dosyalarına yazılması

---

## 📊 Dashboard

Projenin son çıktısı **Power BI**'da hazırlanan interaktif analiz raporudur.

`reports/` klasöründe yer alan:

- `e-commerce-sales.pbix` – Power BI çalışma dosyası
- `e-commerce-sales.png` – Dashboard örnek görüntüsü

---

## 📝 ETL İşlem Akışı

1. **Extract** – `online_retail.csv` dosyası okunur
2. **Validation** – Veri yapısı ve içeriği kontrol edilir
3. **Transform** – Temizleme, standardizasyon, enrichment işlemleri yapılır
4. **Normalization** – Boyutsal tablolara (Dimension) ayrıştırılır
5. **Load** – Star Schema yapısına PostgreSQL'e yüklenir
6. **Quality Check** – Son kontroller ve doğrulamalar yapılır
7. **Report** – Sonuçlar log dosyalarına yazılır

---

## 🔍 Logs & Monitoring

Tüm ETL işlemlerine ait detaylı loglar:

- `logs/etl.log` – Genel ETL işlem logları
- `logs/dag_processor_manager/dag_processor_manager.log` – Airflow DAG işlemci logları
- `logs/dag_id=ecommerce_etl_pipeline/` – DAG çalıştırması logları

---

## 🚨 Sorun Giderme (Troubleshooting)

### PostgreSQL bağlantı hatası

```bash
docker-compose down
docker-compose up --build
```

### Airflow DAG görünmüyor

- DAG dosyasının `dags/` klasöründe olduğundan emin olun
- Airflow Scheduler'ı yeniden başlatın: `docker-compose restart airflow-scheduler`

### ETL işlemi başarısız

- Log dosyalarını kontrol edin: `logs/etl.log`
- Veri formatını CSV şemasıyla karşılaştırın
- PostgreSQL bağlantı bilgilerini config.yaml'da doğrulayın

---

## 📧 İletişim & Bilgi

**Geliştirici:** Yüksel Uygun  
**LinkedIn:** [linkedin.com/in/yukseluygun](https://www.linkedin.com/in/yukseluygun/)

---

## 📄 Lisans

Bu proje açık kaynak olup, eğitim ve geliştirme amaçlarıyla kullanılabilir.

---

**⭐ Projeyi beğendiyseniz, GitHub'da yıldız veriniz!**
