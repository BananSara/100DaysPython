alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt and type 'decode' to decrypt \n")
text = input('please type your message: \n')
shift = int(input('type the shift number: \n'))

# encrypt:
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    
    for letter in plain_text:
        position = alphabet.index(letter) 
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'the encoded text is: {cipher_text}')
    
# decrypt: 
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f'the decoded text is: {plain_text}')
    
    
if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
    

    
    
