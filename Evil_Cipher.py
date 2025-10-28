def key(key_phrase):
    cipher_naughty_word = 0
    # get a the key
    for key in range(len(b)):
        jawn = ord(b[key])
        cipher_naughty_word += jawn
    return cipher_naughty_word

def encode(key, encode):
    message = input('Message: ')
    encoded = [''] * len(message)
    if encode == 'e':
        encode = 1
    elif encode == 'd':
        encode = -1
    else:
        print('Invalid option selected. Exiting...')
        exit()
    # encode the jawn
    for enc in range(len(message)):
        encoded[enc] = chr(ord(message[enc]) + encode*key)
    return encoded

x = input('Would you like to evil encode or decode a message? (e/d): ')
b = input('Key: ')

# get a the key
evil_key = key(b)
evil_message = encode(evil_key, x)

print('Evil Message: ' + ''.join(evil_message))
