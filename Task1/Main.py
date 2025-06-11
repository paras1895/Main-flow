
def sum_of_two_numbers(a, b):
    return a + b

def is_odd_or_even(n):
    return "Even" if n % 2 == 0 else "Odd"

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci_sequence(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d)**power for d in digits) == n


def encrypt_message(text, shift):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in text:
        if char in lowercase:
            index = lowercase.index(char)
            new_index = (index + shift) % 26
            result += lowercase[new_index]
        elif char in uppercase:
            index = uppercase.index(char)
            new_index = (index + shift) % 26
            result += uppercase[new_index]
        else:
            result += char

    return result

def decrypt_message(text, shift=3):
    return encrypt_message(text, -shift)

def main():
    print("\n1. Sum of Two Numbers:")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", sum_of_two_numbers(a, b))

    print("\n2. Odd or Even:")
    n = int(input("Enter a number: "))
    print("Result:", is_odd_or_even(n))

    print("\n3. Factorial Calculation:")
    n = int(input("Enter a number: "))
    print("Factorial =", factorial(n))

    print("\n4. Fibonacci Sequence:")
    n = int(input("Enter the count of Fibonacci numbers: "))
    print("Fibonacci Sequence:", fibonacci_sequence(n))

    print("\n5. Reverse a String:")
    s = input("Enter a string: ")
    print("Reversed:", reverse_string(s))

    print("\n6. Palindrome Check:")
    s = input("Enter a string: ")
    print("Is Palindrome:", is_palindrome(s))

    print("\n7. Leap Year Check:")
    year = int(input("Enter a year: "))
    print("Is Leap Year:", is_leap_year(year))

    print("\n8. Armstrong Number Check:")
    num = int(input("Enter a number: "))
    print("Is Armstrong:", is_armstrong(num))

    print("\n9. Custom Encryption-Decryption:")
    msg = input("Enter the message: ")
    shift = int(input("Enter shift (e.g., 3): "))
    encrypted = encrypt_message(msg, shift)
    decrypted = decrypt_message(encrypted, shift)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()