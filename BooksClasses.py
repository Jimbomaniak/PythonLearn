class Books:
    def __init__ (self, author, title, year, info):
        self.author = author
        self.title = title
        self.year = year
        self.info = info
    def showInfo(self):
        print('Автор книги: {0}\nНазвание книги: {1}\nГод изания: {2}\nОписание книги: {3}'.format(self.author, self.title, self.year, self.info))
book1 = Books('Толстой', 'Война и Мир', '1877', 'Книга о войне')
book1.showInfo()
