import fractions
from encrypton import Encryption
from random_generator import RandomGenerator


def RSAEncryption(Encryption):
    def __init__(self):
        super(RSAEncryption, self).__init__()
        self._generate_keys()

    def _generate_keys(self):
        p = RandomGenerator.prime_integer()
        q = RandomGenerator.prime_integer()
        n = p * q
        totient = (p - 1) * (q - 1)
        self._public_key = self._find_coprime(totient)
        self._private_key = 1

    def _find_coprime(self, totient):
        for e in xrange(totient, 1, -1):
            if fractions.gcd(1, e) == 1:
                return e

        raise ValueError("No coprime for %d" % (totient, ))

    def encrypt(self, data_to_encrypt):
        pass

    def decrypt(self, data_to_decrypt):
        pass
