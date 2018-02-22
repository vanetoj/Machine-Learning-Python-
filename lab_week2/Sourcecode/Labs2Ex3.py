class Book:
    def __init__(self, book_name, isbn, author):
        self.name = book_name
        self.isbn = isbn
        self.author = author

    def display(self):
        print("  Book: ", self.name)
        print("  ISBN: ", self.isbn)
        print("  Author", self.author)


class Library:
    booklist = [
        Book("The Hobbit", "10", "J.R.R.R.R. Tolkien"),
        Book("Learn Python", "11", "Albert Snek"),
        Book("Learn Java", "12", "Bill Gates")]

    def __init__(self):
        self.__books = Library.booklist

    def checkIn(self, student, book):
        self.__books.append(book)
        student.hecked_out_books.remove(book)
        print(student.name, " checked in ", book.name)

    def checkOut(self, student, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                print(student.name, " checked out ", book.name)
                self.__books.remove(book)
                student.hecked_out_books.append(book)

    def display(self):
        print("Books in library: ")
        for book in self.__books:
            book.display()
            print()


class Person:
    def __init__(self, person_name):
        self.name = person_name

    def display(self):
        print("Name: ", self.name)


class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)
        self.student_id = student_id
        self.hecked_out_books = []

    def display(self):
        Person.display(self)
        print("Student ID: ", self.student_id)
        print("Has Books: ")
        for book in self.hecked_out_books:
            book.display()
            print()


class Librarian(Person):
    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        self.employee_id = employee_id

    def display(self):
        Person.display(self)
        print("Employee ID: ", self.employee_id)


class AssistantLibrarian(Student, Librarian):
    def __init__(self, name, student_id, employee_id):
        Student.__init__(self, name, student_id)
        Librarian.__init__(self, name, employee_id)

    def display(self):
        Student.display(self)
        Librarian.display(self)


person = Person("Just Someone")
person.display()
print()

student = Student("Vania", "S-14524")
student.display()
print()

librarian = Librarian("Mildred", "E-12342")
librarian.display()
print()

assistant = AssistantLibrarian("Jack", "S-111", "E-5123")
assistant.display()
print()

library = Library()
library.display()
print()

library.checkOut(student, "11")
library.checkOut(student, "12")
library.display()
student.display()

library.checkIn(student, student.hecked_out_books[0])
library.display()
student.display()





