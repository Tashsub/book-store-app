import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER, attachment TEXT )")
        self.conn.commit()

    def insert_book(self,title, year, author, isbn, file_path=""): 
        self.cur.execute('INSERT INTO books(title, year, author, isbn, attachment) VALUES(?,?,?,?,?)',(title, year, author, isbn, file_path))
        self.conn.commit()
        

    def view_all(self):
        self.cur.execute('SELECT * FROM books')
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def search_entry(self, title="", author="", isbn="", year=""):
        self.cur.execute('SELECT * FROM books WHERE title=? OR author=? OR isbn=? OR year=?',(title,author, isbn, year))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def delete_entry(self, unique_id):
        self.cur.execute('DELETE FROM books WHERE id=?',(unique_id,))
        rows = self.cur.fetchall()
        self.conn.commit()

    def update_entry(self, title,year,author,isbn,unique_id): 
        self.cur.execute('UPDATE books SET title =?, year=?, author =?, isbn=? WHERE id=?',(title,year,author,isbn,unique_id))
        rows = self.cur.fetchall()
        self.conn.commit()


    def drop_table(self):
        conn = sqlite3.connect("bookshop.db")
        cur = conn.cursor()
        cur.execute('DROP TABLE books')
        conn.commit()
        conn.close()

    def get_row_example(self, unique_id):
        conn = sqlite3.connect("bookshop.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM books WHERE id=?',(unique_id,))
        row = cur.fetchall()
        conn.commit()
        conn.close()
        return row

    def update_test(self):
        cur.execute('UPDATE books SET title =?, year=?, author =?, isbn=? WHERE id=?',(title,year,author,isbn,unique_id))
        rows = cur.fetchall()
        conn.commit()
        conn.close()

    def close_connection(self):
        self.conn.close()

    def __del__(self):
        self.conn.close()

    

