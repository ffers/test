import db

conn = db.conn

cur = conn.cursor()

cur.execute(
        "INSERT INTO time (ADMISS, NAME) VALUES (3421, 'Dohn')"
        )

conn.commit()
print("Record insserted succesfully!")

conn.close()
