class Book:
    author = ''
    title = ''
    def __init__(book, author, title):
        book.author = author
        book.title = title
    def printOut(book):
        print(book.title + " written by " + book.author)

b1 = Book("Steinbeck", "Of Mice and Men")
b1.printOut()

b2 = Book("Harper Lee", "To Kill a Mockingbird")
b2.printOut()