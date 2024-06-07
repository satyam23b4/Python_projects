import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for cell in row:
            print(f"|   {cell}   ", end="")
        print("|")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user_move = int(input("Enter your move (1-9): "))
            if user_move < 1 or user_move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            row, col = (user_move - 1) // 3, (user_move - 1) % 3
            if board[row][col] in ['X', 'O']:
                print("The cell is already occupied. Choose another one.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free_fields.append((i, j))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    if [sign, sign, sign] in win_conditions:
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = random.choice(free_fields)
        board[move[0]][move[1]] = 'X'
        
def main():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    board[1][1] = 'X'  # Computer's first move

    while True:
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("You win!")
            break
        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("Computer wins!")
            break
        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()