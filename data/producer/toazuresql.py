from sqlalchemy import create_engine
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
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")

from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.fetchone())