import random

gamer_choice = int(
    input('what do you choose? type 0 for rock, 1 for paper and 2 for scissors \n'))

pc_choice = int(random.randint(0, 2))
print(f'computer chose: {pc_choice}')

if gamer_choice >= 3 or pc_choice < 0:
    print('invalid number!you lose...')

elif gamer_choice == 0 and pc_choice == 2:
    print('you win!')

elif pc_choice == 0 and gamer_choice == 2:
    print('you lose!')

elif pc_choice > gamer_choice:
    print('computer wins,you lose!')

elif gamer_choice > pc_choice:
    print('you win!')

elif pc_choice == gamer_choice:
    print('both same score')
