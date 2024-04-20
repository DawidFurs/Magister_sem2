class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\nOpen Hours: {self.open_hours}\nPhone: {self.phone}"


class Employee:
    def __init__(self,first_name, last_name, hire_date, birth_date, city, street, zip_code, phone) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nHire Date: {self.hire_date}\nBirth Date: {self.birth_date}\nAddress: {self.city}, {self.street}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublication Date: {self.publication_date}\nPages: {self.number_of_pages}\nLibrary: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f" - {book}" for book in self.books])
        return f"Order by {self.employee.first_name} {self.employee.last_name} for {self.student}\nOrder Date: {self.order_date}\nBooks:\n{book_list}"



library1 = Library("City1", "Street1", "12345", "8:00 AM - 6:00 PM", "123-456-789")
library2 = Library("City2", "Street2", "54321", "9:00 AM - 5:00 PM", "987-654-321")

employee1 = Employee("John", "Doe", "2023-01-15", "1990-05-20", "City1", "Street3", "41-706", "123456789")
employee2 = Employee("Jane", "Smith", "2023-02-20", "1988-10-10", "City2", "Street4", "41-708", "223456789")
employee3 = Employee("Alice", "Johnson", "2023-03-25", "1995-03-05", "City1", "Street5", "41-707", "323456789")

book1 = Book(library1, "2022-12-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2021-11-15", "Author2", "Surname2", 300)
book3 = Book(library2, "2023-02-28", "Author3", "Surname3", 250)
book4 = Book(library2, "2020-05-10", "Author4", "Surname4", 180)
book5 = Book(library1, "2024-03-20", "Author5", "Surname5", 150)

order1 = Order(employee1, "Student1", [book1, book2, book3], "2024-04-20")
order2 = Order(employee2, "Student2", [book4, book5], "2024-04-19")


print(order1)
print("\n")
print(order2)