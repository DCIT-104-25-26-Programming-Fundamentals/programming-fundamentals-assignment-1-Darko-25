

def calc_sum(numbers):
    """Return the sum of all numbers in the list, without using sum()."""
    total = 0
    for num in numbers:
        total += num
    return total
def calc_average(numbers):
    """Return the average of all numbers in the list."""
    return calc_sum(numbers) / len(numbers)
def calc_max(numbers):
    """Return the largest number in the list, without using max()."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
def calc_min(numbers):
    """Return the smallest number in the list, without using min()."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
if __name__ == "__main__":
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        numbers = []
        for i in range(n):
            value = int(input(f"Enter number {i + 1}: "))
         numbers.append(value)
         print("\nResults:")
        print(f"Sum:     {calc_sum(numbers)}")
        print(f"Average: {calc_average(numbers)}")
        print(f"Maximum: {calc_max(numbers)}")
        print(f"Minimum: {calc_min(numbers)}")