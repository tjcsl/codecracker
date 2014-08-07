class Cipher:
    def __init__(self):
        raise NotImplementedError()

    def decrypt(self, ciphertext, key):
        raise NotImplementedError("The decrypt function is not implemented for this cipher.")

    def crack(self, ciphertext):
        raise NotImplementedError("The crack function is not implemented for this cipher.")