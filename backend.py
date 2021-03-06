import sqlite3
import app

conn = sqlite3.connect("bookshop.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER, attachment TEXT )")
conn.commit()
conn.close()

def insert_book(title, year, author, isbn, file_path=""): 
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO books(title, year, author, isbn, attachment) VALUES(?,?,?,?,?)',(title, year, author, isbn, file_path))
    conn.commit()
    conn.close()

#insert_book("The Best", 1989, "Crhis Rogers", 23452, "okay" )
#insert_book("op", 1989, "Crhis Rogers", 23452, "okay" )

def view_all():
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search_entry(title="", author="", isbn="", year=""):
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM books WHERE title=? OR author=? OR isbn=? OR year=?',(title,author, isbn, year))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete_entry(unique_id):
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM books WHERE id=?',(unique_id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()

def update_entry(title,year,author,isbn,unique_id): 
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('UPDATE books SET title =?, year=?, author =?, isbn=? WHERE id=?',(title,year,author,isbn,unique_id))
    rows = cur.fetchall()
    conn.commit()
    conn.close()


def drop_table():
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('DROP TABLE books')
    conn.commit()
    conn.close()

def get_row_example(unique_id):
    conn = sqlite3.connect("bookshop.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM books WHERE id=?',(unique_id,))
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

def update_test():
    conn = sqlite3.connect("bookshop.db")
    unique_id = 3
    title ="Sapient"
    year = 2000
    author = "Kim"
    isbn = 23423423423
    cur = conn.cursor()
    cur.execute('UPDATE books SET title =?, year=?, author =?, isbn=? WHERE id=?',(title,year,author,isbn,unique_id))
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    



#drop_table() 
#update_test()
