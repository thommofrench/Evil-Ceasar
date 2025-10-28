import Evil_key
import Evil_Encode

x = input('Would you like to evil encode or decode a message? (e/d): ')
b = input('Key: ')

# get a the key
evil_key = Evil_key.key(b)
evil_message = Evil_Encode.encode(evil_key, x)

print('Evil Message: ' + ''.join(evil_message))
