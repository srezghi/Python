import random

### Global variables to store the number of win, loss or tie of each legal moves. 
win = 0
loss = 0
tie = 0
stats = []
best_stats = []
temp_var = True

### Prints the current board of the game
def game_board(board):
    print("       |       |       ")
    print("\n   "+board[0]+"   |   "+board[1]+"   |   "+board[2])
    print("\n       |       |       ")
    print("\n-------|-------|-------")
    print("\n       |       |       ")
    print("\n   "+board[3]+"   |   "+board[4]+"   |   "+board[5])
    print("\n       |       |       ")
    print("\n-------|-------|-------")
    print("\n       |       |       ")
    print("\n   "+board[6]+"   |   "+board[7]+"   |   "+board[8])
    print("\n       |       |       ")

### Returns whether the board is full or not
def board_is_full(board):
    if (" " in board):
        return False
    else:
        return True

### Returns whether the board given board and character is winner or not
def winner(board, X_or_O):
    if (board[0] == X_or_O and board[1] == X_or_O and board[2] == X_or_O or 
        board[3] == X_or_O and board[4] == X_or_O and board[5] == X_or_O or    
        board[6] == X_or_O and board[7] == X_or_O and board[8] == X_or_O or 
        board[0] == X_or_O and board[3] == X_or_O and board[6] == X_or_O or 
        board[1] == X_or_O and board[4] == X_or_O and board[7] == X_or_O or 
        board[2] == X_or_O and board[5] == X_or_O and board[8] == X_or_O or 
        board[0] == X_or_O and board[4] == X_or_O and board[8] == X_or_O or 
        board[2] == X_or_O and board[4] == X_or_O and board[6] == X_or_O):
        return True
    else:
        return False

### Takes the user move
def user_move(board, user_x_or_o):
    user_choice = input("\n\n\nYour trun: ")
    user_choice = int(user_choice)
    board[user_choice - 1] = user_x_or_o
    game_board(board)

### Returns the legal moves in the board
def get_legal_moves(board):
    ### Making the list of legan moves 
    legal_moves = []
    for i in range(0,9):
        if(board[i] == " "):
            legal_moves.append(i)
    return legal_moves

### Playing the game for the computer/AI
def computer_move(board, computer_x_or_o, user_x_or_o):
    global temp_var
    global stats
    ### Perform playout
    legal_moves = get_legal_moves(board)

    ### Make the stats list based on the legal moves size
    stats = []
    for i in range(0, len(legal_moves)):
        stats.append(0)

    z = 0
    while (z < 100):
        for j in range(0,len(legal_moves)):
            ### Assigning computer's move in the board
            board_copy = []
            for i in range(0,len(board)):
                board_copy.append(" ")
                if (board[i] != " "):
                    board_copy[i] = board[i]
                else:
                    board_copy[i] = " "

            ### Assigning legal moves to the board for random playouts
            board_copy[legal_moves[j]] = computer_x_or_o
            win = 0
            loss = 0
            tie = 0

            temp1 = True
            while (temp1 == True):
                ### Taking the random user move for playout
                if (board_is_full(board_copy)):
                    ### Game is a tie
                    ### Update the stats
                    tie += 1
                    temp1 = False

                else:
                    user__choice = random.randint(0,8)
                    while (board_copy[user__choice] != " "):
                        user__choice = random.randint(0,8)
                    board_copy[user__choice] = user_x_or_o

                if (temp1 == False):
                    break

                ### Checking if the random move was a win for the user
                for i in range(1,10):
                    if (board_copy[i - 1] == " "):
                        board_copy[i - 1] = computer_x_or_o
                        if winner(board_copy, user_x_or_o):
                            board_copy[(i - 1)] = computer_x_or_o
                            ### Update stat with Loss
                            loss += 1
                            temp1 = False
                            break
                        else:
                            board_copy[i - 1] = " "
                
                if (temp1 == False):
                    break

                ### Computer move
                ### Checking if the next move is a win for the computer 
                for i in range(1,10):
                    if (board_copy[i - 1] == " "):
                        board_copy[i - 1] = computer_x_or_o
                        if winner(board_copy, computer_x_or_o):
                            board_copy[(i - 1)] = computer_x_or_o
                            ### Update stat with Win
                            win += 1
                            temp1 = False
                            break
                        else:
                            board_copy[i - 1] = " "
                
                if (temp1 == False):
                    break

                ### Checking if the next move is a win for the user and block it
                temp2 = False
                for i in range(1,10):
                    if (board_copy[i - 1] == " "):
                        board_copy[i - 1] = user_x_or_o
                        if winner(board_copy, user_x_or_o):
                            board_copy[(i - 1)] = computer_x_or_o
                            temp2 = True
                            break
                        else:
                            board_copy[i - 1] = " "

                ### If computer's next move isn't a win or blocking the user
                ### It aims to take a corner or the center
                if (temp2 == False):
                    if (board_is_full(board_copy) == True):
                        ### This is a tie
                        ### Update the stats
                        tie += 1
                        temp1 = False

                    else:
                        options = [0, 2, 4, 6, 8]
                        temp3 = False
                        for i in range(0,5):
                            if (board_copy[options[i]] == " "):
                                temp3 = True
                                break
                        
                        ### Goes to this if statement if any corners or center spots are empty
                        if (temp3):
                            computer__choice = random.randint(0,4)
                            while (board_copy[options[computer__choice]] != " "):
                                computer__choice = random.randint(0,4)
                            board_copy[options[computer__choice]] = computer_x_or_o
                            if (board_is_full(board_copy)):
                                ### Tie situation
                                tie += 1
                                break

                        ### Goes to this else statement if corners or center spots are all taken
                        ### so the code takes any other edge squares 
                        else:
                            options = [1, 3, 5, 7]
                            computer__choice = random.randint(0,3)
                            while (board_copy[options[computer__choice]] != " "):
                                computer__choice = random.randint(0,3)
                            board_copy[options[computer__choice]] = computer_x_or_o
                            if (board_is_full(board_copy)):
                                ### Tie situation
                                tie += 1
                                break

            ### Update the stats list for this move
            stats[j] = win + tie - loss
        
        ### Find the best move based on the stats
        if (temp_var):
            for i in range(0,len(stats)):
                best_stats.append(0)
            temp_var = False

        for i in range(0, len(stats)): 
            best_stats[i] += stats[i]
        
        if (j == 8):
            stats = []
            ### Make the stats list based on the legal moves size
            for i in range(0, len(legal_moves)):
                stats.append(0)

        z += 1

    ### After the end of the playouts, record the best stats
 
    index = 0
    largest = best_stats[0]
    for i in range(0,len(stats)):
        if (largest < best_stats[i]):
            largest = best_stats[i]
            index = i

    while (board[legal_moves[index]] != " "):
        index = 0
        largest = best_stats[0]
        for i in range(0,len(stats)):
            if (largest - 200 < best_stats[i]):
                largest = best_stats[i]
                index = i

    ### Put the computer move in the primary board
    board[legal_moves[index]] = computer_x_or_o

    ### Display the result
    print("\n\n\nHere is my move: \n")
    game_board(board)


