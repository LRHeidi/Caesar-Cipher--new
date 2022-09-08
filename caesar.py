"""
File: caesar.py
Name: Heidi
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    secret_num = int(input('Secret number : '))
    ciphered = input("What's the ciphered string? ")
    if ciphered.islower():
        ciphered = ciphered.upper()
    new_alpha= ALPHABET[len(ALPHABET)-secret_num:] + ALPHABET[:len(ALPHABET)-secret_num]
    deciphered = ''
    for i in (ciphered):
        a = new_alpha.find(i) # 房間號 序號
        if i.isalpha():
            deciphered += ALPHABET[a]
        else:
            deciphered += i


    print('The deciphered string is : ', deciphered )






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
