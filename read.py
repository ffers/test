import db

conn = db.conn
cur = conn.cursor()

cur.execute("SELECT admiss, name FROM time")

rows = cur.fetchall()
for row in rows:
    print("admiss =", row[0])
    print("name =", row[1], "\n")

print("Operation done successfully")


cur.execute("SELECT admiss, name FROM time")

rows = cur.fetchall()
for row in rows:
    print("admiss =", row[0])
    print("name =", row[1], "\n")

print("Operation done successfully")
conn.close()
