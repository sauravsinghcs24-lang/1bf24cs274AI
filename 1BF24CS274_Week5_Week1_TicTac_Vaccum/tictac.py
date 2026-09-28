import random

# Create empty board
board = [" "] * 9


# Display the board
def display_board():
    print()
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print()


# Check winner
def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Check draw
def is_draw():
    return " " not in board


# Human move
def human_move():
    while True:
        position = int(input("Enter position (1-9): "))

        if position < 1 or position > 9:
            print("Enter a number between 1 and 9.")
        elif board[position - 1] != " ":
            print("Position already occupied.")
        else:
            board[position - 1] = "X"
            break


# Computer move
def computer_move():
    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    position = random.choice(empty_positions)
    board[position] = "O"

    print("Computer selected position:", position + 1)


# Main game
print("===== TIC-TAC-TOE =====")
print("Human = X")
print("Computer = O")

while True:

    display_board()

    # Human turn
    human_move()

    if check_winner("X"):
        display_board()
        print("Human Wins!")
        break

    if is_draw():
        display_board()
        print("Game Draw!")
        break

    # Computer turn
    computer_move()

    if check_winner("O"):
        display_board()
        print("Computer Wins!")
        break

    if is_draw():
        display_board()
        print("Game Draw!")
        break