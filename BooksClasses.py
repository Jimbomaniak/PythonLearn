import json
CREATE_LIB = ADD_BOOK = CONT = '1'
LOAD_LIB = SHOW_BOOKS = BACK = '2'
EXIT = SAVE_LIB = '3'
books = []


class Books(object):
    '''Класс создания книг'''
    def __init__(self, author=None, title=None, year=None, info=None):
        self.author = author
        self.title = title
        self.year = year
        self.info = info

    def __str__(self):
        return 'Автор книги: {0.author}\nНазвание книги: {0.title}\n\
Год издания: {0.year}\nОписание книги: {0.info}'.format(self)


class Library(Books):
    '''Класс библиотеки - работа с книгами'''
    def createLibrary(self, lib_name):
        lib = open('{0}.json'.format(lib_name), 'w+')
        lib.close()
        print('Библиотека создана')

    def loadLibrary(self):
        newbooks = []
        lib_name = input('Напишите название библиотеки для загрузки: ')
        try:
            with open('{0}.json'.format(lib_name), 'r+') as file:
                mylist = json.load(file)
                for book in mylist:
                    newbooks.append(Books(**book))
                    print('Библиотека {0} загружена'.format(lib_name))
                    return newbooks
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            print('Такой библиотеки не существует')
            raise NameError('Не загрузилась библиотека')

    def saveLibrary(self, lib_name):
        mylist = []
        for book in books:
            mylist.append(book.__dict__)
        with open('{0}.json'.format(lib_name), 'w+') as f:
            json.dump(mylist, f)

    def addBook(self):
        author = input('Автор книги: ')
        title = input('Название книги: ')
        while True:
            try:
                year = int(input('Год издания: '))
            except ValueError:
                print('Год должен быть числом(например 1892)')
            else:
                break
        info = input('Информация о книге: ')
        books.append(Books(author, title, year, info))
        return books

    def showListOfBooks(self, books):
        if not books:
            print('В библиотеке еще нету книг')
        else:
            for number, book in enumerate(books):
                print(number, '{0.author} - {0.title}'.format(book))
            while True:
                try:
                    choice = int(input('Вывести информацию о книге под номером: '))
                    print(books[choice])
                    break
                except ValueError:
                    print('Введите число')
                except IndexError:
                    print('Такого номера нету в списке')


class Menu(Library):
    '''Класс Меню Программы'''
    def mainMenu(self):
        while True:
            choice = input('ГЛАВНОЕ МЕНЮ\n 1. Создать библиотеку\n 2. Загрузить библиотеку\n 3. Выйти из программы\n ')
            if choice == CREATE_LIB:
                print('Создание библиотеки....')
                global lib_name
                lib_name = input('Напишите название новой библиотеки: ')
                self.createLibrary(lib_name)
                self.subMenu(books)
            elif choice == LOAD_LIB:
                print('Загрузка библиотеки...')
                try:
                    libr = self.loadLibrary()
                except NameError:
                    continue

                self.subMenu(libr)
            elif choice == EXIT:
                print('Завершение программы')
                break

    def subMenu(self, libr):
        while True:
            choice = input('МЕНЮ РАБОТЫ С БИБЛИОТЕКОЙ\n 1.Добавить книгу в библиотеку\n 2.Вывести список книг в библиотеке\n 3.Сохранить изменения в библиотеке\n')
            if choice == ADD_BOOK:
                print('Добавление новой книги')
                self.addBook()
            elif choice == SHOW_BOOKS:
                print('Вывод списка книг в библиотеке')
                self.showListOfBooks(libr)
            elif choice == SAVE_LIB:
                self.saveLibrary(lib_name)
                print('Библиотека сохранена')
                choice = input('1.Продолжить\n2.Выход в ГЛАВНОЕ МЕНЮ\n')
                if choice == CONT:
                    continue
                elif choice == BACK:
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
        2.2.1.Если файл существует => открытие файла => переход в подменю 1.2
        2.2.2 Если файла нету => Вывод сообщения - Такой библиотеки не существует и возврат к пункту 2.1
    2.3 Возврат к основому меню
3. Выход из программы '''
