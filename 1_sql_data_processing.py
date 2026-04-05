import pandas as pd
import sqlite3
import numpy as np

# 1. Tải dữ liệu từ file CSV
print("1. Đang tải dữ liệu từ CSV...")
app_df = pd.read_csv('application_record.csv')
credit_df = pd.read_csv('credit_record.csv')

# 2. Tạo Database SQLite trong RAM
conn = sqlite3.connect(':memory:')

# 3. Đưa dữ liệu vào DB
app_df.to_sql('application_record', conn, index=False)
credit_df.to_sql('credit_record', conn, index=False)

# 4. TRUY VẤN SQL NÂNG CẤP
print("2. Đang thực thi truy vấn SQL nâng cao (Bad Ratio)...")
sql_query = """
WITH Credit_Summary AS (
    SELECT 
        ID,
        COUNT(*) AS Total_Months,
        SUM(CASE WHEN STATUS IN ('2','3','4','5') THEN 1 ELSE 0 END) AS Bad_Months,
        MAX(CASE WHEN STATUS IN ('2','3','4','5') THEN 1 ELSE 0 END) AS Is_Bad_Client
    FROM credit_record
    GROUP BY ID
)

SELECT 
    a.*, 
    c.Is_Bad_Client,
    c.Total_Months,
    c.Bad_Months,
    ROUND(1.0 * c.Bad_Months / c.Total_Months, 2) AS Bad_Ratio
FROM application_record a
INNER JOIN Credit_Summary c 
ON a.ID = c.ID;
"""

# 5. Load dữ liệu sạch
df = pd.read_sql_query(sql_query, conn)

# =========================
# 6. FEATURE ENGINEERING
# =========================
print("3. Đang xử lý Feature Engineering...")

# AGE
df['AGE'] = (-df['DAYS_BIRTH'] / 365).astype(int)

# YEARS_EMPLOYED (xử lý outlier 365243)
df['DAYS_EMPLOYED'] = df['DAYS_EMPLOYED'].replace(365243, np.nan)
df['YEARS_EMPLOYED'] = (-df['DAYS_EMPLOYED'] / 365).fillna(0).astype(int)

# Fill missing OCCUPATION
df['OCCUPATION_TYPE'] = df['OCCUPATION_TYPE'].fillna('Unknown')

# Nhóm tuổi
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=[20,30,40,50,60,70])

# Nhóm thu nhập
df['INCOME_GROUP'] = pd.qcut(df['AMT_INCOME_TOTAL'], 5)

# =========================
# 7. EDA NHANH (PRINT INSIGHT)
# =========================
print("\n4. PHÂN TÍCH NHANH:")

print("\n👉 Bad Rate theo nghề:")
print(df.groupby('OCCUPATION_TYPE')['Is_Bad_Client'].mean().sort_values(ascending=False).head(5))

print("\n👉 Bad Rate theo độ tuổi:")
print(df.groupby('AGE_GROUP')['Is_Bad_Client'].mean())

print("\n👉 Bad Rate theo thu nhập:")
print(df.groupby('INCOME_GROUP')['Is_Bad_Client'].mean())

# =========================
# 8. LƯU FILE
# =========================
print("\n5. Đang lưu file dữ liệu sạch...")
df.to_csv('final_cleaned_data.csv', index=False)

print(f"✅ Hoàn tất! Dataset có {len(df)} khách hàng.")