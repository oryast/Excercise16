from itertools import cycle
from encryption import Encryption


class SymetricEncryption(Encryption):
    def __init__(self):
        super(SymetricEncryption, self).__init__()
        self._key = "61C85192344CBE563222ED9B28719"

    def encrypt(self, data_to_encrypt):
        previous_byte_result = ord(data_to_encrypt[0]) ^ ord(self._key[0])
        text = chr(previous_byte_result)
        for data_byte, key_byte in zip(data_to_encrypt[1:], cycle(self._key[1:])):
            previous_byte_result = (ord(data_byte) ^
                                    ord(key_byte) ^
                                    previous_byte_result)
            text += chr(previous_byte_result)
        return text

    def decrypt(self, data_to_decrypt):
        text = chr(ord(data_to_decrypt[0]) ^ ord(self._key[0]))
        previous_byte = data_to_decrypt[0]
        for data_byte, key_byte in zip(data_to_decrypt[1:], cycle(self._key[1:])):
            text += chr(ord(data_byte) ^ ord(key_byte) ^ ord(previous_byte))
            previous_byte = data_byte
        return text
