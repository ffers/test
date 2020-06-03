import psycopg2
import db

conn = db.conn
cur = db.cur

cur.execute(
        '''
        CREATE TABLE time(
        ADMISS int primary key not null,
        name text not null
        );
        '''
        )
conn.commit()
conn.close()
