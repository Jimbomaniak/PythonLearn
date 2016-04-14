class PowerPlant():
    def __init__(self, power, location, name='Power Water Reactor'):
        self.power = power
        self.location = location
        self.name = name


class Zaes(PowerPlant):
    def __init__(self, power=6000, location='Enerhodar'):
        PowerPlant.__init__(self, power, location)

    def work(self):
        print('All block are working fine')

    def add_block(self):
        number = input('Enter nubmer of block: ')
        capacity = int(input('Enter capacity of block: '))
        self.block = Block(number, capacity)
        return self.block


class Raes(PowerPlant):
    def __init__(self, power=4000, location='Rovno'):
        PowerPlant.__init__(self, power, location)

    def add_power(self):
        self.power = self.power + 1000
        return self.power

    def create_reactor(self):
        name = input('Enter name of reactor: ')
        self.reactor = Reactor(name)
        print(self.reactor)


class Block():
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def __str__(self):
        return 'Block {0.number} with Capacity - {0.capacity}'.format(self)


class Reactor():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Reactor {0.name} ready'.format(self)


if __name__ == '__main__':
    my = Zaes()
    my.add_block()
    print(my.block)
    my1 = Raes()
    my1.create_reactor()

