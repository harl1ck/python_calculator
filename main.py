import math

z = ""
try:
    a = float(input("Введите первое число:"))
    z = str(input("Введите знак операции (+, -, *, /, **, sqrt, !, sin, cos, tan):"))

    if not (z == "sqrt" or z == "!" or z == "sin" or z == "cos" or z == "tan"):
        b = float(input("Введите второе число:"))
except (ValueError):
    print("НЕ ЧИСЛО")

    match z:
        case "+": print(a + b)
        case "-": print(a - b)
        case "*": print(a * b)
        case "/":
            if b == 0:
                print("Я не могу посчитать :_(")
            else:
                print(a / b)
        case "**": print(a ** b)
        case "sqrt": print(math.sqrt(a))
        case "!": print(math.factorial(a))
        case "sin": print(math.sin(a))
        case "cos": print(math.cos(a))
        case "tan": print(math.tan(a))


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