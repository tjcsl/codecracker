import re
from .common import crack_sort, ALPHABET
from pycipher import Playfair

def key_to_keysquare(key):

    keysquare = ''
    for c in key:
        if c in keysquare:
            continue
        keysquare = keysquare + c
    keysquare2 = keysquare
    # Omit Q
    for c in ALPHABET:
        if c=='Q' or c in keysquare:
            continue
        keysquare = keysquare + c
    # I=J
    if 'I' in key and 'J' in key:
        return [keysquare] # No I=J if both are in keyword

    if 'I' in key or 'J' in key:
        for c in ALPHABET:
            if c in 'IJ' or c in keysquare2:
                continue
            keysquare2 = keysquare2 + c
    else:
        for c in ALPHABET:
            if c == 'J' or c in keysquare2:
                continue
            keysquare2 = keysquare2 + c
    return [keysquare, keysquare2] 

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    results = []
    keysquare = key_to_keysquare(key)
    for ks in keysquare:
        try:
            results.append(Playfair(key=ks).decipher(ciphertext))
        except:
            pass
    return crack_sort(results)

def crack(ciphertext):
    raise NotImplementedError()