import string
import random

login = 'your email'
password = 'your password'


def get_random_word(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def get_random_number(low, high):
    return random.randint(low, high)


def count_of_letters(message):
    k = 0
    for i in message:
        if i in string.ascii_lowercase:
            k += 1
    return k


def count_of_numbers(message):
    k = 0
    for i in message:
        if i in string.digits:
            k += 1
    return k
