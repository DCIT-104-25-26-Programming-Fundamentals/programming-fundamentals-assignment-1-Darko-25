

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b, rounded to 2 decimal places, or None if b is 0."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return the remainder of a divided by b, or None if b is 0."""
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    """Return a raised to the power of b."""
    return a ** b


def print_menu():
    """Display the calculator menu options."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_two_numbers():
    """Prompt for and return two numbers from the user."""
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    return a, b


if __name__ == "__main__":
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponentiate),
    }

    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")
        print()

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in operations:
            symbol, operation = operations[choice]
            a, b = get_two_numbers()

            if choice in ("4", "5") and b == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = operation(a, b)
                # Print numbers as ints when they have no decimal part
                a_display = int(a) if a == int(a) else a
                b_display = int(b) if b == int(b) else b
                print(f"Result: {a_display} {symbol} {b_display} = {result}")
        else:
            print("Error: Please enter a number from 1 to 7.")

        print()