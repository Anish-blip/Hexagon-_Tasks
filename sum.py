# sum.py
import sys

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

if __name__ == "__main__":
    # Input from the command line argument
    if len(sys.argv) != 2:
        print("Usage: python sum.py <4-digit-number>")
        sys.exit(1)

    number = int(sys.argv[1])
    
    # Check if the number is 4 digits
    if 1000 <= number <= 9999:
        result = sum_of_digits(number)
        print(f"The sum of the digits of {number} is {result}")
    else:
        print("Please enter a valid 4-digit number.")

