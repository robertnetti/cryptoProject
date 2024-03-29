import string
import random


def generate_key():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)


def sub_encrypt(key, plaintext):
    # make plaintext lowercase
    plaintext = plaintext.lower()

    # list containing all characters
    letters = string.ascii_lowercase

    # dictionary for encryption alphabet
    dict = {}

    # build the dictionary with the given key
    for i in range(len(letters)):
        dict[letters[i]] = key[i]

    # generate ciphertext
    cipher_text = []
    for char in plaintext:
        if char in letters:
            temp = dict[char]
            cipher_text.append(temp)
        else:
            temp = char
            cipher_text.append(temp)

    cipher_text = "".join(cipher_text)
    return cipher_text


def sub_decrypt(key, ciphertext):
    # make ciphertext lowercase
    ciphertext = ciphertext.lower()

    # list containing all characters
    letters = string.ascii_lowercase

    # build the dictionary with the given key
    dict = {}
    for i in range(len(key)):
        dict[key[i]] = letters[i]

    # recover plaintext
    decrypt_text = []
    for char in ciphertext:
        if char in letters:
            temp = dict[char]
            decrypt_text.append(temp)
        else:
            temp = char
            decrypt_text.append(temp)

    decrypt_txt = "".join(decrypt_text)
    return decrypt_txt


def main():
    key = generate_key()
    while True:
        try:
            choice = int(input("Enter 1 to Encrypt, 2 to Decrypt, 3 to Quit: "))
            if choice < 1 or choice > 3:
                print("Invalid Input, Please Try Again")
        except ValueError:
            print("Invalid Input, Please Try Again")
            continue
        if choice == 1:
            key = generate_key()
            plaintext = input("Enter Message to be Encrypted: ")
            ciphertext = sub_encrypt(key, plaintext)
            print("Key: " + key)
            print("Ciphertext: " + ciphertext)
        elif choice == 2:
            key = input("Enter Key: ")
            ciphertext = input("Enter Message to be Decrypted: ")
            plaintext = sub_decrypt(key, ciphertext)
            print("Plaintext: " + plaintext)
        elif choice == 3:
            print("End Program")
            break


if __name__ == '__main__':
    main()