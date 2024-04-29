def print_board(board):
    print("\n  Tic-Tac-Toe\n")
    print("  0 | 1 | 2")
    print(" -----------")
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)}")
        if i < 2:
            print(" -----------")
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(mark != " " for row in board for mark in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!\n")
    print("Instructions:")
    print("Enter the row and column numbers to place your mark.")
    print("  0 1 2")
    print("0| | | ")
    print(" -----")
    print("1| | | ")
    print(" -----")
    print("2| | | ")

    while True:
        print_board(board)

        while True:
            try:
                row = int(input(f"Player {current_player}, enter row (0-2): "))
                col = int(input(f"Player {current_player}, enter column (0-2): "))

                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Please enter valid row and column numbers.")

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
