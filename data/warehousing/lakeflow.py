"""
Execute Databricks Lakeflow utility_scripts.sql on SQL Server via pyodbc.

Reads utility_scripts.sql from this directory unchanged and runs it as-is.
Credentials load from the project-root .env (server, db, db_username, db_password).
"""

from __future__ import annotations

import logging
import os
import re
import sys
import time
from pathlib import Path

import pyodbc
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]
SQL_FILE = SCRIPT_DIR / "utility_scripts.sql"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("lakeflow")


def load_environment() -> None:
    env_path = PROJECT_ROOT / ".env"
    load_dotenv(env_path if env_path.is_file() else None)


def get_connection_string() -> str:
    server = os.environ["server"]
    database = os.environ["db"]
    username = os.environ["db_username"]
    password = os.environ["db_password"]

    driver = os.getenv("SQL_ODBC_DRIVER", "ODBC Driver 17 for SQL Server")
    port = os.getenv("SQL_PORT", "1433")
    if "," not in server and ":" not in server:
        server = f"{server},{port}"

    return (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        f"Encrypt={os.getenv('SQL_ENCRYPT', 'yes')};"
        f"TrustServerCertificate={os.getenv('SQL_TRUST_SERVER_CERTIFICATE', 'yes')};"
        f"Connection Timeout={os.getenv('SQL_CONNECTION_TIMEOUT', '120')};"
    )


def read_sql_script() -> str:
    if not SQL_FILE.is_file():
        raise FileNotFoundError(f"SQL script not found: {SQL_FILE}")
    return SQL_FILE.read_text(encoding="utf-8-sig")


def split_batches(script: str) -> list[str]:
    """Split only on GO line separators; otherwise run the full script."""
    parts = re.split(r"^\s*GO\s*;?\s*$", script, flags=re.IGNORECASE | re.MULTILINE)
    batches = [part.strip() for part in parts if part.strip()]
    return batches if batches else [script.strip()]


def drain_cursor(cursor: pyodbc.Cursor) -> None:
    while True:
        if cursor.messages:
            for message in cursor.messages:
                logger.info("SQL Server: %s", message[1] if len(message) > 1 else message)
        if cursor.description:
            try:
                cursor.fetchall()
            except pyodbc.ProgrammingError:
                pass
        if not cursor.nextset():
            break


def execute_sql_script(connection: pyodbc.Connection, script: str) -> None:
    batches = split_batches(script)
    logger.info("Executing %d batch(es)...", len(batches))

    connection.autocommit = False
    cursor = connection.cursor()
    started = time.perf_counter()

    try:
        for index, batch in enumerate(batches, start=1):
            logger.info("Batch %d/%d", index, len(batches))
            cursor.execute(batch)
            drain_cursor(cursor)
        connection.commit()
        logger.info("Committed successfully in %.1fs.", time.perf_counter() - started)
    except Exception:
        connection.rollback()
        logger.exception("Rolled back after error.")
        raise
    finally:
        cursor.close()


def main() -> int:
    load_environment()
    script = read_sql_script()
    logger.info("Loaded %s (%d bytes)", SQL_FILE.name, len(script.encode("utf-8")))

    conn_str = get_connection_string()
    logger.info("Connecting to %s / %s", os.environ["server"], os.environ["db"])

    connection = pyodbc.connect(conn_str, autocommit=False)
    try:
        execute_sql_script(connection, script)
    finally:
        connection.close()
        logger.info("Connection closed.")

    print("Lakeflow utility_scripts.sql ran successfully.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        raise SystemExit(1) from None
