def check_winner(board):
    for row in board:
        if all(cell == row[0] and cell != '.' for cell in row):
            return row[0]
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != '.' for row in range(3)):
            return board[0][col]
    if all(board[i][i] == board[0][0] and board[i][i] != '.' for i in range(3)):
        return board[0][0]
    if all(board[i][2 - i] == board[0][2] and board[i][2 - i] != '.' for i in range(3)):
        return board[0][2]
    return 'DRAW'
def main():
    t = int(input())
    for _ in range(t):
        board = [input().strip() for _ in range(3)]
        result = check_winner(board)
        print(result)

    main()

