#task1 
def swap_and_compare(x, y):
    """
    Swaps the values of x and y, then compares them to their original values.

    Parameters:
    x (int/float): The first value.
    y (int/float): The second value.

    Returns:
    tuple: A tuple containing the swapped values and a boolean indicating if the swap was successful.
    """
    original_x, original_y = x, y  # Storing original values for comparison

    # Swapping values
    x, y = y, x

    # Comparing original and swapped values
    is_swapped = (x == original_y) and (y == original_x)

    return (x, y, is_swapped)

# Example usage
x = 5
y = 10
swapped_x, swapped_y, is_swapped = swap_and_compare(x, y)

print(f"Original values: x = {x}, y = {y}")
print(f"Swapped values: x = {swapped_x}, y = {swapped_y}")
print(f"Values successfully swapped: {is_swapped}")

#task2
def is_perfect_square(number):
    """
    Determine if a given number is a perfect square.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is a perfect square, False otherwise.
    """
    if number < 0:
        return False  # Negative numbers cannot be perfect squares

    sqrt = int(number ** 0.5)
    return sqrt**2 == number

# Example usage
num = 16
print(f"{num} is a perfect square: {is_perfect_square(num)}")
