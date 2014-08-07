def decrypt(ciphertext, key):
    return [ciphertext.decode('base64')]

def crack(ciphertext):
    return decrypt(ciphertext, '')