import math

def multiplication_table(n):
    print('Table of', n, ':')
    for i in range(1, 11):
        print(n, '*', i, '=', i*n)

def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    print('After swapping a :', a, 'b :', b)

def is_substring(s1, s2):
    if s2 in s1:
        return True
    return False

def decimal_to_binary(n):
    bin = ""
    if n == 0:
        bin = "0"
    while n > 0:
        bin += '1' if n % 2 == 1 else '0'
        n = n // 2
    print('binary :', bin[::-1])

def matrix_addition(mat1, mat2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]
    print(result)

def matrix_multiplication(mat1, mat2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            for k in range(len(mat1)):
               result[i][j] += mat1[i][k] * mat2[k][j] 
    print(result)

board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(b, player):
    win_combos = [(0,1,2), (3,4,5), (6,7,8),
                  (0,3,6), (1,4,7), (2,5,8),
                  (0,4,8), (2,4,6)]
    return any(b[i] == b[j] == b[k] == player for i,j,k in win_combos)

def is_draw():
    return ' ' not in board

def minimax(b, depth, is_max):
    if check_winner(b, 'O'):
        return 1
    elif check_winner(b, 'X'):
        return -1
    elif is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best = min(best, score)
        return best

def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != ' ' or move not in range(9):
                print("Invalid move, try again.")
                continue
        except:
            print("Please enter a valid number.")
            continue

        board[move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        print("AI's turn:")
        move = best_move()
        board[move] = 'O'
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

def main():
    multiplication_table(int(input('Enter a number : ')))
    swap(int(input('Enter first number (a): ')), int(input('Enter second number (b): ')))
    print(is_substring(input('Enter first string : '), input('Enter second string : ')))
    decimal_to_binary(int(input('Enter a number : ')))
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    matrix_addition(mat1, mat2)
    matrix_multiplication(mat1, mat2)
    play_game()

if __name__ == "__main__":
    main()
