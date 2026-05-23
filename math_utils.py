def validate_numbers(a, b):
    
    if isinstance(a, bool) or isinstance(b, bool): # чекаем чтоб не булевая
        raise TypeError("Принимаемые аргументы должны быть int или float, не bool")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)): # чекаем что инт или флоат
        raise TypeError("Принимаемые аргументы должны быть int или float")

def add(a, b):
    validate_numbers(a, b)
    return a + b

def subtract(a, b):
    validate_numbers(a, b)
    return a - b

def multiply(a, b):
    validate_numbers(a, b)
    return a * b

def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b