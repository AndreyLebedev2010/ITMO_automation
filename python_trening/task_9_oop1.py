# создать класс nput, принимающий 1 аргумент при инициализации  (loc)
# создать обьект earch (экземпляр класса input)
#

class Input:
    def __init__(self, loc):
        self.loc = loc


search = Input('input#search')
print(search.loc)



