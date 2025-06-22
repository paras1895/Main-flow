import math

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def lcm_and_gcd(a, b):
    gcd = math.gcd(a, b)
    print('GCD : ', gcd)
    print('LCM : ', abs(a * b) // gcd)

def reverse_list():
    list = input('Enter sequence of numbers : ').split()
    print('Reversed list : ', list[::-1])

def sort_list():
    l = list(map(int, input('Enter numbers for list: ').split()))
    sorted_list = sorted(l)
    print('Sorted list : ', sorted_list)

def remove_duplicates():
    l = list(map(int, input('Enter numbers for list : ').split()))
    unique_list = set(l)
    print('List without duplicates: ', unique_list)

def length_of_string(str):
    len = 0
    for char in str:
        len += 1
    return len

def vowels_and_consonants(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowel_count = 0
    consonant_count = 0
    for char in str:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    print('Vowels : ', vowel_count, 'Consonants : ', consonant_count)

def main():
    print(is_prime(int(input('Enter a number : '))))
    print('Sum of digits : ', sum_of_digits(int(input('Enter a number : '))))
    lcm_and_gcd(int(input('Enter first number : ')), int(input('Enter second number : ')))
    reverse_list()
    sort_list()
    remove_duplicates()
    print('Length of the string is : ' , length_of_string(input('Enter a string : ')))
    vowels_and_consonants(input('Enter a string : '))

if __name__ == "__main__":
    main()
