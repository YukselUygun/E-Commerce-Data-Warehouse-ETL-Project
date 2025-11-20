-- DATABASE SCHEMA SETUP

-- 1) Dimension Tables

CREATE TABLE IF NOT EXISTS dim_product (
    product_id SERIAL PRIMARY KEY,
    stock_code VARCHAR(50),
    description TEXT
);

CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id SERIAL PRIMARY KEY,
    customer_code INT,
    country VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id SERIAL PRIMARY KEY,
    date DATE,
    year INT,
    month INT,
    day INT,
    weekday VARCHAR(20)
);

-- 2) Fact Table

CREATE TABLE IF NOT EXISTS fact_order (
    order_line_id SERIAL PRIMARY KEY,
    invoice_no VARCHAR(50),
    product_id INT REFERENCES dim_product(product_id),
    customer_id INT REFERENCES dim_customer(customer_id),
    date_id INT REFERENCES dim_date(date_id),
    quantity INT,
    unit_price NUMERIC,
    total_price NUMERIC
);
