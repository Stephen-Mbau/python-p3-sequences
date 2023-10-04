#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    else:
        a, b = 0, 1
        fibonacci_sequence = [a, b]

        while len(fibonacci_sequence) < length:
            next_fibonacci = a + b
            fibonacci_sequence.append(next_fibonacci)
            a, b = b, next_fibonacci

        print(fibonacci_sequence)
    

print_fibonacci(0)  # Prints: []
print_fibonacci(1)  # Prints: [0]
print_fibonacci(2)  # Prints: [0, 1]
print_fibonacci(10)  # Prints the first 10 Fibonacci numbers