import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY, title text, author text, "
                         "year integer, reader_id INTEGER FOREIGN KEY)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS readers (reader_id  INTEGER PRIMARY KEY, first_name text, "
                         "last_name text, birth_year integer, book_id INTEGER FOREIGN KEY)")
        self.conn.commit()

    def add_book(self, title, author, year, reader_id):
        self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,NULL)", (title, author, year, reader_id))
        self.conn.commit()

    def del_book(self, book_id):
        self.cur.execute("DELETE FROM books WHERE book_id=?", (book_id, ))
        self.conn.commit()

    def give_book_to_reader(self, reader_id, book_id,):
        self.cur.execute("UPDATE books SET reader_id=? WHERE book_id=?", (reader_id, book_id))
        self.cur.execute("UPDATE readers SET book_id=? WHERE reader_id=?", (book_id, reader_id))
        self.conn.commit()

    def get_book_from_reader(self, reader_id, book_id):
        self.cur.execute("UPDATE books SET reader_id=NULL WHERE book_id=?", book_id)
        self.cur.execute("UPDATE readers SET book_id=NULL WHERE reader_id=?", reader_id)
        self.conn.commit()

    def view_all_books(self):
        self.cur.execute("SELECT * FROM books")
        all_rows = self.cur.fetchall()
        return all_rows

    def view_all_available_books(self):
        self.cur.execute("SELECT * FROM books WHERE reader_id IS NULL")
        all_rows = self.cur.fetchall()
        return all_rows

    def view_all_unavailable_books(self):
        self.cur.execute("SELECT * FROM books WHERE reader_id IS NOT NULL")
        all_rows = self.cur.fetchall()
        return all_rows

    def view_all_readers(self):
        self.cur.execute("SELECT * FROM readers")
        all_rows = self.cur.fetchall()
        return all_rows

    def view_readers_with_book(self):
        self.cur.execute("SELECT * FROM books WHERE book_id IS NOT NULL")
        all_rows = self.cur.fetchall()
        return all_rows

    def search(self, title="", author="", year=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year))
        all_rows = self.cur.fetchall()
        return all_rows

    def sort_books_by_name(self):
        self.cur.execute("SELECT * FROM books")
        all_rows = self.cur.fetchall()
        return all_rows

    def sort_books_by_author(self):
        self.cur.execute("SELECT * FROM books")
        all_rows = self.cur.fetchall()
        return all_rows

    def sort_books_by_year(self):
        self.cur.execute("SELECT * FROM books")
        all_rows = self.cur.fetchall()
        return all_rows

    def __del__(self):
        self.conn.close()
