books = []
while True:
    print('Что хотим делать?\n Добавить книгу введите 1, Посмотреть список книг введите 2, Для завершения нажмите 3')
    enter = input()
    LIST_ACTION = '1'
    ADD_ACTION = '2'
    EXIT = '3'
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
        print(books)
    elif enter == ADD_ACTION:
        for number, book in enumerate(books):
            print(number, book['title'])
        try:
            number = int(input('Введите номер книги,для получения информации о ней: '))
            print('Автор и название книги: {author} {title}\n Год издания: {year}\n Информация о книге: {info}'.format(**books[number]))
        except:
            ValueError
            print('Такого номера книги несуществует')
    elif enter == EXIT:
        print('До свидания')
        break



