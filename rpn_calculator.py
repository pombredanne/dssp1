from stack import Stack

def calculate():
    operators = {
        "*": lambda left, right: left * right,
        "-": lambda left, right: left - right,
        "+": lambda left, right: left + right,
        "/": lambda left, right: left / right,
        "%": lambda left, right: left / right,
    }

    calculator_input = raw_input("Enter expression to evaluate: ")

    values = Stack()
    tokens = calculator_input.strip().split()

    for token in tokens:
        try:
            operand = int(token)
            values.push(operand)
        except ValueError:
            if token in ("+", "-", "*", "/", "%"):
                right = values.pop()
                left = values.pop()
                result = operators[token](left, right)
                values.push(result)
            else:
                raise ValueError("Unrecognized token")

    return values.pop()

