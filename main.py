import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def modify(a, b):
    return a * b


def divide(a, b):
    return a / b


def pow(a, b):
    return a ** b


def sqrt(a):
    return math.sqrt(a)


def factorial(a):
    return math.factorial(int(a))


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tan(a):
    return math.tan(a)
z = ""
try:
    a = float(input("Введите первое число:"))
    z = str(input("Введите знак операции (+, -, *, /, **, sqrt, !, sin, cos, tan):"))

    if not (z == "sqrt" or z == "!" or z == "sin" or z == "cos" or z == "tan"):
        b = float(input("Введите второе число:"))
except ValueError:
    print("НЕ ЧИСЛО")

match z:
    case "+": print(add(a, b))
    case "-": print(subtract(a, b))
    case "*": print(modify(a, b))
    case "/":
        if b == 0:
            print("Я не могу посчитать :_(")
        else:
            print(divide(a, b))
    case "**": print(pow(a, b))
    case "sqrt":
        try:
            print(sqrt(a))
        except ValueError:
            print("Число не подходит")
    case "!":
        try:
            print(factorial(a))
        except ValueError:
            print("Число не подходит")
    case "sin": print(sin(a))
    case "cos": print(cos(a))
    case "tan": print(tan(a))

