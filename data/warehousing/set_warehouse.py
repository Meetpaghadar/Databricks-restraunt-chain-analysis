from sqlalchemy import create_engine, text
import urllib
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("server")
database = os.getenv("db")
username = os.getenv("db_username")
password = os.getenv("db_password")


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


with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
    conn.execute(text("""
        ALTER DATABASE db_sqlserver
        SET CHANGE_TRACKING = ON
        (CHANGE_RETENTION = 14 DAYS, AUTO_CLEANUP = ON)
    """))

print("Database Change Tracking Enabled")

with open("db_setup.sql", "r") as file:
    sql_script = file.read()


with engine.begin() as conn:

    for statement in sql_script.split(";"):

        statement = statement.strip()

        if statement:
            conn.execute(text(statement))

print("Warehouse setup completed successfully!")

with engine.connect() as conn:

    result = conn.execute(text("""
        SELECT TABLE_SCHEMA, TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
    """))

    print("\nTables in Azure SQL:\n")

    for row in result:
        print(row)