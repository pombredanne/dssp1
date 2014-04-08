from stack import Stack

def calculate(calculator_input):
    operators = {
        "*": lambda left, right: left * right,
        "-": lambda left, right: left - right,
        "+": lambda left, right: left + right,
        "/": lambda left, right: left / right,
        "%": lambda left, right: left / right,
    }

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

if __name__ == '__main__':
    calculator_input = raw_input("Enter expression to evaluate: ")
    calculate(calculator_input)

