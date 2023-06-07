a: int = 5
b: str = 'строка'
с: list = [1, 2]

def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s

print(indent('123', 123))

def a(s: str = '') -> int:
    return len(s)

def b(a: list, b: list) -> int:
    return max(len(a), len(b))

def c(l = [1, 2]):
    l.append(3)
    return l
print(c())