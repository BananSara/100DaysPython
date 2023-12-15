import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']


nr_letters = int(input('how many letters would you like in your password? \n'))
nr_numbers = int(input('how many numbers would you like in your password? \n'))
nr_symbols = int(input('how many symbols would you like in your password? \n'))


# easy level with order
password = ''
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
print(f'your password: {password}\n')


# hard level random
password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
random.shuffle(password_list)
print(password_list)
password = ''
for char in password_list:
    password += char
print(f'your password is: {password}')