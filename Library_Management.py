# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and show how you can print all books,
# add a book and get the number of books using
# different methods. Show that your program doesnt persist the books after the program is stopped!

class library:
    def __init__(self):
       self.no_ofbook=0
       self.books =[]

    def addbooks(self,book):
        self.books.append(book)
        self.no_ofbook = len(self.books)

    def showinfo(self):
        print(f"The no.of books in the library is {self.no_ofbook}.\nAnd the books in the library are :")
        for book in self.books:
            print(book)

library1 =library()
library1.addbooks("Ramcharitra Manas")
library1.addbooks("Garud puran")
library1.addbooks("Bhagwad Gita")
library1.addbooks("Ramayan")
library1.addbooks("Mahabharat")
library1.showinfo()

