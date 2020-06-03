import psycopg2
import os

db_psswd = os.getenv("DB_PSSWD")

conn = psycopg2.connect(
        database="timedb",
        user="den",
        password= db_psswd,
        host="127.0.0.1",
        port="5432",
        )

cur = conn.cursor()

cur.execute("SELECT version();")

rows = cur.fetchall()

for row in rows:
    print("  ", row[0], "\n")


