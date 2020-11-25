import string


def sub_encrypt(key, plain_text):
    # list containing all characters
    letters = string.ascii_letters

    # dictionary for encryption alphabet
    dict = {}

    # build the dictionary with the given key
    for i in range(len(letters)):
        dict[letters[i]] = letters[(i + key) % len(letters)]

    # generate ciphertext
    cipher_text = []
    for char in plain_text:
        if char in letters:
            temp = dict[char]
            cipher_text.append(temp)
        else:
            temp = char
            cipher_text.append(temp)

    cipher_text = "".join(cipher_text)
    return cipher_text


def sub_decrypt(key, cipher_text):
    # list containing all characters
    letters = string.ascii_letters

    # build the dictionary with the given key
    dict = {}
    for i in range(len(letters)):
        dict[letters[i]] = letters[(i - key) % (len(letters))]

    # recover plaintext
    decrypt_text = []
    for char in cipher_text:
        if char in letters:
            temp = dict[char]
            decrypt_text.append(temp)
        else:
            temp = char
            decrypt_text.append(temp)

    decrypt_txt = "".join(decrypt_text)
    return decrypt_txt


def main():

    while True:
        try:
            choice = int(input("Enter 1 to Encrypt, 2 to Decrypt, 3 to Quit: "))
            if choice < 1 or choice > 3:
                print("Invalid Input, Please Try Again")
        except ValueError:
            print("Invalid Input, Please Try Again")
            continue

        if choice == 1:
            key = int(input("Enter Key for Encryption:"))
            plain_text = input("Enter Plaintext for Encryption:")
            cipher_text = sub_encrypt(key, plain_text)
            print("Encrypted Message: " + cipher_text)
        elif choice == 2:
            key = int(input("Enter Key for Decryption:"))
            cipher_text = input("Enter Plaintext for Decryption:")
            decrypt_text = sub_decrypt(key, cipher_text)
            print("Decrypted Message: " + decrypt_text)
        elif choice == 3:
            print("End Program")
            break


if __name__ == '__main__':
    main()