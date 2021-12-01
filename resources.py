import math

# funcions used in main app

def is_prime(n):
    if n == 0: return False
    if n == 2 or n == 3: return True  # since all primes > 3 are of the form 6n ± 1
    if n < 2 or n % 2 == 0: return False  # start with f=5 (which is prime)
    if n < 9: return True  # and test f, f+2 for being prime
    if n % 3 == 0: return False  # then loop by 6.
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True

def polynomial(x, n):
    return (x ** 2 - 1) % n

def algorithm(n):
    d = 1
    x = 2
    y = 2
    while d == 1:
        x = int(polynomial(x, n))
        y = int(polynomial(polynomial(y, n), n))
        d = math.gcd(int(abs(x - y)), n)

    if d == n:
        return "Done"
    else:
        return d

def factorization(n):
    primes = []
    if algorithm(n) == "Done":
        primes.append(n)
    else:
        first = int(algorithm(n))
        primes.append(first)
        check = n

        while check / first != 1:
            m = int(check / first)
            next = algorithm(m)
            if next == "Done":
                primes.append(int(n / math.prod(primes)))
                break
            else:
                primes.append(next)
                check = check / next

    return primes

def euclid(a, b):
    return (1 - a * euclid(b, a % b)) / b % a if b else 0
