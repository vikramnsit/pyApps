class Fruit:

    def __init__(self, name, flavor, color):
        self.name = name
        self.flavor = flavor
        self.color = color

    def description(self):
        print(f'I am {self.name} and I taste {self.flavor} and my color is {self.color}')


