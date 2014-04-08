from stack import Stack

def calculate():
    calculator_input = raw_input("Enter expression to evaluate: ")
    values = Stack()
    tokens = calculator_input.strip().split()
    for token in tokens:
        try:
            operand = int(token)
            values.push(operand)
        except ValueError:
            if token in ("+", "-", "*", "/", "%"):
                operator = parseOperator(token)
            else:
                raise ValueError("Unrecognized token")

