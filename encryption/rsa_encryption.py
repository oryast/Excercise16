import fractions
import collections
from encrypton import Encryption
from random_generator import RandomGenerator


KEY_LENGTH = 128  # bits
BLOCK_SIZE = (KEY_LENGTH / 8)  # (bits / 1 byte)


RSAPublicKey = collections.namedtuple('RSAPublicKey', 'n e')
RSAPrivateKey = collections.namedtuple('RSAPrivateKey', 'n d')


def RSAEncryption(Encryption):
    def __init__(self):
        super(RSAEncryption, self).__init__()
        self._generate_keys()

    def _generate_keys(self):
        p = RandomGenerator.prime_integer()
        q = RandomGenerator.prime_integer()
        n = p * q
        totient = (p - 1) * (q - 1)
        e = self._find_coprime(totient)
        d = self._modinv(e, totient)
        self._public_key = RSAPublicKey(n=n, e=e)
        self._private_key = RSAPrivateKey(n=n, d=d)

    def _egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def _modinv(self, a, m):
        g, x, y = self._egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def _find_coprime(self, totient):
        for e in xrange(totient, 1, -1):
            if fractions.gcd(1, e) == 1:
                return e

        raise Exception("No coprime for %d" % (totient, ))

    def encrypt(self, data_to_encrypt):
        blocks = [data_to_encrypt[index:index + BLOCK_SIZE] for index in xrange(0, len(data_to_encrypt), BLOCK_SIZE)]
        cipher_text = []
        for block in blocks:
            cipher_text = self._encrypt_block(block)
        return cipher_text

    def _encrypt_block(self, block_to_encrypt):
        message = self._represent_block_as_integer(block_to_encrypt)
        cipher_text = message ** self._public_key.e
        cipher_text = cipher_text % self._public_key.n
        return cipher_text

    def _represent_block_as_integer(self, block_data):
        return int(block_data.encode('hex'), 16)

    def _integer_to_data(self, integer):
        return hex(integer)[2:].decode("hex")

    def decrypt(self, data_to_decrypt):
        data = ""
        for block in data_to_decrypt:
            block_plain_text = self._decrypt_block(block)
            data += block_plain_text

        return data

    def _decrypt_block(self, encrypted_block):
        plain_text = encrypted_block ** self._private_key.d
        plain_text = plain_text % self._private_key.n
        return plain_text
