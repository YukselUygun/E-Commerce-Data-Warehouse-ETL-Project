def run_checks(df):
    print("🔎 Quality Check başlatılıyor...")

    # 1) Eksik müşteri kontrolü
    missing_cust = df["customer_id"].isna().sum()
    print(f"➡ Missing customer_id: {missing_cust}")

    # 2) Negatif quantity kontrolü
    negative_qty = (df["quantity"] < 0).sum()
    print(f"➡ Negative quantity rows: {negative_qty}")

    # 3) Boş description kontrolü
    missing_desc = df["description"].isna().sum()
    print(f"➡ Missing description: {missing_desc}")

    # 4) Duplicate invoice kontrolü
    dup_inv = df["invoice_no"].duplicated().sum()
    print(f"➡ Duplicate invoice_no: {dup_inv}")

    print("✔ Quality Check tamamlandı.")
