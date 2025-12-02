import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # Проверка добавления двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # Проверка, что у новой книги пустой жанр
    def test_newly_added_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Новая книга')
        
        assert collector.get_book_genre('Новая книга') == ''
    # Проверка получения жанра книги по имени
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', 'Фантастика')
        
        assert collector.get_book_genre('Тестовая книга') == 'Фантастика'

    # Проверка получения словаря книг и жанров
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        
        books_genre = collector.get_books_genre()
        
        assert books_genre['Книга 1'] == 'Фантастика'

    # Проверка, что книга с длинным названием не добавляется
    def test_add_new_book_with_long_name_not_added(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)
        
        assert long_name not in collector.get_books_genre()

    # Проверка установки жанра книги
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', 'Фантастика')
        
        assert collector.get_book_genre('Тестовая книга') == 'Фантастика'

    # Проверка получения книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Фантастика')
        collector.set_book_genre('Книга 3', 'Комедии')
        
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        
        assert fantasy_books == ['Книга 1', 'Книга 2']
    # Книги без возрастного рейтинга присутствуют в списке книг для детей
    def test_books_without_age_rating_are_in_children_list(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        
        children_books = collector.get_books_for_children()
        
        assert 'Детская книга' in children_books

    # Проверка получения книг по несуществующему жанру
    def test_get_books_with_specific_genre_nonexistent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        
        result = collector.get_books_with_specific_genre('Неизвестный жанр')
        assert result == []

    # Книги с возрастным рейтингом отсутствуют в списке книг для детей
    def test_books_with_age_rating_not_in_children_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга ужасов')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        
        children_books = collector.get_books_for_children()
        
        assert 'Книга ужасов' not in children_books

    # Проверка добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для удаления')
        collector.add_book_in_favorites('Книга для удаления')
        
        collector.delete_book_from_favorites('Книга для удаления')
        
        assert 'Книга для удаления' not in collector.get_list_of_favorites_books()

    # Проверка получения списка избранных книг, когда он заполнен
    def test_get_list_of_favorites_books_with_items(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        
        result = collector.get_list_of_favorites_books()
        assert result == ['Книга 1', 'Книга 2']