from resources import *
from Crypto.Util import number
import random
import math

#classes for generated and cracked rsa key

class RSA:
    def __init__(self):
        self.p: int = 0
        self.q: int = 0
        self.e: int = 0
        self.d: int = 0
        self.phi: int = 0
        self.n: int = 0

    def genrsa(self):
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        while self.e == self.d:
            while math.gcd(self.e, self.phi) != 1:
                self.e = random.randint(2, self.phi - 1)
            self.d = int(euclid(self.phi, self.e))
        int(self.e)

    def genprimes(self, keylen: int):
        self.p = number.getPrime(keylen // 2)
        self.q = number.getPrime(keylen // 2)

    def setprimes(self, p: int, q: int):
        self.p = p
        self.q = q

    def printRsa(self):
        print("GENERATED VALUES")
        print("----------------")
        print("p = %i q = %i" % (self.p, self.q))
        print("n = %i" % self.n)
        print("e = %i" % self.e)
        print("phi = %i" % self.phi)
        print("d = %i" % self.d)
        print("----------------")
    def check_e(self):
        if math.gcd(self.e, self.phi) != 1:
            return False
        else:
            return True
    def rsaset_e(self, e: int):
        self.e = e
        self.d = int(euclid(self.phi, self.e))
class CrackedRSA:
    def __init__(self, p: int, q: int, e: int):
        self.p = p
        self.q = q
        self.e = e
        self.n = p*q
        self.d: int = 0
        self.phi: int = 0

    def crack_rsa(self):
        self.phi = (self.p - 1) * (self.q - 1)
        self.d = int(euclid(self.phi, self.e))

    def printRsa(self):
        print("CRACKED VALUES")
        print("----------------")
        print("p = %i q = %i" % (self.p, self.q))
        print("n = %i" % self.n)
        print("e = %i" % self.e)
        print("phi = %i" % self.phi)
        print("d = %i" % self.d)
        print("----------------")