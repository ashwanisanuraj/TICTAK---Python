#creating the table
import time
import sys

board=['-','-','-','-','-','-','-','-','-']

def display():
    print('-------')
    print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
    print('-------')
    print('|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('-------')
    print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|')
    print('-------')

def check(board):
    p1='x'
    p2='o'

    #horizontal
    if board[0] == board[1] == board[2] == p1 or board[0] == board[1] == board[2] == p2:
        return True
    elif board[3] == board[4] == board[5] == p1 or board[3] == board[4] == board[5] == p2:
        return True
    elif board[6] == board[7] == board[8] == p1 or board[6] == board[7] == board[8] == p2:
        return True

    #verticle
    elif board[0] == board[3] == board[6] == p1 or board[0] == board[3] == board[6] == p2:
        return True
    elif board[1] == board[4] == board[7] == p1 or board[1] == board[4] == board[7] == p2:
        return True
    elif board[2] == board[5] == board[8] == p1 or board[2] == board[5] == board[8] == p2:
        return True

    #digonale
    elif board[0] == board[4] == board[8] == p1 or board[0] == board[4] == board[8] == p2:
        return True
    elif board[2] == board[4] == board[6] == p1 or board[2] == board[4] == board[6] == p2:
        return True

    else:
        return False

# def inp(board):
#     x = int(input("Enter the position: "))
#     # return x
#     if board [x-1]!='-':
#         print('INVALID POSITION,\nEnter Again!!')
#         return inp(board)
#     else:
#         return x

def animate():
        sys.stdout.write('.')
        time.sleep(0.8)
        sys.stdout.write('.')
        time.sleep(0.8)
        sys.stdout.write('.')
        time.sleep(0.8)

def gameover():
    sys.stdout.write('G')
    time.sleep(0.3)
    sys.stdout.write('A')
    time.sleep(0.3)
    sys.stdout.write('M')
    time.sleep(0.3)
    sys.stdout.write('E')
    time.sleep(0.25)
    sys.stdout.write(' ')
    time.sleep(0.25)
    sys.stdout.write('O')
    time.sleep(0.3)
    sys.stdout.write('V')
    time.sleep(0.3)
    sys.stdout.write('E')
    time.sleep(0.3)
    sys.stdout.write('R')

player1 = input('Enter Name of Player 1: ')
player2 = input('Enter Name of Player 2: ')
display()

for i in range(9):
    if i%2 == 0:
        # x = inp(board)
        x = int(input(str(player1)+', its your turn: '))
        board[x-1] = 'x'
        display()
        print(str(player1)+' pressed '+ str(x))
        if check(board):
            animate()
            print('\n'+str(player1)+' Wins🎉')
            break
        
    else:
        # x = inp(board)
        x = int(input(str(player2)+', its your turn: '))
        board[x-1] = 'o'
        display()
        print(str(player2)+' pressed '+ str(x))
        if check(board):
            animate()
            print('\n'+str(player2)+' Wins🎉')
            break

gameover()     