def play_a_new_game():
    ### Initializing the board of the game using the following list of  size 9
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    print("\n\nWelcome to ~~~~~ TIC-TAC-TOE ~~~~~")
    print("Let's have some fun playing together !!")
    print("But I bet you are not as smart as I am ;) \n")

    ### Asking the user if they want to be X or O
    user_x_or_o = input("Do you want to be  - X -  or  - O - :  ")
    
    ### Initializing the computer's X or O based on the user's input above
    if (user_x_or_o == 'X' or user_x_or_o == 'x' ):
        computer_x_or_o = 'O'
        user_x_or_o = 'X'
    else:
        computer_x_or_o = 'X'
        user_x_or_o = 'O'
    
    ### Making sure who is X and who is O 
    print("\nAlright, I play with -", computer_x_or_o,"- and you with -", user_x_or_o, "-\n")

    ### Asking user if they want to go first. If not, the computer will begin the game
    who_first = input("Would you like to go first? Answer with [y/n]: ")

    ### Checking who is going first based on the user's decision
    if (who_first == 'y'):
        print("\nAlright, take your first move wisely!\n")
    else:
        print("\nAlright, I will take the first move then :)\n")

    ### Starting the game by showing the X_O board
    print("Here is our board. Take any number between 1-9 to choose the spot you want. \n\n")        
    game_board(board)
    
    ### Resume the game based on who is going first
    terminate = False
    ### If user is going first:
    if (who_first == 'y'):
        while (terminate != True):
            for i in range(0,4):
                ### User's turn
                user_move(board, user_x_or_o)
                if (winner(board, user_x_or_o)):
                    print("\nCongrats! You Won! \n")
                    terminate = True
                    break
                    
                ### Computer's turn
                computer_move(board, computer_x_or_o, user_x_or_o)
                if (winner(board, computer_x_or_o)):
                    print("\nI Won! Try harder next time! \n")
                    terminate = True
                    break

            ### Last move: User's turn
            if (terminate == False):
                user_move(board, user_x_or_o)
                if (winner(board, user_x_or_o)):
                    print("\nCongrats! You Won! \n")
                    terminate = True
                else:
                    ### Tie situation
                    print("\nTie! It was a good game! I'll beat you next time!!\n")
                    terminate = True
    
    else:
        while (terminate != True):
            for i in range(0,4):
                ### Computer's turn
                computer_move(board, computer_x_or_o, user_x_or_o)
                if (winner(board, computer_x_or_o)):
                    print("\nI Won! Try harder next time! \n")
                    terminate = True
                    break
                     
                ### User's turn
                user_move(board, user_x_or_o)
                if (winner(board, user_x_or_o)):
                    print("\nCongrats! You Won! \n")
                    terminate = True
                    break

        ### Last move: Computer's turn
            if (terminate == False):
                computer_move(board, computer_x_or_o, user_x_or_o)
                if (winner(board, computer_x_or_o)):
                    print("\nI Won! Try harder next time! \n")
                    terminate = True
                else:
                    ### Tie situation
                    print("\nTie! It was a good game! I'll beat you next time!!\n")
                    terminate = True

if __name__ == "__main__":
    ### Beginning the game by calling the following function
    play_a_new_game()

    ### Inviting the user for anther game
    another_game = input("Do you want to play again? Answer with [y/n]: ")
    while (another_game == 'y'):
        play_a_new_game()
        another_game = input("Do you want to play again? Answer with [y/n]: ")
