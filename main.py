from rsa import *
from resources import *
from logo import printLogo
from sympy import primerange
import time

if __name__ == '__main__':
    menu=None
    factors = []

    printLogo()

    while menu != 0:
        print('0 - Quit application \n1 - Generate key by bitlenght\n2 - Enter key\n3 - Generate key by range')
        menu = int(input())
        if menu == 1:
            print("Generating RSA:")
            generated = RSA()
            keylen = int(input("Please enter bitlenght of a key: "))
            generated.genprimes(keylen)
            generated.genrsa()

            generated.printRsa()

            startTime = time.time()
            factors=factorization(generated.n)
            print("Factorization took ", time.time() - startTime, " seconds "),
            cracked = CrackedRSA(factors[0], factors[1], generated.e)
            cracked.crack_rsa()
            cracked.printRsa()
        if menu == 2:
            p: int=0
            q: int=0
            print("Please enter primes p & q of RSA:")
            while not is_prime(p):
                p = int(input("Enter prime p: "))
            while not is_prime(q):
                q = int(input("Enter prime q: "))
            generated = RSA()
            generated.setprimes(p, q)
            generated.genrsa()
            public_exp = int(input("(Leave empty for it to be generated)\nPlease enter public exponent e: "))

            #TODO: Ak e nebude pasovat nech to vypise: public exponent has to be coprime with modulo of RSA

            if public_exp != '':
                if generated.check_e():
                    generated.rsaset_e(public_exp)
                    generated.genrsa()
            generated.printRsa()

            startTime = time.time()
            factors = factorization(generated.n)
            print("Factorization took ", time.time() - startTime, " seconds "),
            cracked = CrackedRSA(factors[0], factors[1], generated.e)
            cracked.crack_rsa()
            cracked.printRsa()
        if menu == 3:
            lowerprime = 0
            higherprime = 0
            print("Set the floor of range of primes: ")
            lowerprime = int(input())
            print("Set the top of range of primes: ")
            higherprime = int(input())
            primes = sorted(primerange(lowerprime, higherprime))
            p, q = random.sample(primes, 2)
            generated = RSA()
            generated.setprimes(p, q)
            generated.genrsa()
            generated.printRsa()

            startTime = time.time()
            factors = factorization(generated.n)
            print("Factorization took ", time.time() - startTime, " seconds "),
            cracked = CrackedRSA(factors[0], factors[1], generated.e)
            cracked.crack_rsa()
            cracked.printRsa()



quit()