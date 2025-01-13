from projects.Fruit import Fruit


class AmericanFruit(Fruit):
    def __init__(self, name, flavor, color, location):
        super().__init__(name, flavor, color)
        self.location = location

    def description(self):
        print(f'I am an American fruit and I taste {self.flavor}')


if __name__ == '__main__':
    lemon = Fruit(name='Lemon', flavor='sour', color='green')
    lemon.description()
    washingtonApple = AmericanFruit(name='Apple', flavor='sweet', color='red', location='America')
    washingtonApple.description()

