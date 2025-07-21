from collections import deque

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

def word_frequency(text):
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    
    words = cleaned_text.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

def knapsack_01(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
   
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]

        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)

    return merged

def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

def maximal_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    def largest_rectangle_area(heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()
        return max_area

    max_rect = 0
    n_cols = len(matrix[0])
    heights = [0] * n_cols

    for row in matrix:
        for i in range(n_cols):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        max_rect = max(max_rect, largest_rectangle_area(heights))

    return max_rect

def max_subarray_sum(nums):
    if not nums:
        return 0

    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global

def word_ladder_length(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])

    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == endWord:
            return steps
        
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, steps + 1))

    return 0

def main():
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
    print(is_valid_sudoku(sudoku_board))
    print(word_frequency(input("Enter a string : ")))
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    
    print(knapsack_01(weights, values, capacity))
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print('Intervals : ', intervals)
    print('Merged intervals : ', merge_intervals(intervals))
    print('Median of two arrays is : ', find_median_sorted_arrays(list(map(int, input('Enter first array : ').split())), list(map(int, input('Enter second array : ').split()))))

    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print('Area of largest rectangle is : ', maximal_rectangle(matrix))
    print('Maximum sum of subarray is : ', max_subarray_sum(list(map(int, input('Enter a array of integers : ').split()))))
    begin = "hit"
    end = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(word_ladder_length(begin, end, wordList))
    
if __name__ == "__main__":
    main()