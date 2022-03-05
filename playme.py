import random
import sys
guess = input('Guess what number between 0 - 10 I\'m thinking. You get 5 tries go: ')
wrongAns = ['You may try again, but it looks hopeless','Odds are never in your favour. Try again.','Wrong','Almost there! Or are you?','Not even close!']
righAns = 'Wow, yaarrr a winner Harrry! Such winning, I take the L.'
maxRound = 5
round = 0

def main ():
    while round < maxRound:
         num = random.randint(0,10)
         randAns = secrets.choise(wrongAns)
         round += 1
         if guess == num:
             print(rightAns)
             break
         elif guess != num:
             print(randAns + '/n')
             guess = input('Round ' + round + '. Go: ')
             continue
         if round == maxRound:
             print('Thanks for playing.')
             playAgain = input('Play again type 1. Exit type 0: ')
                 if playAgain == 1:
                     round = 0
                 else:
                     sys.exit('bye bye')

main()

