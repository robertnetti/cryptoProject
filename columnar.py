def key_assign(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_list = list(range(len(key)))

    #print all in list to check
    key_num = 0
    for row in range(len(alphabet)):
        for column in range(len(key)):
            if alphabet[row] == key[column]:
                key_num += 1
                key_list[column] = key_num
    return key_list

def numeric_pos(key, key_list):
    #gets numeric position of each letter
    pos = ""
    for row in range(len(key) + 1):
        for column in range(len(key)):
            if key_list[column] == row:
                pos += str(column)
    return pos



def columnar_encrypt(text, key):
    text = text.replace(" ", "").upper()
    key = key.upper()
    #assign list of keys
    key_list = key_assign(key)

    #print to check
    for index in range(len(key)):
        print(key[index], end=" ", flush=True)

    print()
    for index in range(len(key)):
        print(str(key_list[index]), end=" ", flush=True)
    print()
    print("-------------------------")

    #if all letters don't fit in grid properly
    extras = len(text) % len(key)
    fillers = len(key) - extras

    if extras != 0:
        for index in range(fillers):
            text += "|"

    rows = int(len(text) / len(key))

    #convert to grid
    grid = [[0] * len(key) for index in range(rows)]
    n = 0
    for row in range(rows):
        for column in range(len(key)):
            grid[row][column] = text[n]
            n += 1

    #print to check
    for row in range(rows):
        for column in range(len(key)):
            print(grid[row][column], end=" ", flush=True)
        print()

    #get number locations
    location = numeric_pos(key, key_list)
    print(location)

    # begin cipher
    encrypted = ""
    k = 0
    for i in range(rows):
        if k == len(key):
            break
        else:
            d = int(location[k])
        for j in range(rows):
            encrypted += grid[j][d]
        k += 1

    return encrypted

def columnar_decrypt(cipher, key):
    cipher = cipher.replace(" ", "").upper()
    # print(msg)
    key = key.upper()

    # assigning numbers to keywords
    kywrd_num_list = key_assign(key)

    num_of_rows = int(len(cipher) / len(key))

    # getting locations of numbers
    num_loc = numeric_pos(key, kywrd_num_list)

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # decipher
    decrypted = ""
    k = 0
    itr = 0

    # print(arr[6][4])
    # itr = len(msg)

    for i in range(len(cipher)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = cipher[itr]
            # print("j: {} d: {} m: {} l: {} ". format(j, d, msg[l], l))
            itr += 1
        if itr == len(cipher):
            break
        k += 1
    print()

    for i in range(num_of_rows):
        for j in range(len(key)):
            decrypted += str(arr[i][j])
        # for
    # for

    return decrypted

#Driver Code to test the above functions
def main():
    while True:
        choice = int(input("Enter 1 to Encrypt, 2 to Decrypt, 3 to Quit: "))
        if choice == 1:
            text = input("Enter text to encrypt: ")
            key = input("Enter keyword: ")
            enc_text = columnar_encrypt(text, key)
            print('Encrypted Text: {}'.format(enc_text))
        elif choice == 2:
            text = input("Enter text to decrypt: ")
            key = input("Enter keyword: ")
            dec_text = columnar_decrypt(text, key)
            print('Decrypted Text: {}'.format(dec_text))
        elif choice == 3:
            print("End Program")
            break

if __name__ == '__main__':
    main()