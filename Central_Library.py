# Central Library
# Author is Rahul
# date 17-03-2022

class Library:
    def __init__(self, listOfbooks):
        self.books = listOfbooks

    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print("*" + book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(
                f"Thanks for borrowing the {bookname}. Keep it safe and return it in 30 days")
            self.books.remove(bookname)
            return True
        else:
            print(
                f"{bookname} is not present or it is either already isuued to someone. Please wait until he return the book")
            return False

    def returnbook(self, bookname):
        self.books.append(bookname)
        print(
            "Thanks for returning the book! Hope you enjoyed reading it. Have a great day!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow.\n")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return.\n")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "C++", "C#", "Python"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomeMsg = '''===== Welcome to Central Library ====
        1. List of books
        2. Request a book
        3. Return a book
        4. Exit Library
        '''
        print(welcomeMsg)

        a = int(input("Enter a choice\n"))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnbook(student.returnBook())
        elif a == 4:
            print("Thanks for using the central library! Have a great day ahead.")
            exit()
        else:
            print("Invalid choice")
