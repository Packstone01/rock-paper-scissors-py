import random

num = random.randrange(1,4)
compChoice = ''

if num == 1:
  compChoice = 'rock'
elif num == 2:
  compChoice = 'paper'
else:
  compChoice = 'scissors'

choice = input('What do you choose? Rock, Paper or Scissors? ')
choice = choice.lower()
print(f'\nComputer chose {compChoice}.')
print(f'You chose {choice}.\n')

if choice == compChoice:
  print(f'Tie game! You both chose {choice}.')
elif choice == 'rock' and compChoice == 'paper':
  print('The computer won! They chose paper.')
elif choice == 'rock' and compChoice == 'scissors':
  print('You won! The computer chose scissors.')
elif choice == 'paper' and compChoice == 'rock':
  print('You won! The computer chose rock.')
elif choice == 'paper' and compChoice == 'scissors':
  print('The computer won! They chose scissors!')
elif choice == 'scissors' and compChoice == 'rock':
  print('The computer won! The computer chose rock.')
elif choice == 'scissors' and compChoice == 'paper':
  print('You won! The computer chose paper.')
