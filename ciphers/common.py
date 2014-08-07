class Cipher:
    def __init__(self):
        raise NotImplementedError()

    def decrypt(self, ciphertext, key):
        raise NotImplementedError("The decrypt function is not implemented for this cipher.")

    def crack(self, ciphertext):
        raise NotImplementedError("The crack function is not implemented for this cipher.")

def shift_string(string, offset):
    if offset == 0:
        return string
    return string[offset:len(string)] + string[0:offset]
