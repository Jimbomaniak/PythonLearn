class Technology():
    def __init__(self, firm):
        self.firm = firm

    def secret(self):
        if self.firm.lower() == 'nike':
            print('Adding secret ingridient for Nike shoes')
        elif self.firm.lower() == 'adidas':
            print('Adding secret ingridient for Adidas shoes')


class Shoes():
    def __init__(self, size=None, color=None, sex=None, firm=None):
        self.size = size
        self.color = color
        self.sex = sex
        self.firm = firm

    def __str__(self):
        return '{0.size}, {0.color}'.format(self)


class Nike(Shoes):
    def __init__(self, size=None, color=None, sex=None, firm='Nike'):
        Shoes.__init__(self, size, color, sex, firm)
        self.firm = Technology(firm)


class Adidas(Shoes):
    def __init__(self, size=None, color=None, sex=None, firm='ADiDas'):
        Shoes.__init__(self, size, color, sex, firm)
        self.firm = Technology(firm)


class ShopOfShoes():
    def __init__(self, city, type):
        self.city = city
        self.type = type

    def __str__(self):
        return 'City - {0.city}'.format(self)


class Megasport(ShopOfShoes):
    def __init__(self, city, adress, type):
        ShopOfShoes.__init__(self, city, type)
        self.adress = adress
        self.production = Nike(), Adidas()


if __name__ == '__main__':
    shop1 = Megasport('Kiev', 'Hreshatik 2/14', 'sportshop')
    for shoes in shop1.production:
        shoes.firm.secret()
