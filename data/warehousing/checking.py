import pyodbc
import pandas as pd

# Connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=restrauntops.database.windows.net;"
    "DATABASE=db_sqlserver;"
    "UID=sqladmin;"
    "PWD=saral@369;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
    "Connection Timeout=60;"
)

cursor = conn.cursor()

print("✅ Connected Successfully")

# =====================================================
# 1. SHOW ALL TABLES + SCHEMAS
# =====================================================

tables_query = """
SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_SCHEMA, TABLE_NAME
"""

tables = pd.read_sql(tables_query, conn)

print("\n📦 TABLES IN DATABASE:")
print(tables)

# =====================================================
# 2. SHOW ROW COUNTS
# =====================================================

print("\n📊 ROW COUNTS:")

for _, row in tables.iterrows():
    schema = row["TABLE_SCHEMA"]
    table = row["TABLE_NAME"]

    query = f"SELECT COUNT(*) AS count FROM [{schema}].[{table}]"

    try:
        count = pd.read_sql(query, conn).iloc[0, 0]
        print(f"{schema}.{table} --> {count} rows")
    except Exception as e:
        print(f"{schema}.{table} --> Error: {e}")

# =====================================================
# 3. SHOW COLUMNS FOR EACH TABLE
# =====================================================

columns_query = """
SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
ORDER BY TABLE_SCHEMA, TABLE_NAME
"""

columns = pd.read_sql(columns_query, conn)

print("\n🧱 COLUMNS:")
print(columns)

# =====================================================
# 4. SAMPLE DATA FROM EACH TABLE
# =====================================================

for _, row in tables.iterrows():

    schema = row["TABLE_SCHEMA"]
    table = row["TABLE_NAME"]

    print(f"\n🔎 SAMPLE DATA: {schema}.{table}")

    query = f"SELECT TOP 5 * FROM [{schema}].[{table}]"

    try:
        df = pd.read_sql(query, conn)
        print(df)
    except Exception as e:
        print(f"Error reading table: {e}")

# =====================================================

conn.close()

print("\n✅ Done")