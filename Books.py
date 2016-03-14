import pickle
books = []
LIST_ACTION = '1'
ADD_ACTION = '2'
EXIT = '3'
while True:
    print('Что хотим делать?\n Добавить книгу введите 1, Посмотреть список книг введите 2, Для завершения нажмите 3')
    enter = input()
    if enter == LIST_ACTION:
        print('Введите имя новой книги')
        newbook = input()
        print('Введите автора книги')
        author = input()
        print('Введите год издания')
        year = input()
        print('Введите информацию о книге')
        information = input()
        books.append({'author' : author, 'title' : newbook, 'year': year, 'info': information})
        with open('books.pickle', 'wb') as f:
            pickle.dump(books, f)
    elif enter == ADD_ACTION:
        with open('books.pickle', 'rb') as f:
            books = pickle.load(f)
        for number, book in enumerate(books):
            print(number, book['title'])
            number = int(input('Введите номер книги,для получения информации о ней: '))
        try:
            print('Автор и название книги: {author} {title}\n Год издания: {year}\n Информация о книге: {info}'.format(**books[number]))
        except IndexError:
            print('Такого номера книги не существует')
    elif enter == EXIT:
        print('До свидания')
        break
