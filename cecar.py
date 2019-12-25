alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя1234567890'
encrypt = input('Enter your message: ')
key = 3
encrypt = encrypt.lower()
encrypted = ''
for letter in encrypt:
    position = alphabet.find(letter)
    newposition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newposition]
    else:
        encrypted = encrypted + letter
print('Your chipher is: ', encrypted)

   




