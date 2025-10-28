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