

def print_single_table(number):
    """Print the multiplication table for a single number, 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:<2} =  {number * i}")


def print_tables_up_to_n(n):
    """Print multiplication tables for every number from 1 to n."""
    for num in range(1, n + 1):
        print_single_table(num)
        if num != n:
            print("-" * 27)


if __name__ == "__main__":

    print("=== Part A: Single Table ===")
    number = int(input("Enter a number: "))
    print_single_table(number)

    print("\n=== Part B: Tables from 1 to N ===")
    n = int(input("Enter a number N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to_n(n)