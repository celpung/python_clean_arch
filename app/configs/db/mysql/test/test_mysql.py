from sqlalchemy import inspect as sqlalchemy_inspect
from sqlalchemy.exc import SQLAlchemyError
from configs.db.mysql.mysql_config import engine
from sqlalchemy import text

def test_mysql_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ MySQL connection successful.")

            # Cek semua tabel di database
            inspector = sqlalchemy_inspect(engine)
            tables = inspector.get_table_names()
            print("📋 Tables in DB:", tables)
    except SQLAlchemyError as err:
        print("❌ Failed to connect to MySQL.")
        print(f"Error: {err}")
