import string
import random

login = 'your login'
password = 'your password'


def get_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
