board = [' ' for _ in range (0, 9)]

def print_board(board):
    top = board[0:3]
    middle = board[3:6]
    bottom = board[6:9]
    print(top)
    print(middle)
    print(bottom)

print_board(board)

playerturn = 0 # player O
stopgame = False
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

while stopgame == False:
    move = input('Which cell do you wanna occupy? (0-9)')
    if board[int(move)] == ' ':
        if playerturn == 0:
            board[int(move)] = 'O'
            playerturn = 1
        elif playerturn == 1:
            board[int(move)] = 'X'
            playerturn = 0
    else:
        print('this field is already taken')

    print_board(board)

    if decide_winner('O'):
        print('player O is the winner')
        stopgame = True
    elif decide_winner('X'):
        print('player X is the winner')
        stopgame = True
    elif not board[0] == ' ' and not board[1] == ' ' and not board[2] == ' ' and not board[3] == ' ' and not board[4] == ' ' and not board[5] == ' ' and not board[6] == ' ' and not board[7] == ' ' and not board[8] == ' ':
        print('it is a tie')
        stopgame = True
    
    print(round)
        


