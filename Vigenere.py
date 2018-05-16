#two functions, one to encrypt using a Vigenère cipher, the other to decrypt.
#as well as a quick n dirty main function
#https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher to learn more about this sort of cipher

def vig_cipher(message, keyword):
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 '
    #ensure message only has alphanum and spaces
    message = ''.join(item for item in message if item in alphabet)
    
    #table contains (0-63),(1-63,0),(2-63,0,1), etc.
    row = [index for index in range(len(alphabet))]
    table = [row[x:] + row[:x] for x in range(len(alphabet))]
    
    #to encode, need full key
    if len(keyword) > len(message):
        #if key is longer than message, set key to first n letters of keyword
        full_key = keyword[:len(message)]
    elif len(keyword) == len(message):
        full_key = keyword
    else:
        full_fits = len(message) // len(keyword)
        remainder = len(message) % len(keyword)
        full_key = ''
        for index in range(full_fits + 1):
            full_key += keyword
        #add on extra
        full_key += keyword[:remainder]

    #Now, ready to encrypt message
    encrypted_message = ''
    current_index = 0
    for letter in message:
        letter_index = alphabet.find(letter)
        key_index = alphabet.find(full_key[current_index])
        #encrypted value for char n is at point (message_n,key_n)
        encrypted_letter = alphabet[table[letter_index][key_index]]
        encrypted_message += encrypted_letter
        current_index += 1

    return encrypted_message

def decrypt_vig(message, keyword):
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 '
    #ensure message only has alphanum and spaces
    message = ''.join(item for item in message if item in alphabet)
    
    row = [index for index in range(len(alphabet))]
    table = [row[x:] + row[:x] for x in range(len(alphabet))]

    #need full key to decode
    if len(keyword) > len(message):
        #if key is longer than message, set key to first n letters of keyword
        full_key = keyword[:len(message)]
    elif len(keyword) == len(message):
        full_key = keyword
    else:
        full_fits = len(message) // len(keyword)
        remainder = len(message) % len(keyword)
        full_key = ''
        for index in range(full_fits + 1):
            full_key += keyword
        #add on extra
        full_key += keyword[:remainder]

    decrypt_message = ''
    current_index = 0
    for letter in message:
        key_row_index = alphabet.find(full_key[current_index])
        key_row = table[key_row_index]
        letter_index = alphabet.find(letter)
        letter = ''
        for index in range(len(key_row)):
            if key_row[index] == letter_index:
                letter = alphabet[index]
                break
        decrypt_message += letter
        current_index += 1
    return decrypt_message

def main():
    #quick main function to encode a message
    message = input('Enter the message you wish to encode: ')
    key = input('Enter your keyword: ')
    encoded = vig_cipher(message, key)
    print('Your encoded message is: ' + encoded)
    return

if __name__ == '__main__':
    main()

