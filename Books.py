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



"""
А1. Вместо списка как структуры данных для одной книги удобнее использовать словарь (обсуждали с олегом это уже):
 гораздо проще ориентироваться в book["title"], book["author"] ... чем в book[0] book[1]
 в функции .format() тоже удобнее передавать словарь и юзать его как "Название: {title}, Автор: {author}".format(**book)
Кстати ты понимаешь, что значит передача параметров через * и ** ?
2. if enter == '1': - '1' - магическое значение. В маленькой программе все понятно, но если кода очень много, то тот, кто его будет читать не будет понимать что значит этот '1', для этого лучше такие вещи выносить в константы, например:

LIST_ACTION = '1'
ADD_ACTION = '2'

if enter == LIST_ACTION:
   ...
elif enter == ADD_ACTION:
   ...

3. Ты знаешь про такую штуку как globals и в частности __name__ ?
4. books[number]=book --> books[number] = book
5. books[number]=book --> books[number] = book
6. for number,book --> for number, book
7. author+' '+newbook --> author + ' ' + newbook
8. что, если я введу номер несуществующей книги? этот случай у тебя не обрабатывается и программа падает
9. почему программа завершает работу после отображения информации о книге?
10. добавь пункт меню "завершить работу"
11. books[number]=book на 20 строчке - зачем? я кажется уже спрашивал подобное в прошлый раз.
[06.03.2016 19:08:42] Андрей Богомолов: это олежику """
