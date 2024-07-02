import pytest
import random
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name_book', ['K', 'Ян', 'Название книги которое состоит из 40 сим'])
    def test_add_new_book_boundary_value_positiv(self, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert name_book in collector.get_books_genre()

    @pytest.mark.parametrize('name_book', ['', 'Название книги которое состоит больше 40 символов'])
    def test_add_new_book_boundary_value_negative(self, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert name_book not in collector.get_books_genre()

    def test_set_book_genre_positive(self):
        collector = BooksCollector()
        name_book = 'Бойцовский клуб'
        genre = 'Детективы'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert collector.get_book_genre(name_book) == genre

    def test_set_book_genre_no_value_in_genre_negative(self):
        collector = BooksCollector()
        name_book = 'Бойцовский клуб'
        genre = 'Драма'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert collector.get_book_genre(name_book) == ''

    def test_get_books_genre_true_value_positive(self):
        collector = BooksCollector()
        genre_test_dict = {}
        genre_test_dict['Бойцовский клуб'] = 'Детективы'
        name_book = 'Бойцовский клуб'
        genre = 'Детективы'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert genre_test_dict == collector.get_books_genre()

    def test_get_books_genre_instance_value(self):
        collector = BooksCollector()
        name_book = 'Бойцовский клуб'
        genre = 'Детективы'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert isinstance(collector.get_books_genre(), dict)
        assert bool(collector.get_books_genre())

    @pytest.mark.parametrize('name_books,genre', [('Бойцовский клуб', 'Ужасы'),
                                                  ('Первый мститель', 'Детективы'),
                                                  ('В', 'Мультфильмы'),
                                                  ('Поворот не туда', 'Комедии')]
                            )
    def test_get_books_with_specific_genre_positive(self, name_books, genre):
        collector = BooksCollector()
        collector.add_new_book(name_books)
        collector.set_book_genre(name_books, genre)
        assert name_books in collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize('name_books,genre', [('В', 'Мультфильмы'),
                                                  ('Поворот не туда', 'Комедии')]
                             )
    def test_get_books_for_children_pisitive(self, name_books, genre):
        collector = BooksCollector()
        collector.add_new_book(name_books)
        collector.set_book_genre(name_books, genre)
        assert name_books in collector.get_books_for_children()



    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()
        name_book = 'Бойцовский клуб'
        collector.add_new_book(name_book)
        collector.add_book_in_favorites(name_book)
        assert name_book in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_poitive(self):
        collector = BooksCollector()
        name_book = 'Бойцовский клуб'
        collector.add_new_book(name_book)
        collector.add_book_in_favorites(name_book)
        collector.delete_book_from_favorites(name_book)
        assert name_book not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        name_book = 'Бойцовский клуб'
        collector.add_new_book(name_book)
        collector.add_book_in_favorites(name_book)
        assert isinstance(collector.get_list_of_favorites_books(), list)
        assert bool(collector.get_list_of_favorites_books())
