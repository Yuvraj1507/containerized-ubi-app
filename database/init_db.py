import psycopg2
import os

DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "mydatabase")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")

def init_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST
        )
        cur = conn.cursor()

        with open("database/schema.sql", "r") as f:
            cur.execute(f.read())

        with open("database/seed_data.sql", "r") as f:
            cur.execute(f.read())

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Database initialized successfully!")

    except Exception as e:
        print(f"❌ Error initializing database: {e}")

if __name__ == "__main__":
    init_db()
