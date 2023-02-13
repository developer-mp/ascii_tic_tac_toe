# Game initial setup
print("Welcome to Tic-Tac-Toe game!")
print(" ")
print("|1|2|3|", "|4|5|6|", "|7|8|9|", sep="\n")
print(" ")
print("Make a move X or O by turn \nPlayer X starts first (type the cell's number from 1 to 9)")
print(" ")

# Game board which will be updated with X or O depending on user input
BOARD = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

# Winning number combos which will be checked after each move
WINNING_COMBO = [
    "123", 
    "456", 
    "789", 
    "147", 
    "258", 
    "369",
    "159",
    "357"
]

# Checking if board has empty values
def board_has_empty_cells():
    for i in range (1,10):
        while BOARD[i] == " ":
            return True
        
# Clearing all values from board            
def clear_board():
    for i in range(1,10):
        BOARD[i] = " "
    return BOARD
    
# Printing the game board with updated values X or O
def print_board():
   print("|" + BOARD[1] + "|" + BOARD[2] + "|" + BOARD[3] + "|")
   print("|" + BOARD[4] + "|" + BOARD[5] + "|" + BOARD[6] + "|")
   print("|" + BOARD[7] + "|" + BOARD[8] + "|" + BOARD[9] + "|")
   return

# Reseting all game values            
def reset_game():
    
    global move, play_x, play_o, combo_x, combo_o
    
    move = 1
    play_x = []
    play_o = []
    combo_x = " "
    combo_o = " "
    return

def another_game():
    
    reset_game()
    clear_board()
    global message
    
    while True:
        message = input("Type 'Play' to start again: \nType 'Quit' to quit the game: ") 
        if message.lower() not in ("quit", "play"):
            print(" ")
            print("Input is not recognized, please try again")
            print(" ")
        else:
            if message.lower() == "quit":
                clear_board()
                reset_game()
                return False
            else:
                clear_board()
                reset_game()
                return True

def validation_rules():
    
    global message

    if message.isdigit() == False:
        print("Input is not a number, please enter a number")
    else:
        if int(message) > 9 or int(message) <= 0:
            print("The cell is out of range, please try again!")
            return False
        elif BOARD[int(message)] != " ":
            print("The cell has been used, please try another one!")
            return False
        else:
            return True
    
# Main function
message = " "
move = 1
play_x = []
play_o = []
combo_x = " "
combo_o = " "

while board_has_empty_cells() == True:
    if move % 2 != 0:
        message = input("Player X move: ")
        if validation_rules() != True:
            print(" ")
        else:
            BOARD[int(message)] = "X"
            play_x.append(message)
            play_x.sort()
            combo_x = "".join(play_x)
            print(" ")
            print_board()
            move += 1
            print(" ")
    else:
        message = input("Player O move: ")
        if validation_rules() != True:
            print(" ")
        else:
            BOARD[int(message)] = "O"
            play_o.append(message)
            play_o.sort()
            combo_o = "".join(play_o)
            print(" ")
            print_board()
            move += 1
            print(" ")

    if len(combo_x) >= 3 and any(c in combo_x for c in WINNING_COMBO):
        print("Player X has won!")
        print(" ")
        if another_game() == False:
            break
        print(" ")
    elif len(combo_o) >= 3 and any(c in combo_o for c in WINNING_COMBO):
        print("Player O has won!")
        print(" ")
        if another_game() == False:
            break
        print(" ")
    else:
        if board_has_empty_cells() == None:
            print("Draw")
            print(" ")
            if another_game() == False:
                break
            print(" ")

