def calculator(num1, num2, operation):
    """Perform arithmetic, raising ValueError for unsupported operations.

    Raise ZeroDivisionError when dividing by zero.
    """
    if operation == "add":
        return num1 + num2
    if operation == "subtract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    raise ValueError(f"Unsupported operation: {operation}")