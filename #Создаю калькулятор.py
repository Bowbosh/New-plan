#Создаю калькулятор
#Мне нужны 4 функции с возвратом результата(наверное)
def plus(num_1, num_2):
    return (num_1 + num_2)
num_1 = int(input('Введите первое число'))
num_2 = int(input('Введите второе число'))
print(f'plus of {num_1} and {num_2} is {plus(num_1, num_2)}')


def minus(num_1, num_2):
    return (num_1 - num_2)
num_1 = int(input('Введите первое число'))
num_2 = int(input('Введите второе число'))
print(f'minus of {num_1} and {num_2} is {minus(num_1, num_2)}')

def mult(num_1, num_2):
    return (num_2 * num_2)
num_1 = int(input('Введите первое число'))
num_2 = int(input('Введите второе число'))
print(f'mult of {num_1} and {num_2} is {mult(num_1, num_2)}')


def delenie(num_1, num_2):
    return (num_1 / num_2)
num_1 = int(input('Введите первое число'))
num_2 = int(input('Введите второе число'))
print(f'delenie of {num_1} and {num_2} is {delenie(num_1, num_2)}')

