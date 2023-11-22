operators = "multi"
multi_operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '%': lambda x, y: x % y
}
def operation(num1=int, num2=int, operator=operators):
    if operator in multi_operators:
        result = multi_operators[operator](num1, num2,)
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("Invalid operator")

# Example usage:
operation(5, 3, '+')  # Output: 5 + 3 = 8
operation(5, 3, '*')  # Output: 5 * 3 = 15
operation(10, 2, '/')  # Output: 10 / 2 = 5


