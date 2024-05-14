import random
from hangman_words import word_list

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 7
score = 0
chosen_word = random.choice(word_list)

print(chosen_word) #FOR TESTING PURPOSE

display = []

for i in range(len(chosen_word)):
    display.append('_')

while '_' in display:
    user_input = input('Guess a letter: ')
    guess = user_input.lower()

    if guess in chosen_word:
        for i in range(0,len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess          
                    
            
    else:
        lives-= 1
        if lives == 0:
            print(stages[0])
            print('You Lose')
            break
        elif lives == 1:
            print(stages[1])
        elif lives == 2:
            print(stages[2])
        elif lives == 3:
            print(stages[3])
        elif lives == 4:
            print(stages[4])
        elif lives == 5:
            print(stages[5])
        elif lives == 6:
            print(stages[6])

print("you Win")
print(display)

