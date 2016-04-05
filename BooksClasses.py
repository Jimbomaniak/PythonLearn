import json
CREATE_LIB = ADD_BOOK = CONT = '1'
LOAD_LIB = SHOW_BOOKS = BACK = '2'
EXIT = SAVE_LIB = '3'
books = []


class Books(object):
    def __init__(self, author=None, title=None, year=None, info=None):
        self.author = author
        self.title = title
        self.year = year
        self.info = info

    def __str__(self):
        return 'Author: {0.author}\nName: {0.title}\n\
Year: {0.year}\nInformation: {0.info}'.format(self)


class Library(Books):
    def create_library(self, lib_name):
        lib = open('{0}.json'.format(lib_name), 'w+')
        lib.close()
        print('Library created')

    def load_library(self):
        newbooks = [] # список в котором будут  объекты класса , извлеченные из файла словарями и переданные классу Books
        try:
            with open('{0}.json'.format(lib_name), 'r+') as file:
                mylist = json.load(file)
                for book in mylist:
                    newbooks.append(Books(**book))
                    print('Labrary {0} loaded'.format(lib_name))
                    return newbooks
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            print('Such library not exist')
            raise NameError('Library not loaded') # Генерирует ошибку для возвращения в основное меню

    def save_library(self, lib_name):
        mylist = []
        for book in books:
            mylist.append(book.__dict__)
        with open('{0}.json'.format(lib_name), 'w+') as f:
            json.dump(mylist, f)

    def add_book(self):
        author = input('Book Author: ')
        title = input('Book Name: ')
        while True:
            try:
                year = int(input('Book Year: '))
            except ValueError:
                print('Year must be number(example: 1892)')
            else:
                break
        info = input('Book Information: ')
        books.append(Books(author, title, year, info))
        return books

    def show_list_of_books(self, books):
        if not books:
            print('Library do not have books yet')
        else:
            for number, book in enumerate(books):
                print(number, '{0.author} - {0.title}'.format(book))
            while True:
                try:
                    choice = int(input('Show information about book with number: '))
                    print(books[choice])
                    break
                except ValueError:
                    print('Enter number')
                except IndexError:
                    print('Such number dont exist')


class Menu(Library):
    def main_menu(self):
        while True:
            choice = input('MAIN MENU\n 1. Create Library\n 2. Load Library\n 3. Exit\n ')
            if choice == CREATE_LIB:
                print('Creation of library....')
                global lib_name
                lib_name = input('Write name for new library: ')
                self.create_library(lib_name)
                self.submenu(books)
            elif choice == LOAD_LIB:
                print('Library loading...')
                lib_name = input('Write name of library to load: ')
                try:
                    libr = self.load_library() # - загруженная библиотека в виде [class.object1, class.object2]
                except NameError:
                    continue
                self.submenu(libr)
            elif choice == EXIT:
                print('Exit.')
                break

    def submenu(self, libr):
        while True:
            choice = input('LIBRARY MENU\n 1.Add book \n 2.Show list of books\n 3.Save changes\n')
            if choice == ADD_BOOK:
                print('Adding new book...')
                self.add_book()
            elif choice == SHOW_BOOKS:
                print('Showing list of books...')
                self.show_list_of_books(libr)
            elif choice == SAVE_LIB:
                self.save_library(lib_name)
                print('Library saved.')
                choice = input('1.Continue\n2.Return to MAIN MENU\n')
                if choice == CONT:
                    continue
                elif choice == BACK:
                    break

if __name__ == '__main__':
    menu = Menu()
    menu.main_menu()


