import random
import sys

# define constant parameters
stopGame = 69 # this stops the program from running
lowBound = 0 # range low of the guess
upBound = 10 # range high of the guess

# let's give the bot some lines to say if the player is right or wrong
wrongAns = ['Looks hopeless.','Odds are never in your favour.','Wrong.','Almost there! Or are you?','Not even close!']
rightAns = 'Wow, yaarrr a winner Harrry! You got it! Such winning!'

# introduce the game to the player and get the first guess from the player 
def getInput():
    while True:
        try:
            guess = int(input(f'Welcome anon. Guess what number I\'m thinking right now between {lowBound} - {upBound}. Exit with {stopGame}: '))
            break
        except ValueError:
            print("Integers only please: ")
    return(guess)   
# if the player guesses wrong, then let them try again         
def tryAgain():
    while True:
        try: 
            guess = int(input('Try again: '))  
            break
        except ValueError:
            print("Integers only please!")  
    return(guess) 
    
def main ():
    guess = getInput()
    while True:
        num = random.randint(0,10) # computers guess
        randAns = random.choice(wrongAns).strip() #get random line to say when player is wrong
        if guess == stopGame:
            sys.exit('Thanks for playing hun!')  # exit system if user gives stopGame input          
        if guess == num:  
            print(rightAns) # user is guessed right. Congratulate them
            break
        if guess != num and guess != stopGame and guess >= lowBound and guess <= upBound:
            print(randAns) #player guessed wrong. Get random line to make fun of them
        else:
            print(f'Please, give an integer between {lowBound}-{upBound}.')  #player gave wrong input
        guess = tryAgain()   # run the tryAgain function to give the player another try if they are wrong
      
main()