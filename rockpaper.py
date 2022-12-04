from random import randint
t = ['rock','paper','scissors']
comp = t[randint(0,2)]
score =0
def game (player = False , score = 0) :
    while player == False:
        player = input("Choose one from: rock, paper, scissors\n")
        if player == comp:
            score = 0
            print('Tie! , No points !')
            
        elif player == 'rock':
            if comp == 'paper':
                score = 0
                print('You LOSE! Paper covers Rock.')
                
            else:
                score = 1
                print('You WIN! Scissors cut Paper.')
                
        elif player == 'paper':
            if comp == 'rock':
                score = 1
                print('You WIN! Paper covers Rock.')
            else:
                score = 0
                print('You LOSE! Rock destroys Scissors.')
        elif player == 'scissors':
            if comp == 'paper':
                score = 1
                print('You WIN! Scissors cut Paper.')
            else:
                score = 0
                print('You LOSE! Rock destroys Scissors.')
        else:
            print('The spelling seems to be incorrect. Kindly check the spelling once!')
        print('your score : ' + str(score))
game()

game()

game()

print ('Thankyou  for playing this game. ')

