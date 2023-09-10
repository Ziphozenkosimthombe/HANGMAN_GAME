import random
import hang_man
import words

lives = 6

chosen_letter = random.choice(words.words) # choosing the random word for a user

display = []
for i in range(len(chosen_letter)):
    display += '_'
print(display)

endOfTheGame = False
while not endOfTheGame:
    guess_letter = input('GUESS THE LETTER:  ')
    for position in range(len(chosen_letter)):
        letter = chosen_letter[position]
        if letter == guess_letter:
            display[position] = guess_letter
    print(display)
    if guess_letter not in chosen_letter:
        lives -= 1
        if lives == 0:
            endOfTheGame = True
            print('you lose!!!')
    if '_' not in display:
        endOfTheGame = True
        print('you win')
    print(hang_man.stages[lives])
print('the correct word is {}'.format(chosen_letter))