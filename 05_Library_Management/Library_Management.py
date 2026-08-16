class Library:
    def __init__(self):
        self.Books = []

    def add_book(self, addbook):
        self.Books.append(addbook)
        print(addbook, "Book is successfully added.")

    def show_books(self):
        if len(self.Books) == 0:
            print("No Books Available!")
        else:
            print("\nBooks Available:")
            for i in self.Books:
                print(i)

    def remove_book(self, removebook):
        self.Books.remove(removebook)
        print(removebook, "Book successfully removed.")


Obj = Library()
Obj.add_book("English")
Obj.add_book("Math")
Obj.add_book("Chemistry")
Obj.remove_book("English")
Obj.show_books()
