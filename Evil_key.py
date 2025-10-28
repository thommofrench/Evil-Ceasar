def key(key_phrase):
    cipher_naughty_word = 0
    # get a the key
    for key in range(len(key_phrase)):
        jawn = ord(key_phrase[key])
        cipher_naughty_word += jawn
    return cipher_naughty_word