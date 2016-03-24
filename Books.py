import json

def save_data(bookslist):
    with open('data.json', 'w') as files:
        json.dump(bookslist, files)
    print('Библиотека сохранена')

def load_data():
    try:
        files = open('data.json', 'r+')
        books = json.load(files)
        files.close()
        print('Библиотека загружена')
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        files = open('data.json', 'w')
        files.close
        books = []
        print('Библиотека пустая')
    return books

ADD_ACTION = '1'
LIST_ACTION = '2'
EXIT = '3'
books = load_data()

while True:
    enter = input('Что хотим делать?\n 1 - Добавить книгу\n 2 - Посмотреть список книг\n 3 - Сохранить и Выйти\n')
    if enter == ADD_ACTION:
        title = input('Введите имя новой книги: ')
        author = input('Введите автора книги: ')
        year = input('Введите год издания: ')
        info = input('Введите информацию о книге')
        books.append({'author' : author, 'title' : title, 'year': year, 'info': info})
    elif enter == LIST_ACTION:
        for number, book in enumerate(books):
            print(number, book['title'])
        number = int(input('Введите номер книги,для получения информации о ней: '))
        try:
            print('Автор и название книги: {author} {title}\n Год издания: {year}\n Информация о книге: {info}'.format(**books[number]))
        except IndexError:
            print('Такого номера книги не существует')
    elif enter == EXIT:
        save_data(books)
        print('До свидания')
        break

