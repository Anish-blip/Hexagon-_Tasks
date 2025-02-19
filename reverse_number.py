#!/usr/bin/env python3
import sys

def reverse_number(n):
    """Recursively reverse the digits of an integer."""
    def helper(n, rev=0):
        if n == 0:
            return rev
        else:
            return helper(n // 10, rev * 10 + n % 10)
    return helper(n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: reverse_number.py <number>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
    
    result = reverse_number(num)
    print(f"Reversed number: {result}")

