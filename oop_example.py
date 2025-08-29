# ===============================
# Assignment 1: Design Your Own Class
# ===============================

# Base Class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Inherited Class: EBook (demonstrates inheritance)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size
    
    def description(self):
        # Polymorphism: Overrides parent method
        return f"'{self.title}' by {self.author}, {self.pages} pages, File size: {self.file_size}MB"


# ===============================
# Activity 2: Polymorphism Challenge
# ===============================

class Vehicle:
    def move(self):
        pass  # Base method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


# ===============================
# Testing the classes
# ===============================

# Assignment 1
print("=== Assignment 1: Books ===")
book1 = Book("1984", "George Orwell", 328)
ebook1 = EBook("Python Basics", "Yordanos", 250, 5)

print(book1.description())
print(ebook1.description())

# Assignment 2
print("\n=== Assignment 2: Vehicles ===")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
