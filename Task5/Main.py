from itertools import permutations
from collections import Counter
import heapq

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]

def fibonacci(n):
    if n <= 1: return n
    dp = [0, 1]
    for _ in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

def find_duplicates(nums):
    count = Counter(nums)
    return [num for num, freq in count.items() if freq > 1]

def length_of_LIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def k_largest(nums, k):
    return heapq.nlargest(k, nums)

def rotate_matrix(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

def is_valid_sudoku(board):
    def is_valid_group(group):
        nums = [x for x in group if x != '.']
        return len(nums) == len(set(nums))

    for i in range(9):
        row = board[i]
        col = [board[j][i] for j in range(9)]
        if not is_valid_group(row) or not is_valid_group(col):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i+3)
                                   for y in range(j, j+3)]
            if not is_valid_group(block):
                return False

    return True

def main():
    print('Permutations of the string : ', all_permutations(input('Enter a string : ')))
    print('nth fibonnaci number is : ', fibonacci(int(input('Enter a number : '))))
    print('Duplicate elements : ', find_duplicates(list(map(int, input('Enter list of numbers : ').split()))))
    print('Length of longest increasing subset is : ', length_of_LIS(list(map(int, input('Enter list of numbers : ').split()))))
    print('The kth largest elements are : ', k_largest(list(map(int, input('Enter list of numbers : ').split())), int(input('Enter value of k : '))))
    original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('Original Matrix : ')
    for row in original_matrix:
        print(row)
    rotated_matrix = rotate_matrix(original_matrix)
    print('Rotated matrix : ')
    for row in rotated_matrix:
        print(row)
    sudoku_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [5, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    print('Is sudoku valid : ', is_valid_sudoku(sudoku_board))
    
if __name__ == '__main__':
    main()
