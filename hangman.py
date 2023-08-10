#Just a random code to kill time

import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = ['cat', 'milk', 'dyson']

guess = [i for i in random.choice(words)]
answer = []
for i in guess:
    guess[guess.index(i)] = '_'
    answer.append(i)

print(f"The word is {' '.join(guess)}")

ongoing_pic = 0

while ongoing_pic != len(HANGMAN_PICS):
    letter = input("What is the letter?\n")
    if letter in answer:
        guess[answer.index(letter)] = letter
        print(f"That's right! The word is {' '.join(guess)}")
        if '_' not in guess:
            print("Congratulation! You won!! :)")
            break
    else:
        print("Incorrect")
        print(HANGMAN_PICS[ongoing_pic])
        ongoing_pic += 1

if '_' not in guess:
    print('Would you like to try again?')
else:
    print("Boooooo. You lost. Try again")
    
