#!/usr/bin/env python
# coding: utf-8

# # Code1---- Game stops only when all the cells are filled(player vs player)

# In[ ]:


from IPython.display import clear_output
I=[' 'for i in range(0,9) ]
count=0
count2=0
score=0
count1=0
oc=[]
def display():            #function displays the board ,initially with no entries and later with all entries of both players.
    '''
    This function displays the board
    '''
    clear_output()
    print(I[0],'|',I[1],'|',I[2])
    print('-- --- --')
    print(I[3],'|',I[4],'|',I[5])
    print('-- --- --')
    print(I[6],'|',I[7],'|',I[8])
    print('\n')
while True:                #while loop takes the inputs from players and assigns x/o at the respective positions.
        for x in range (count,9):    #This for loop aks for input ,checks if it is valid and breaks if valid else asks for a valid input
            j=int(input('player-1  '))
            if (j not in oc and 0<=j<10):
                I[j-1]='x'                
                oc.append(j)
                display()        
                break
            else:
                print('invalid input,try again')
        count=count+1
        if count==9:            #when all the cells are filled loop is broke and game is over and it would be declared a tie. 
            print('game over')
            break    
        for x in range(count,9):    #This for loop aks for input ,checks if it is valid and breaks if valid else asks for a valid input
            k=int(input('player-2  '))
            if (k not in oc and 0<=k<10):
                I[k-1]='o'
                oc.append(k)
                display()
                break
            else:
                print('invalid input,try again')   
        count=count+1
        print(count)
        
    # below are the winning conditions and if any of them satisfy then the player who did it will be the winner. 
        
if (I[0]==I[1]==I[2]=='x' or I[3]==I[4]==I[5]=='x' or I[6]==I[7]==I[8]=='x' or I[0]==I[4]==I[8]=='x' or I[6]==I[4]==I[2]=='x'or I[0]==I[3]==I[6]=='x' or I[1]==I[4]==I[7]=='x' or I[2]==I[5]==I[8]=='x'):
    count1+=10     #Winning condition for player1 and if he wins 10 ponts are given
    
else:
    count1=0
if (I[0]==I[1]==I[2]=='o' or I[3]==I[4]==I[5]=='o' or I[6]==I[7]==I[8]=='o' or I[0]==I[4]==I[8]=='o' or I[6]==I[4]==I[2]=='o'or I[0]==I[3]==I[6]=='o' or I[1]==I[4]==I[7]=='o' or I[2]==I[5]==I[8]=='o'):
    score+=10      #Winning condition for player2 and if he wins 10 points are given
else:
    score=0
if count1==score: 
    count1=5
    score=5
    print('Its a tie')
elif count1>score:
    print('player1 won')
elif score>count1:
    print('player2 won')
print('player1 got ',count1,'points\nplayer2 got ',score,'points')  # this print statement displays scores of both the players at the end of the game.


# # Code2---player vs player (Game stops when any one of the player wins)

# In[ ]:




from IPython.display import clear_output
I=[' 'for i in range(0,9) ]
count=0
count2=0
score=0
count1=0
oc=[]
def display():      #This function displays the board,initially with no entries and later with  entries of both players. 
    '''
    This function displays the board
    '''
    clear_output()
    print(I[0],'|',I[1],'|',I[2])
    print('-- --- --')
    print(I[3],'|',I[4],'|',I[5])
    print('-- --- --')
    print(I[6],'|',I[7],'|',I[8])
    print('\n')
while True:   
        for x in range (0,9):
            j=int(input('player-1  '))
            if (j not in oc and 0<=j<10):
                I[j-1]='x'                
                oc.append(j)
                display()     
                if (I[0]==I[1]==I[2]=='x' or I[3]==I[4]==I[5]=='x' or I[6]==I[7]==I[8]=='x' or I[0]==I[4]==I[8]=='x' or I[6]==I[4]==I[2]=='x'or I[0]==I[3]==I[6]=='x' or I[1]==I[4]==I[7]=='x' or I[2]==I[5]==I[8]=='x'):
                    print('player1 won')  # above is the winning condition for player1 and if any one of them satisfies, this print statement is printed.  
                    count1=10
                    break
                break
            else:
                print('invalid input,try again')
        count=count+1
        if (count1==10 or count==9): #when player1 wins or all the cells are filled then the game ends.        
            print('game over')
            break    
        for count in range(0,9):
            k=int(input('player-2  '))
            if (k not in oc and 0<=k<10):
                I[k-1]='o'
                oc.append(k)
                display()
                if (I[0]==I[1]==I[2]=='o' or I[3]==I[4]==I[5]=='o' or I[6]==I[7]==I[8]=='o' or I[0]==I[4]==I[8]=='o' or I[6]==I[4]==I[2]=='o'or I[0]==I[3]==I[6]=='o' or I[1]==I[4]==I[7]=='o' or I[2]==I[5]==I[8]=='o'):
                    print('player2 won')   # above is the winning condition for player2 and if any one of them satisfies, this print statement is printed. 
                    score=10
                    break
                break
            else:
                print('invalid input,try again')   
        count=count+1
        if score==10:
            print('game over')
            break
if count1==score:
    print('its a tie' )
print('player1 got ',count1,'points\nplayer2 got ',score,'points')  # this print statement displays scores of both the players at the end of the game.


