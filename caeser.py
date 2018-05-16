#Caeser cipher
#A simple program that can encode or decode using a caeser cipher
#Caeser ciphers are pretty simple, for more information see https://en.wikipedia.org/wiki/Caesar_cipher

import random

def caeser_encode(message, key):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 '
    message = ''.join(item for item in message if item in chars)
    encoded = ''
    for item in message:
        reg_index = chars.find(item)
        enc_index = (reg_index + key) % len(chars)

        encoded += chars[enc_index]

    return encoded

def caeser_decode(message, key):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 '
    message = ''.join(item for item in message if item in chars)
    decoded = ''
    for item in message:
        reg_index = chars.find(item)
        enc_index = (reg_index - key) % len(chars)

        decoded += chars[enc_index]

    return decoded

def main():
    #simple main function to encode with a random key
    key = int(63 * random.random())
    message = input('Enter the message you wish to encode: ')
    out = caeser_encode(message, key)
    print('Your encoded message is: ' + out)
    print('Key used: ' + str(key))
    return

if __name__ == '__main__':
    main()
