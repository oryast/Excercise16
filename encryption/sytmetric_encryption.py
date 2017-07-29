from itertools import cycle
from encryption import Encryption


class SymetricEncryption(Encryption):
    def __init__(self):
        super(SymetricEncryption, self).__init__()
        self._key = "61C85192344CBE563222ED9B28719"

    def encrypt(self, data_to_encrypt):
        return self._crypt_function(data_to_encrypt)

    def decrypt(self, data_to_decrypt):
        return self._crypt_function(data_to_decrypt)

    def _crypt_function(self, data):
        previous_byte_result = data[0] ^ self._key[0]
        text = previous_byte_result
        for data_byte, key_byte in zip(data[1:], cycle(self._key[1:])):
            previous_byte_result += data_byte ^ key_byte ^ previous_byte_result
            text += previous_byte_result
        return text
