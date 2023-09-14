import math
b = 0
a = int(input("Введите первое число:"))
z = str(input("Введите знак операции (+, -, *, /, **, sqrt, !, sin, cos, tan):"))
if not (z == "sqrt" or z == "!" or z == "sin" or z == "cos" or z == "tan"):
    b = int(input("Введите второе число:"))

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