import sqlite3

conn = sqlite3.connect("bookshop.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER, attachment TEXT )")
conn.commit()
conn.close()

def insert_book(title, year, author, isbn, file_path): 
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO books(title, year, author, isbn, attachment) VALUES(?,?,?,?,?)',(title, year, author, isbn, file_path))
    conn.commit()
    conn.close()

insert_book("The Best", 1989, "Crhis Rogers", 23452, "okay" )

def view():
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    rows = cur.fetchall()
    print(rows)
    conn.commit()
    conn.close()

def search_entry(title, year, isbn, author):
    
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM books WHERE title =?',(title) )
    rows = cur.fetchall()
    conn.commit()
    conn.close()

view()