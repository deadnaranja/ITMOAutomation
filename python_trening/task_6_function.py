       # определяем функцию
def add(x, y,):
    return (x + y)

      # вызов функции
print(add(1, 2,))

# вызываем функцию с другими аргументами

print(add('i am ', 'tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))
print(arg(2, 2))
print(arg(2, 2, 1, 1))

def range_arg(a, b, c, d):
    return a + '' + b + '' + c + '' + d + ''

print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d='3', c='4'))



def fun(a = (1, 2, 3, 4)):
    return a[0]
print(fun())
