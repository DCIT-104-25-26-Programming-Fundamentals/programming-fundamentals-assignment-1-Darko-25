

def generate_fibonacci(n):
    """Return a list of the first n Fibonacci numbers, using a loop."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_fibonacci(num):
    """Return True if num appears in the Fibonacci sequence, using a loop."""
    if num < 0:
        return False

    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False


if __name__ == "__main__":

    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        fib_sequence = generate_fibonacci(n)
        fib_strings = [str(num) for num in fib_sequence]
        print("Fibonacci sequence: " + " ".join(fib_strings))


    num_to_check = int(input("Enter a number to check: "))

    if is_fibonacci(num_to_check):
        print(f"{num_to_check} is a Fibonacci number.")
    else:
        print(f"{num_to_check} is NOT a Fibonacci number.")