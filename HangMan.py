import random

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

lives = 6
score = 0
word_list = ['ardvork','baboon','camel']
chosen_word = random.choice(word_list)
print(chosen_word)
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
                score += 1
            
    else:
        lives-= 1
        if lives == 0:
            print('You Lose')
            print(stages[6])
            break
        elif lives == 1:
            print(stages[0])
        elif lives == 2:
            print(stages[1])
        elif lives == 3:
            print(stages[2])
        elif lives == 4:
            print(stages[3])
        elif lives == 5:
            print(stages[4])
        elif lives == 6:
            print(stages[5])
        

print(display)

