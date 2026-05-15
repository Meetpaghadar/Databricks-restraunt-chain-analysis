from sqlalchemy import create_engine
import urllib
import os
from dotenv import load_dotenv
import pandas as pd

# =========================================
# Load Environment Variables
# =========================================

load_dotenv()

server = os.getenv("server")
database = os.getenv("db")
username = os.getenv("db_username")
password = os.getenv("db_password")

# =========================================
# Azure SQL Connection
# =========================================

connection_string = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server},1433;"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=yes;"
    f"Connection Timeout=60;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={connection_string}"
)

print("Connected to Azure SQL")

# =========================================
# CSV File Paths
# =========================================

base_path = "../files"

customers_path = os.path.join(base_path, "customers.csv")
restaurants_path = os.path.join(base_path, "restaurants.csv")
menu_items_path = os.path.join(base_path, "menu_items.csv")
reviews_path = os.path.join(base_path, "reviews.csv")

# =========================================
# Read CSV Files
# =========================================

print("Reading CSV files...")

df_customers = pd.read_csv(customers_path)
df_restaurants = pd.read_csv(restaurants_path)
df_menu_items = pd.read_csv(menu_items_path)
df_reviews = pd.read_csv(reviews_path)

print("CSV files loaded successfully")

# =========================================
# Upload Customers
# =========================================

df_customers.to_sql(
    "customers",
    engine,
    schema="restaurant",
    if_exists="append",
    index=False
)

print(f"Customers uploaded: {len(df_customers)} rows")

# =========================================
# Upload Restaurants
# =========================================

df_restaurants.to_sql(
    "restaurants",
    engine,
    schema="restaurant",
    if_exists="append",
    index=False
)

print(f"Restaurants uploaded: {len(df_restaurants)} rows")

# =========================================
# Upload Menu Items
# =========================================

df_menu_items.to_sql(
    "menu_items",
    engine,
    schema="restaurant",
    if_exists="append",
    index=False
)

print(f"Menu items uploaded: {len(df_menu_items)} rows")

# =========================================
# Upload Reviews
# =========================================

df_reviews.to_sql(
    "reviews",
    engine,
    schema="restaurant",
    if_exists="append",
    index=False
)

print(f"Reviews uploaded: {len(df_reviews)} rows")

# =========================================
# Finished
# =========================================

print("\nAll CSV data loaded successfully into Azure SQL!")