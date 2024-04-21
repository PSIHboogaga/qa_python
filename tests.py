import pytest

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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # nen bpvtytybza
    def test_set_book_genre_set_genre(self):
        collector1 = BooksCollector()
        collector1.add_new_book('Гордость и предубеждение и зомби')
        collector1.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        assert collector1.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    @pytest.mark.parametrize('book_name, book_genre', [['Гордость и предубеждение и зомби', 'Ужасы'], ['Что делать, если ваш кот хочет вас убить', 'Ужасы']])
    def test_get_book_genre_get_genre(self, book_name, book_genre):
        BooksCollector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Ужасы'


    def test_get_books_with_specific_genre_get_books(self):

        collector3 = BooksCollector()
        collector3.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector3.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector3.get_books_with_specific_genre('Ужасы')
        assert 'Что делать, если ваш кот хочет вас убить' in collector3.books_with_specific_genre


    def test_get_books_genre_get_books(self):
        collector3 = BooksCollector()
        collector3.add_new_book('Гордость и предубеждение и зомби')
        collector3.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector3.get_books_genre()
        assert 'Гордость и предубеждение и зомби' and 'Что делать, если ваш кот хочет вас убить' in collector3.books_genre


    def test_get_books_for_children_show_books_for_children(self):
        collector4 = BooksCollector()
        collector4.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector4.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector4.add_new_book('Что делать, если хочешь какать')
        collector4.set_book_genre('Что делать, если хочешь какать', 'Мультфильмы')
        collector4.get_books_for_children()
        assert 'Что делать, если хочешь какать' in collector4.books_for_children

    def test_add_book_in_favorites_book_in_favorites(self):
        collector5 = BooksCollector()
        collector5.add_new_book('Гордость и предубеждение и зомби')
        collector5.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector5.add_new_book('Что делать, если хочешь какать')
        collector5.add_book_in_favorites('Что делать, если хочешь какать')
        assert 'Что делать, если хочешь какать' in collector5.favorites


    def test_delete_book_from_favorites_delete_book_from_favorites(self):
        collector6 = BooksCollector()
        collector6.add_new_book('Гордость и предубеждение и зомби')
        collector6.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector6.add_new_book('Что делать, если хочешь какать')
        collector6.add_book_in_favorites('Что делать, если хочешь какать')
        collector6.delete_book_from_favorites('Что делать, если хочешь какать')
        assert 'Что делать, если хочешь какать' not in collector6.favorites

    def test_get_list_of_favorites_books_get_list(self):
        collector7 = BooksCollector()
        collector7.add_new_book('Гордость и предубеждение и зомби')
        collector7.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector7.add_new_book('Что делать, если хочешь какать')
        collector7.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector7.add_book_in_favorites('Что делать, если хочешь какать')
        collector7.get_list_of_favorites_books()
        assert 'Что делать, если хочешь какать' and 'Что делать, если ваш кот хочет вас убить' in collector7.favorites

    def test_add_new_book_len_name_longer_then_forty(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Что делать, если ваш кот хочет вас убить, расчленить и съесть')
        assert 'Что делать, если ваш кот хочет вас убить, расчленить и съесть' not in collector8.books_genre


    def test_delete_fake_book_from_favorites_delete_book_from_favorites(self):
        collector6 = BooksCollector()
        collector6.add_new_book('Гордость и предубеждение и зомби')
        collector6.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector6.add_new_book('Что делать, если хочешь какать')
        collector6.add_book_in_favorites('Что делать, если хочешь какать')
        collector6.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если хочешь какать' in collector6.favorites



