class Books():
    def __init__ (self, author=None, title=None, year=None, info=None):
        self.author = author
        self.title = title
        self.year = year
        self.info = info
    def showInfo(self):
        print('Автор книги: {0.author}\nНазвание книги: {0.title}\nГод издания: {0.year}\nОписание книги: {0.info}'.format(self))

import json
CREATE_LIB = '1'
LOAD_LIB = '2'
EXIT = '3'
ADD_BOOK = '11'
SHOW_BOOKS = '22'
SAVE_LIB = '33'
RETURN_TO_MAIN_MENU = '44'

class Library():
    def createLibrary(self, lib_name):
        lib = open('{0}.json'.format(lib_name), 'w')
        lib.close()
        print('Библиотека создана')

    def loadLibrary(self, lib_name):
        try:
            lib = open('{0}.json'.format(lib_name), 'r+')
            books = json.load(lib)
            print('Библиотека загружена')
            return books
        except  FileNotFoundError:
            print('Такой библиотеки еще не существует')
        except json.decoder.JSONDecodeError:
            print('Библиотека пустая')

    def saveLibrary(self):
        lib = open('{0}.json'.format(lib_name), 'w')
        json.dump(books, lib)
        lib.close()
        print('Библиотека сохранена')

    def addBook(self, book_id=0):
        if





class Menu(Library, Books):
    def mainMenu(self):
        while True:
            choice = input('ГЛАВНОЕ МЕНЮ\n 1. Создать библиотеку\n 2. Загрузить библиотеку\n 3. Выйти из программы\n ')
            if choice == CREATE_LIB:
                print('Создание библиотеки....')
                lib_name = input('Напишите название новой библиотеки: ')
                self.createLibrary(lib_name)
                self.subMenu()
            elif choice == LOAD_LIB:
                print('Загрузка библиотеки...')
                lib_name = input('Напишите название библиотеки для загрузки: ')
                self.loadLibrary(lib_name)
            elif choice == EXIT:
                print('Завершение программы')
                break

    def subMenu(self):
        while True:
            choice = input('Меню работы с библиотекой\n 11. Добавить книгу в библиотеку\n 22. Вывести список книг в библиотеке\n 33. Сохранить изменения в библиотеке\n 44. Возврат в ГЛАВНОЕ МЕНЮ\n')
            if choice == ADD_BOOK:
                print('Добавление новой книги')
            elif choice == SHOW_BOOKS:
                print('Вывод списка книг в библиотеке')
            elif choice == SAVE_LIB:
                print('Сохранение библиотеки')
            elif choice == RETURN_TO_MAIN_MENU:
                print('Возврат в ГЛАВНОЕ МЕНЮ')
                break




if __name__ == '__main__':
    menu = Menu()
    menu.mainMenu()


'''АЛГОРИТМ:
1. Создание Библиотеки
1.2 Добавление книги в библиотеку
1.2.1 Добавление информации о книге(название автор год ифнормация)
1.3 Вывод пронумерованного списка книги
1.3.1 Выбор из этого списка нужно книги по номеру
1.3.2 Показ информации о выбранной книге
1.3.3 Возврат в 1.2
1.4 Сохранение созданной библиотеки
2. Отрытите библиотеки
2.1 Ввод названия библиотеки
2.2 Поиск по названию файла:
    1.Если файл существует => открытие файла => переход в подменю 1.2
    2.Если файла нету => Вывод сообщения - Такой библиотеки не существует и возврат к пункту 2.1
2.3 Возврат к основому меню
3. Выход из программы '''
