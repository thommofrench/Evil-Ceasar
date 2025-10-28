a = input('Message: ')
b = input('Key: ')

e = [''] * len(a)
d = e

cipher_naughty_word = 0
cipher_other_naughty_word = 0



# get a the key
for key in range(len(b)):
    jawn = ord(b[key])
    cipher_naughty_word += jawn

# encode the jawn
for enc in range(len(a)):
    e[enc] = chr(ord(a[enc]) + cipher_naughty_word)

print('Encoded Message: ' + ''.join(e))

c = input('Key the Jawn: ')
# get a the key
for key2 in range(len(c)):
    jawn2 = ord(c[key2])
    cipher_other_naughty_word += jawn2

# decode the jawn
for dec in range(len(e)):
    d[dec] = chr(ord(e[dec]) - cipher_other_naughty_word)


print('Decoded Message: ' + ''.join(d))