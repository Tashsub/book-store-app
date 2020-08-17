import sqlite3

conn = sqlite3.connect("lite.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS booktracker (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER, attachment BLOB )")
conn.commit()
conn.close()