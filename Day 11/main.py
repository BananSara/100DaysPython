
#A game with cards, the goal of the game is to add up your cards to the largest number without going over 21. so if the cards in your hand add up more than 21, then it's called a bust and means that you lose the game.
#In this game, Jack, Queen and king each count as 10 and Ace can either count as a one towards your total or it can count as an 11.

import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)== 21 and len(cards) == 2:
        return 0 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score >21 and computer_score > 21:
        return 'you went over. You Lose!'
    elif user_score == computer_score:
        return 'Draw'
    elif user_score > 21:
        return 'you went over. You Lose!'
    elif computer_score > 21:
        return 'opponent went over.You Win!'
    elif user_score > computer_score:
        return 'You Win!'
    elif user_score == 0:
        return 'win with a blackjack'
    elif computer_score == 0:
        return 'Lose, opponent has blackjack'
    else:
        return 'You Lose!'
    

def play_game():
    user_card = []
    computer_card = []
    is_game_over = False
    
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    
    
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f' your cards: {user_card}, current score: {user_score}')
        print(f"computer's first card: {computer_card[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input('Type "y" to get another card, type "n" to pass: ')
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
                
    
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
        
    print(f'your final hand: {user_card}, final score: {user_score}')
    
    print(f"computer's final hand: {computer_card}, final score: {computer_score}") 
    print(compare(user_score, computer_score))
    
game_question = input('do you want to play a game of blackjack? type "y" or "n": ')
while game_question == 'y':
    play_game()
    