from itertools import combinations

def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        result = []
        i = j = inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inv_count += len(left) - i
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv_count

    _, count = merge_sort(arr)
    return count

def longest_palindrome(s):
    if not s:
        return ""
    start = end = 0
    for i in range(len(s)):
        for a, b in [(i, i), (i, i+1)]:
            while a >= 0 and b < len(s) and s[a] == s[b]:
                if b - a > end - start:
                    start, end = a, b
                a -= 1
                b += 1
    return s[start:end+1]

def tsp(dist):
    n = len(dist)
    dp = {(1 << i, i): (dist[0][i], [0, i]) for i in range(1, n)}
    for r in range(2, n):
        for subset in combinations(range(1, n), r):
            bits = sum(1 << i for i in subset)
            for j in subset:
                prev = bits ^ (1 << j)
                candidates = [(dp[(prev, k)][0] + dist[k][j], dp[(prev, k)][1] + [j])
                              for k in subset if k != j and (prev, k) in dp]
                dp[(bits, j)] = min(candidates)
    bits = (1 << n) - 2
    final = [(dp[(bits, j)][0] + dist[j][0], dp[(bits, j)][1] + [0]) for j in range(1, n)]
    return min(final)

def has_cycle(graph):
    visited = set()
    def dfs(v, parent):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

def length_of_longest_substring(s):
    seen = {}
    start = max_len = 0
    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        seen[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len

def generate_parentheses(n):
    res = []
    def backtrack(s, open, close):
        if len(s) == 2 * n:
            res.append(s)
            return
        if open < n:
            backtrack(s + '(', open + 1, close)
        if close < open:
            backtrack(s + ')', open, close + 1)
    backtrack('', 0, 0)
    return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root):
    if not root:
        return []
    res, curr, left_to_right = [], [root], True
    while curr:
        level, next_level = [], []
        for node in curr:
            level.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        res.append(level if left_to_right else level[::-1])
        curr = next_level
        left_to_right = not left_to_right
    return res

def partition(s):
    res = []
    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if s[start:end] == s[start:end][::-1]:
                backtrack(end, path + [s[start:end]])
    backtrack(0, [])
    return res

def main():
    arr = [2, 4, 1, 3, 5]
    print('Array : ', arr, 'No of inversions : ', count_inversions(arr))
    print('The longest palindromic substring : ', longest_palindrome(input("Enter a string : ")))

    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    cost, path = tsp(dist)
    print("Minimum cost:", cost)
    print("Path:", path)
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        3: [4],
        4: [3]
    }
    
    print(has_cycle(graph))
    print('Length of longest substring without repetation : ', length_of_longest_substring(input("Enter a string : ")))
    print("All possible valid parenthesis are : ", generate_parentheses(int(input('Enter a number : '))))
    root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, None, TreeNode(6))
    )
    
    print('Zig Zag traversal of tree : ', zigzag_level_order(root))
    print('All possible palindrome substrings are : ', partition(input('Enter a string : ')))

if __name__ == "__main__":
    main()
