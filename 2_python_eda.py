import pandas as pd
import numpy as np

# 1. LOAD DATA
print("1. Load dữ liệu...")
df = pd.read_csv('final_cleaned_data.csv')

# =========================
# 2. FEATURE ENGINEERING
# =========================
print("2. Feature Engineering...")

# AGE
df['AGE'] = (-df['DAYS_BIRTH'] / 365).astype(int)

# YEARS_EMPLOYED
df['DAYS_EMPLOYED'] = df['DAYS_EMPLOYED'].replace(365243, np.nan)
df['YEARS_EMPLOYED'] = (-df['DAYS_EMPLOYED'] / 365).fillna(0).astype(int)

# Fill missing OCCUPATION
df['OCCUPATION_TYPE'] = df['OCCUPATION_TYPE'].fillna('Unknown')

# AGE GROUP
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=[20,30,40,50,60,70])

# INCOME GROUP
df['INCOME_GROUP'] = pd.qcut(df['AMT_INCOME_TOTAL'], 5)

# =========================
# 3. KPI TỔNG QUAN
# =========================
print("\n3. KPI:")

total_clients = len(df)
bad_rate = df['Is_Bad_Client'].mean()
avg_income = df['AMT_INCOME_TOTAL'].mean()

print(f"Total Clients: {total_clients}")
print(f"Bad Rate: {round(bad_rate*100,2)}%")
print(f"Avg Income: {round(avg_income,0)}")

# =========================
# 4. EDA - TÌM INSIGHT
# =========================

print("\n4. Phân tích:")

# 4.1 Nghề nghiệp
occupation_risk = df.groupby('OCCUPATION_TYPE')['Is_Bad_Client'].mean().sort_values(ascending=False)
print("\n👉 Top nghề rủi ro cao:")
print(occupation_risk.head(10))

# 4.2 Độ tuổi
age_risk = df.groupby('AGE_GROUP')['Is_Bad_Client'].mean()
print("\n👉 Rủi ro theo độ tuổi:")
print(age_risk)

# 4.3 Thu nhập
income_risk = df.groupby('INCOME_GROUP')['Is_Bad_Client'].mean()
print("\n👉 Rủi ro theo thu nhập:")
print(income_risk)

# =========================
# 5. LƯU FILE CHO POWER BI
# =========================
print("\n5. Lưu file cho Power BI...")
df.to_csv('final_dataset_for_powerbi.csv', index=False)

print("✅ Hoàn tất!")