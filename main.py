def encrypt(string, key):

    ciphertext = ""

    for char in string:

        if char == ' ':
            ciphertext += char

        elif char.isupper():
            ciphertext += chr((ord(char) + key-65) % 26 + 65)

        else:
            ciphertext += chr((ord(char) + key-97) % 26 + 97)

    print(ciphertext)


def decrypt(string, key):

    plaintext = ""

    for char in string:

        if char == ' ':

            plaintext += char

        elif char.isupper():

            plaintext += chr(65 + (ord(char)-key-65) % 26)

        else:

            plaintext += chr((ord(char) - key - 97) % 26 + 97)

    print(plaintext)


encrypt('Axeeh phkew', 7)
decrypt("Hello world", 7)
