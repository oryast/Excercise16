import random


class RandomGenerator(object):

    @staticmethod
    def prime_integer():
        PRIMES = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, ]
        return PRIMES[random.randint(0, len(PRIMES) - 1)]
