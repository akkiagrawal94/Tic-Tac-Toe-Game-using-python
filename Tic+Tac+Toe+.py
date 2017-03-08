
# coding: utf-8

# In[1]:

from IPython.display import clear_output
def board_display(board):#function to display the board
    clear_output()
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')


# In[2]:

def player_input():#function to take input 
    marker=' '
    while not (marker=='O' or marker=='X'):
        marker=input('Player1:do you want x or o').upper()
    if(marker=='X'):
        return('X','O')#returning tuple
    else:
        return('O','X')
        


# In[3]:

def place_marker(board,marker,position):#palce the option in board
    board[position]=marker


# In[4]:

def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark)or
            (board[7]==mark and board[8]==mark and board[9]==mark)or
             (board[1]==mark and board[4]==mark and board[7]==mark)or
            (board[2]==mark and board[5]==mark and board[8]==mark)or
            (board[3]==mark and board[6]==mark and board[9]==mark)or
            (board[1]==mark and board[5]==mark and board[9]==mark)or
             (board[3]==mark and board[5]==mark and board[7]==mark))


# In[5]:

import random
def choose_first():#randomly chooses player
    if random.randint(0,1)==0:
        return 'Player1'
    else:
        return 'Player2'
    


# In[6]:

def space_check(board,position):#to check if space is available or not
    return board[position]==' '


# In[7]:

def full_board_check(board):#To check board is full or not
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[30]:


def replay():#to paly again
    return input("Do you want to play again:Yes or no").startswith('y')


# In[31]:

def player_choice(board):#to enter the choice of player
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position=input("Choose your next position:(1-9)")
    return (int(position))


# In[32]:

print("Welcome to Tic Tac Toe")#main function
while True:
    theboard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+"will go first")
    game_on = True
    while game_on:
        if turn=='Player1':
            board_display(theboard)
            position=player_choice(theboard) 
            place_marker(theboard,player1_marker,position)
            if win_check(theboard,player1_marker):
                board_display(theboard)
                print("Congrats Player 1")
                game_on = False
            else:
                if full_board_check(theboard):
                    board_display(theboard)
                    print("Game is draw")
                    break
                else:
                    turn ="Player2"
        else:
            board_display(theboard)
            position=player_choice(theboard) 
            place_marker(theboard,player2_marker,position)
            if win_check(theboard,player2_marker):
                board_display(theboard)
                print("Congrats Player 2")
                game_on = False
            else:
                if full_board_check(theboard):
                    board_display(theboard)
                    print("Game is draw")
                    break
                else:
                    turn ="Player1"
    if not replay():
        break
        

