import random
from collections import Counter

countries = '''India China Pakistan Paris Belgium Japan Malaysia Singapore Thailand  '''

countries = countries.split(' ')
each_country = random.choice(countries)

if __name__ == '__main__':
    for one_country in each_country:
        print('_', end = ' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(each_country) + 2
    correct = 0

    try:
        while (chances != 0):
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue


            # If letter is guessed correcly
            if guess in each_country:
                letterGuessed += guess

            # Print the each_country
            for char in each_country:
                if char in letterGuessed:
                    print(char, end = ' ')
                    correct += 1
                else:
                    print('_', end = ' ')

            # If user has guessed all the letters
            if (Counter(letterGuessed) == Counter(each_country)):
                print()
                print('Congratulations, You won!')
                break

        # If user has used all of his chances
        if chances == 0:
            print()
            print('You lost! Try again..')
            print('The each_country was {}'.format(each_country))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

        # print(letterGuessed)