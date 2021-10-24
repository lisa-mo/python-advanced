from database import Database

class Library(Database):

    def __init__(self, list_books, list_readers):
        self.list_books = list_books
        self.list_readers = list_readers

    def add_book(self):
        pass

    def del_book(self):
        pass

    def give_book_to_reader(self):
        pass

    def get_book_from_reader(self):
        pass

    def view_all_books(self):
        pass

    def view_all_available_books(self):
        pass

    def view_all_unavailable_books(self):
        pass

    def sort_books_by_name(self):
        pass

    def sort_books_by_author(self):
        pass

    def sort_books_by_year(self):
        pass