# # Code3--- player vs computer

# In[ ]:


####player vs computer
from IPython.display import clear_output
from random import randint
I=[' 'for i in range(0,9) ]
count=0
score=0
count1=0
oc=[]
def display():      #this function displays the board
    '''
    This function displays the board
    '''
    clear_output()
    print(I[0],'|',I[1],'|',I[2])
    print('-- --- --')
    print(I[3],'|',I[4],'|',I[5])
    print('-- --- --')
    print(I[6],'|',I[7],'|',I[8])
    print('\n')
while True:   
        for x in range (0,9):     #This for loop aks for input ,checks if it is valid and breaks if valid else asks for a valid input 
            j=int(input('player-1  '))
            if (j not in oc and 0<=j<10):
                I[j-1]='x'                
                oc.append(j)
                display()     
                if (I[0]==I[1]==I[2]=='x' or I[3]==I[4]==I[5]=='x' or I[6]==I[7]==I[8]=='x' or I[0]==I[4]==I[8]=='x' or I[6]==I[4]==I[2]=='x'or I[0]==I[3]==I[6]=='x' or I[1]==I[4]==I[7]=='x' or I[2]==I[5]==I[8]=='x'):
                    print('player1 won')  # above is the winning condition and if any one of them being satisfied,player wins.
                    count1=10
                    break
                break
            else:
                print('invalid input,try again')
        count=count+1
        if (count1==10 or count==9):        
            print('game over')
            break    
        for x in range(0,9):
            k=randint(0,9)    #computer selects a random cell which isnt selected by the player.
            if k not in oc :
                I[k-1]='o'
                oc.append(k)
                display()
                if (I[0]==I[1]==I[2]=='o' or I[3]==I[4]==I[5]=='o' or I[6]==I[7]==I[8]=='o' or I[0]==I[4]==I[8]=='o' or I[6]==I[4]==I[2]=='o'or I[0]==I[3]==I[6]=='o' or I[1]==I[4]==I[7]=='o' or I[2]==I[5]==I[8]=='o'):
                    print('player2 won')  # above is the winning condition and if any one of them satisfies computer wins.
                    score=10
                    break
                break  
        count=count+1
        print(count)
        if score==10:
            print('game over')
            break
if count1==score:
    print('Its a tie' )
print('player1 got ',count1,'points\nplayer2 got ',score,'points')  # this print statement displays scores of the player and computer at the end of the game.


# # Code4--- series play

# In[4]:




        from IPython.display import clear_output
        score=0
        count1=0
        s=0
        I=[' 'for i in range(0,9) ]
        count=0
        oc=[]
        C='yes'
        def display():   #This function displays the board
            '''
            This function displays the board
            '''
            clear_output()
            print(I[0],'|',I[1],'|',I[2])
            print('-- --- --')
            print(I[3],'|',I[4],'|',I[5])
            print('-- --- --')
            print(I[6],'|',I[7],'|',I[8])
            print('\n')    
while C!='exit':  #this while loop helps in repeating the game
    while True:   #this while loop executes the game
                s=0            
                if C=='yes':
                    I=[' 'for i in range(0,9) ]
                    oc=[]
                    C='exit'
                    count=0
                for x in range (0,9):   #This for loop aks for input ,checks if it is valid and breaks if valid else asks for a valid input and also checks for winning condition
                    j=input('player-1  ')
                    if (j not in oc and 0<=int(j)<10):
                        I[int(j)-1]='x'                
                        oc.append(j)
                        display()     
                        if (I[0]==I[1]==I[2]=='x' or I[3]==I[4]==I[5]=='x' or I[6]==I[7]==I[8]=='x' or I[0]==I[4]==I[8]=='x' or I[6]==I[4]==I[2]=='x'or I[0]==I[3]==I[6]=='x' or I[1]==I[4]==I[7]=='x' or I[2]==I[5]==I[8]=='x'):
                            print('player1 won')
                            count1=count1+10
                            s='stop'
                        break
                    else:
                        print('invalid input,try again')
                count=count+1
                if s=='stop':        
                    print('game over')
                    break
                if count==9:
                    print('its a tie')
                    count1=count1+5
                    score=score+5
                    break
                for x in range(0,9):  #This for loop aks for input ,checks if it is valid and breaks if valid else asks for a valid input and also checks for winning condition
                    k=input('player-2  ')
                    if (k not in oc and 0<=int(k)<10 ):
                        I[int(k)-1]='o'
                        oc.append(k)
                        display()
                        if (I[0]==I[1]==I[2]=='o' or I[3]==I[4]==I[5]=='o' or I[6]==I[7]==I[8]=='o' or I[0]==I[4]==I[8]=='o' or I[6]==I[4]==I[2]=='o'or I[0]==I[3]==I[6]=='o' or I[1]==I[4]==I[7]=='o' or I[2]==I[5]==I[8]=='o'):
                            print('player2 won')
                            score=score+10
                            s='stop'
                        break
                    else:
                        print('invalid input,try again')   
                count=count+1
                if s=='stop':
                    print('game over')
                    break                    
    print('player1 got ',count1,'points\nplayer2 got ',score,'points')  # this print statement displays cumulative scores of both the players at the end of the each game.          
    C=input('Would you like to continue playing (yes or exit)   ').lower() 
    
        

