c


class Soda:

    def __init__(self, ing = None ):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')

        else:
            print('Обычная газировка')

ob1 = Soda('mmm')

ob1.show_my_drink()
