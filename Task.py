def rectangle_area(width, height):
    return height * width
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

print(rectangle_area(78,56))
print(is_even(4))
print(is_even(5))
print(sum_digits(1434))