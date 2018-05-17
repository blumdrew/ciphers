#A program by me, which will be a cipher

def encode(message, key):
    #something like a vinegere cipher, but instead of repeating key, add n
    #character index to each repetion of key word
    ascii_chars = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '''

    #need to exclude all non-ascii chars from the message
    message = ''.join(char for char in message if char in ascii_chars)

    row = [index for index in range(len(ascii_chars))]
    #table is same as from vigenere cipher: rows ((0-n),(1-n,0),(2-n,0,1)..)
    table = [row[x:] + row[:x] for x in range(len(ascii_chars))]

    #create full key - this part is different
    if len(key) >= len(message):
        full_key = key[:len(message)]
    else:
        full_fits = len(message) // len(key)
        full_key = ''
        key_list = [key[x] for x in range(len(key))]
        for index in range(full_fits):
            new_key = ''
            for item in key_list:
                #shifts the key over n chars
                key_item_index = ascii_chars.find(item) + index
                new_key += ascii_chars[key_item_index]
            #add on key to total key
            full_key += new_key
        extra = len(message) % len(key)
        full_key += key[:extra]
        
    #encrypt message with new key
    encrypted = ''
    current_index = 0
    for letter in message:
        letter_index = ascii_chars.find(letter)
        key_index = ascii_chars.find(full_key[current_index])
        encrypted += ascii_chars[table[letter_index][key_index]]
        current_index += 1

    #Now, convert the ascii char to hex value use format(ord('char'), 'x')
    hex_encrypt = ''.join(format(ord(char), 'x') for char in encrypted)
    #final output seperates the long string of chars into groups of 8 chars (4hex vals)
    final_out = ' '.join(hex_encrypt[i:i+8] for i in range(0, len(hex_encrypt), 8))

    return final_out

def decode(message, key):
    #same deal as the encode segment
    ascii_chars = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '''
    message = ''.join(char for char in message if char in ascii_chars)

    row = [index for index in range(len(ascii_chars))]
    table = [row[x:] + row[:x] for x in range(len(ascii_chars))]
    
    #decode from hex
    message = bytearray.fromhex(message).decode()

    #now, decode the twisted vig, generate key same way as in encoder
    if len(key) >= len(message):
        full_key = key[:len(message)]
    else:
        full_fits = len(message) // len(key)
        full_key = ''
        key_list = [key[x] for x in range(len(key))]
        for index in range(full_fits):
            new_key = ''
            for item in key_list:
                #shifts the key over n chars
                key_item_index = ascii_chars.find(item) + index
                new_key += ascii_chars[key_item_index]
            #add on key to total key
            full_key += new_key
        extra = len(message) % len(key)
        full_key += key[:extra]

    translated = ''
    current_index = 0
    #this is same idea as in the vigenere cipher. you find the row of the key, see which letter
    #or char corresponds to which
    for item in range(len(message)):
        key_row_index = ascii_chars.find(full_key[item])
        key_row = table[key_row_index]
        letter_index = ascii_chars.find(message[item])
        letter = ''
        for index in range(len(key_row)):
            if key_row[index] == letter_index:
                letter = ascii_chars[index]
                break
        translated += letter
        current_index += 1

    return translated
    
