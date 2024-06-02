import random

words = ['apple','green','love','computer','programming']
lives = 5

chosen_word = random.choice(words)
len_chosen_word = len(chosen_word)
print(f'the word has {len_chosen_word} letter')

#create blanks:
display = []
for i in range(len_chosen_word):
    display += '_'
print(display)

end_of_game = False
while end_of_game == False:
    guess = input('Guess a letter: ')
    
    for position in range(len_chosen_word):
        letter = chosen_word[position]
    
        if letter == guess:
            display[position] = letter
            
        
    if guess not in chosen_word:
        lives -= 1
        print('you lose one of your lives! no mach')
            
        if lives == 0:
            print('you lose!')
            end_of_game = True
            
                
    if '_' not in display:
        end_of_game = True
        print('you win!')
        
            
    print(display)