'''
Пример ООП на русском языке для системы управления библиотекой:

Шаг №1: Класс Book (Книга)
Этот класс представляет книгу с её основными атрибутами, такими как название, автор, год издания и статус доступности.

Шаг №2: Класс Author (Автор)
Этот класс представляет автора книги.

Шаг №3: Класс Member (Член библиотеки)
Класс Member представляет читателя, который может брать и возвращать книги.

Шаг №4: Класс Librarian (Библиотекарь)
Библиотекарь может управлять книгами в библиотеке: добавлять новые книги, проверять их доступность и помогать с возвратами.

Шаг №5: Класс Library (Библиотека)
Класс Library управляет всеми книгами и членами библиотеки.
'''

# Описание класса Book (Книга)

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self._available = True  # Инкапсуляция: статус доступности книги

    def borrow(self):
        if self._available:
            self._available = False
            print(f"Книга '{self.title}' была взята.")
        else:
            print(f"Книга '{self.title}' недоступна для выдачи.")

    def return_book(self):
        self._available = True
        print(f"Книга '{self.title}' была возвращена.")

    def get_info(self):
        status = "Доступна" if self._available else "Недоступна"
        return f"'{self.title}' от {self.author} ({self.year}) - {status}"


# Класс Author (Автор)

class Author:
    def __init__(self, name, surname, patronomic, birth_year):
        self.name = name
        self.surname = surname
        self.patronomic = patronomic
        self.birth_year = birth_year
        self.books = []  # Список книг автора

    def write_book(self, title, year, genre):
        new_book = Book(title, self.name, year, genre)
        self.books.append(new_book)
        return new_book

    def get_books(self):
        return [book.get_info() for book in self.books]


# Класс Member (Студент)

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book._available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"{self.name} не может взять '{book.title}', так как она недоступна.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} не взял книгу '{book.title}'.")

    def get_borrowed_books(self):
        return [book.get_info() for book in self.borrowed_books]


# Класс Librarian (Библиотекарь)

class Librarian:
    def __init__(self, name):
        self.name = name

    def check_availability(self, book):
        status = "доступна" if book._available else "недоступна"
        print(f"Книга '{book.title}' сейчас {status}.")

    def add_book(self, library, book):
        if book not in library.books:  # Проверка, есть ли книга уже в библиотеке
            library.add_book(book)
            print(f"Книга '{book.title}' добавлена в библиотеку.")
        else:
            print(f"Книга '{book.title}' уже есть в библиотеке.")

    def remove_book(self, library, book):
        if book in library.books:  # Проверка, есть ли книга в библиотеке перед удалением
            library.remove_book(book)
            print(f"Книга '{book.title}' удалена из библиотеки.")
        else:
            print(f"Книга '{book.title}' не найдена в библиотеке.")


# Класс Library (Библиотека)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"Книга '{book.title}' не найдена в библиотеке.")

    def list_books(self):
        if not self.books:
            print(f"В библиотеке '{self.name}' нет книг.")
        else:
            for book in self.books:
                print(book.get_info())z


# TODO: Заметки
## Преподаватель: Дуплей Максим Игоревич
## Дата: 06.10.2024