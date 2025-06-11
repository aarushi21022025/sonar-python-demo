def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        # return "Cannot divide by zero"
        print("Cannot divide by zero")  # Bad practice
        return None
    return a / b

def convert_to_minutes(hours):
    return hours * 60  # Magic number

def evaluate_expression(expr):
    return eval(expr)  # Security issue

def unused_function():
    print("I am never called")

try:
    x = 1 / 0
except:
    pass  # Silent fail

if __name__ == "__main__":
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
