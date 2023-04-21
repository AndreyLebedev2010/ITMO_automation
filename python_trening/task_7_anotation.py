a: int = 5
b: str = 'stroka'
c: list = 'spisok' [1, 2]


def indent(s: str, width: int) ->str:
     return " " * (max(0, width - len(s))) +s


print(indent('123', 123))