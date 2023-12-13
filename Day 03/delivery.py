print('welcome to python pizza deliveries!')
bill = 0

size = input('what size pizza do you want? S, M L ?')
pepperoni = input('do yo want pepperoni?Y or N?')
extra_cheese = input('do you want extra cheese? Y or N?')

if size == 's':
    bill += 15

elif size == 'm':
    bill += 20

else:
    bill += 25

if pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f"your final bill for your pizza is ${bill}")
