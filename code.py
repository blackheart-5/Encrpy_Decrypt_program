''' ###########################################################
#
#
#  Algorithm
#The user will enter a sentence, a string
#composed of letters, numbers, and punctuation. This string would be
#encrypted and decrypted using a combination of Affine and Caesar Cipher.
#Specifically, letters and numbers will be encrypted and decrypted using Affine Cipher;
#the punctuation using Caesar Cipher.
#
########################################################### '''

import string
import math

# Define constants for punctuation and alphanumeric characters
#  string.punctuation is a string constant that contains all the punctuation characters on the keyboard.
#  except space is not included in this string
PUNCTUATION = string.punctuation


#  string.ascii_lowercase is a string constant that contains all the lowercase letters in the alphabet.
#  string.digits is a string constant that contains all the digits 0-9.
ALPHA_NUM = string.ascii_lowercase + string.digits



BANNER = ''' Welcome to the world of 'dumbcrypt,' where cryptography meets comedy! 
    We're combining Affine Cipher with Caesar Cipher to create a code 
    so 'dumb,' it's brilliant. 
    Remember, in 'dumbcrypt,' spaces are as rare as a unicorn wearing a top hat! 
    Let's dive into this cryptographic comedy adventure!             
    '''


def print_banner(message):
    ''' Display the message as a banner.
    It formats the message inside a border of asterisks, creating the banner effect.'''
    border = '*' * 50
    print(border)
    print(f'* {message} *')
    print(border)
    print()
def multiplicative_inverse(A, M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.
        Args:
        A (int): The number for which the inverse is to be found.
        M (int): The modulo value.
        Returns:
            int: The multiplicative inverse of A modulo M.
    '''
    for x in range(M):
        if (A * x) % M == 1:
            return x
def check_co_prime(num, M):
    '''check the factors of each arguments
    use gcd to find the common factor is 1
    if the common factor is 1 return true other
    wise return false'''
    if math.gcd(num,M) == 1 :
        return True
    else:
        return False
def get_smallest_co_prime(M):
    '''Find all the factors of the arguments up to the argument
    from 2 up to the argument check if both both the argument and
    i are co-prime. return the first co-prime upon first iteration'''
    num = 0
    for i in range(2,(M+1)):
        if check_co_prime(i, M) == True:
            num += i
            return num



#
def caesar_cipher_encryption(ch, N, alphabet):
    '''use caesar for punctuation.
    find value of m
    find index value of character in alphabet
    Find the position E and convert the position to coded text
    return encryted character'''
    encrypt_text = ''
    M = len(alphabet)
    x = alphabet.find(ch)
    E = (x+N)%M
    encrypt_text += str(alphabet[E])
    return encrypt_text
def caesar_cipher_decryption(ch, N, alphabet):
    '''use caesar for punctuation.
    use caesar for punctuation.
    find value of m
    find index value of character in alphabet
    Find the position E and convert the position to Plain(actual) text
    return decoded character'''
    decrypt_text = ''
    M = len(alphabet)
    x = alphabet.find(ch)
    E = (x - N) % M
    decrypt_text += str(alphabet[E])
    return decrypt_text

#
def affine_cipher_encryption(ch, N, alphabet):
    '''use Affine for letters and numbers.
    find value of M
    find value of A
    find index value of character in alphabet
    Find the position E and convert the position to coded text
    return encrypted character'''
    encrypt_text = ''
    M = len(alphabet)
    A = (get_smallest_co_prime(M))
    x = alphabet.find(ch)
    E = ((A*x)+N)%M
    encrypt_text += str(alphabet[E])
    return encrypt_text
def affine_cipher_decryption(ch, N, alphabet):
    '''use Affine for letters and numbers.
    find value of M
    find value of A
    find index value of character in alphabet
    Find the position E and convert the position to coded text
    return decoded character'''
    decrypt_text = ''
    M = len(alphabet)
    A = (get_smallest_co_prime(M))
    A_inv = multiplicative_inverse(A,M)
    x = alphabet.find(ch)
    E = A_inv*(x - N) % M
    decrypt_text += str(alphabet[E])
    return decrypt_text


def main():
    '''main function to run the function
    print banner
    ask user rotation num n and loop if not integer
    ask command and check if its e or d or q
    loop under each command input
        ask string and print error and break if space in string
        loop each character
            if puctuation then use cipher and continue concatenation still loop ends
            elif letter or number then use alphine and continue concatenation still loop ends
        print output of plain and cipher text
    '''
    print_banner(BANNER)
    N = input('Input a rotation (int): ') #rotation input
    #ask N again again until right N is entered
    while N not in string.digits:
        print("\nError; rotation must be an integer.")
        N = input('Input a rotation (int): ')
    N = int(N)

    command = 'j' #assign initial command
    #ask command again again until right command is entered
    while command != 'q':
        command = input('\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ')
        while command not in 'edq':
            print("\nCommand not recognized.")
            command = input('\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ')

        if command == 'q':#quit program if true
            break
        else:
            if command == 'e':
                string_text = input(f'\nInput a string to encrypt: ')
            else:
                string_text = input(f'\nInput a string to decrypt: ')

            if ' ' in string_text:#catch spaces in string_text if true return to the top
                print("\nError with character:")
                print("Cannot encrypt this string.")
                continue
            #function Logic
            else:
                #if user wants to encrypt
                if command == 'e':
                    cipher_text = ''#empty string to store cipher text
                    for ch in string_text.lower(): #loop through each character of string and encrypt
                        if ch.isalnum():
                            alphabet = ALPHA_NUM
                            cipher_text += affine_cipher_encryption(ch, N, alphabet)
                        else:
                            alphabet = PUNCTUATION
                            cipher_text += caesar_cipher_encryption(ch, N, alphabet)

                    print("\nPlain text: {}".format(string_text))
                    print("\nCipher text: {}".format(cipher_text))

                #if user wants to encrypt
                elif command == 'd':
                    text = '' #empty string to store decoded plain text
                    for ch in string_text.lower():#loop through each character of string and decrypt
                        if ch.isalnum():
                            alphabet = ALPHA_NUM
                            text += affine_cipher_decryption(ch, N, alphabet)
                        else:
                            alphabet = PUNCTUATION
                            text += caesar_cipher_decryption(ch, N, alphabet)
                    print("\nCipher text: {}".format(string_text))
                    print("\nPlain text: {}".format(text))




if __name__ == '__main__':
    main()





