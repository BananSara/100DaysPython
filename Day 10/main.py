#calculator app
num1 = int(input('enter the first number:'))
num2 = int(input('enter the second number:'))

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2


operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
    }


for symbol in operations:
    print(symbol)
    
operation_symbol = input('pick an operation from the line above: ')

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)
print(f'the answer is:\n {num1} {operation_symbol} {num2} = {answer}')