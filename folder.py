#creating board
""" 00 01 02 03 04 05 06
    10 11 12 13 14 15 16
    20 21 22 23 24 25 26
    30 31 32 33 34 35 36
    40 41 42 43 44 45 46
    50 51 52 53 54 55 56"""
rows = 6
col =7

def print_board(board):
    for row in board:
        print("|" + "|".join(row)+ "|") #.join helps in merging 
        print("-" *(2 * col + 1))
    print()
#checking winner 
def check_winner(board, player):
    #checking for horizontal wins in rows
    for row in board:
        for i in range (4):
            if all(piece == player for piece in row[i:i+4]): 
        #all checks if all the elements in an iterable are true 
        #row [i:i+4] = [start : end]used slicing to get 
        #a part of the matrix to check if they are same 4
                return True
    #checkin for vertical wins in colums 
    for col in range(7):
        for i in range (3): # starts checking from 00, 10, 20, 30 || 01, 02, 03, 04
            if all(row[col] == player for row in board[i:i+4]):
                return True
    #checking for cross wins 
    for row in range(3):
        for col in range(4):
            #calculations while row 0 col is 0 (00, 11, 22, 33) and so on
            if all(board[row+i][col+i] == player for i in range(4)):
                return True 
    #checking for right diagonal 
    for row in range(3,6):
        for col in range(4):
            if all(board[row-i][col+i] == player for i in range(4)):
                return True 
    return False

#check if the board is completely filled 
def is_full(board):
    return all(piece != ' ' for row in board for piece in row)

def main():
    board = [[' ' for _ in range (7)] for _ in range(6)]
    player = 'X' 

    while True:
        print_board(board)
        column= int(input(f"Player {player} enter a col 0-6 :"))

        if column < 0 or column > 6:
            print("the input is not valid!")
            continue 
        #checking if the column entered by the user is valid or not
        for row in range (5, -1, -1):
            if board[row][column] == ' ':
                board[row][column] = player 
                break
            else: 
                print("the column is full")
                continue 
        #printing the winner 
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break 
        #checking if the board is full 
        if is_full(board):
            print_board(board)
            print("tie!")
            break
        
        if player == 'X':
            player = 'O'
        else:
            player= 'X'
main()