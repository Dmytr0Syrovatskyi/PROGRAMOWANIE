# Importujemy klasę Student z zadania 1, jeśli pliki są w tym samym folderze
# Jeśli wolisz mieć niezależny plik, możesz skopiować tutaj definicję klasy Student
from zad_1 import Student

class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w {self.city}, ul. {self.street} ({self.open_hours})"

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}"

class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka: {self.author_name} {self.author_surname} ({self.publication_date}) ze zbiorów: [{self.library}]"

class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n  - ".join([str(b) for b in self.books])
        return (f"--- ZAMÓWIENIE z dnia {self.order_date} ---\n"
                f"Obsługujący: {self.employee}\n"
                f"Wypożyczający: {self.student}\n"
                f"Książki:\n  - {books_str}\n"
                f"-----------------------------------")

if __name__ == '__main__':
    # 2 Biblioteki
    lib1 = Library("Warszawa", "Marszałkowska 10", "00-001", "08:00-18:00", "111-222-333")
    lib2 = Library("Kraków", "Floriańska 5", "30-002", "09:00-17:00", "444-555-666")

    # 3 Pracowników
    emp1 = Employee("Piotr", "Zalewski", "2020-01-01", "1990-05-15", "Warszawa", "Polna", "00-123", "123-123-123")
    emp2 = Employee("Kasia", "Burak", "2021-03-01", "1992-07-20", "Warszawa", "Leśna", "00-321", "234-234-234")
    emp3 = Employee("Marek", "Kowalski", "2019-10-10", "1985-11-30", "Kraków", "Długa", "30-111", "345-345-345")

    # 3 Studentów
    stud1 = Student("Michał", [60, 80])
    stud2 = Student("Zosia", [70, 90])
    stud3 = Student("Bartek", [40, 45])

    # 5 Książek
    book1 = Book(lib1, "2001", "J.R.R.", "Tolkien", 450)
    book2 = Book(lib1, "1997", "J.K.", "Rowling", 320)
    book3 = Book(lib1, "1925", "F. Scott", "Fitzgerald", 200)
    book4 = Book(lib2, "1988", "Stephen", "Hawking", 256)
    book5 = Book(lib2, "1851", "Herman", "Melville", 600)

    # 2 Zamówienia
    order1 = Order(emp1, stud1, [book1, book2], "2023-10-01")
    order2 = Order(emp3, stud2, [book4, book5, book3], "2023-10-02")

    # Wyświetlanie zamówień
    print(order1)
    print(order2)