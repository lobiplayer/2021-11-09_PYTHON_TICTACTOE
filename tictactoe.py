board = [' ' for _ in range (0, 9)] #create 9 emty strings.

def print_board(board): #print the board so that there are three rows.
    top = board[0:3]
    middle = board[3:6]
    bottom = board[6:9]
    print(top)
    print(middle)
    print(bottom)

print_board(board)

playerturn = 0 # 0 = player O 1 = player X
stopgame = False #needed for the while loop on line 33
def decide_winner(y):
    if board[0] == y and board[1] == y and board[2] == y:
        return True
    elif board[3] == y and board[4] == y and board[5] == y:
        return True
    elif board[6] == y and board[7] == y and board[8] == y:
        return True
    elif board[0] == y and board[3] == y and board[6] == y:
        return True
    elif board[1] == y and board[4] == y and board[7] == y:
        return True
    elif board[2] == y and board[5] == y and board[8] == y:
        return True
    elif board[0] == y and board[4] == y and board[8] == y:
        return True
    elif board[2] == y and board[4] == y and board[6] == y:
        return True

while stopgame == False: #game is on till there is a winner or a tie
    move = input('Which cell do you wanna occupy? (0-9)') #get the user input
    if int(move) >= 0 and int(move) < 9: #checks if the input is between 0 and 9
        if board[int(move)] == ' ': #is this tile free?
            if playerturn == 0: #Who's the player?
                board[int(move)] = 'O' #place the O
                playerturn = 1 #give turn to other player
            elif playerturn == 1:
                board[int(move)] = 'X'
                playerturn = 0
        else:
            print('this field is already taken')
    else:
        print('Invalid input. please pick a number from 0 to 9 (9 not included)')

    print_board(board) #shows the board with the changes of this move.

    if decide_winner('O'): #checks all the possible winning lines
        print('player O is the winner')
        stopgame = True #makes the while loop stop
    elif decide_winner('X'):
        print('player X is the winner')
        stopgame = True
        #So at this point there is no winner. Let's check if all the tiles are taken. If so, it's a tie: stop the while loop.
    elif not board[0] == ' ' and not board[1] == ' ' and not board[2] == ' ' and not board[3] == ' ' and not board[4] == ' ' and not board[5] == ' ' and not board[6] == ' ' and not board[7] == ' ' and not board[8] == ' ':
        print('it is a tie')
        stopgame = True
    
    print(round)
        


