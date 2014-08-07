from .common import shift_string, crack_sort
import string

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(ciphertext, key):
    if type(key) == str:
        if key.isnumeric():
            key = int(key)
        else:
            key = ALPHABET.index(key) + 1
    ciphertext = ciphertext.upper()

    tt = str.maketrans(ALPHABET, shift_string(ALPHABET, key))
    return [ciphertext.translate(tt)]

def crack(ciphertext):
    l = [decrypt(ciphertext, i)[0] for i in range(26)]
    return crack_sort(l)
