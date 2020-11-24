def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def rsaencrypt(e, N, plaintext):
    cipher = ""

    for c in plaintext:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher

def rsadecrypt(d, N, ciphertext):
    plaintext = ""

    parts = ciphertext.split()
    for part in parts:
        if part:
            c = int(part)
            plaintext += chr(pow(c, d, N))

    return plaintext

# Driver Code to test the above functions
def main():
    while True:
        choice = int(input("Enter 1 to Encrypt, 2 to Decrypt, 3 to Quit: "))
        if choice == 1:
            plaintext = input("Enter the text to be encrypted: ")
            e = int(input("Enter e for rsa encryption: "))
            N = int(input("Enter N for rsa encryption: "))
            enc = rsaencrypt(e, N, plaintext)
            print("Ciphertext: ", enc)
        elif choice == 2:
            ciphertext = input("Enter the text to be decrypted: ")
            e = int(input("Enter e for rsa decryption: "))
            p = int(input("Enter p of N for rsa decryption: "))
            q = int(input("Enter q of N for rsa decryption: "))
            phiN = (p-1)*(q-1)
            N = p*q
            d = modinv(e, phiN)
            #print for  testing
            print("d: ", d)
            print("N: ", N)
            print("phi(N): ", phiN)
            dec = rsadecrypt(d, N, ciphertext)
            print("Plaintext: ", dec)
        elif choice == 3:
            print("End Program")
            break

if __name__ == '__main__':
    main()
