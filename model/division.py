operation_mark = '/'
x = 0
y = 0


def init(a, b):
    global x
    global y
    x = a
    y = b


def calc():
    if y == 0:
        return
    return x / y
