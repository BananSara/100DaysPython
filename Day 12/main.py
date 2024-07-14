print('welcome to the number guessing game!')

import random

easy_level_turn = 10
hard_level_turn = 5

def check_answer(guess,answer,turns):
    if guess > answer:
        print('too high')
        return turns - 1
    elif guess < answer:
        print('too low')
        return turns - 1
    else:
        print(f'currect! you got it! the answer was {answer}')

def set_difficulty():
    level = input('choose a difficulty: type "easy" or "hard": ')
    if level == 'easy':
        return easy_level_turn
    elif level == 'hard':
        return hard_level_turn
    else:
        print('incorrect input!')       

def game():
    print("I'm thinking of a number between 1 and 100 so guess that..")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f'you have {turns} attempts remaining to guess the answer')
        guess = int(input('make a guess: '))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('you lose! you have out of guesses')
            return
        elif guess != answer:
            print('guess again!')
    print(f'the currect answer is {answer}')
    

game()

