import hashlib
import math
import random
# from sympy import mod_inverse, gcd, randprime


def is_prime(n, k=30):
    if n <= 3:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


def generate_prime(bits=256):
    left = 2 ** (bits - 1)
    right = 2 ** bits
    while True:
        p = random.randint(left, right)
        if is_prime(p):
            return p


def get_different_primes():
    while True:
        p = generate_prime()
        q = generate_prime()
        if p != q:
            return p, q


def extended_gcd(a, b):
    print(a, b)
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y


def mod_inverse(d, m):
    gcd, x, y = extended_gcd(d, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse does not exist for {d} modulo {m}")
    else:
        return ((x % m) + m) % m


def get_coprime(m):
    while True:
        d = random.randint(2, m - 1)
        if math.gcd(m, d) == 1:
            return d


def generate_keys():
    p, q = get_different_primes()
    n = p * q
    m = (p - 1) * (q - 1)
    d = get_coprime(m)
    e = mod_inverse(d, m)
    return (n, e), (n, d)


def encrypt(message, public_key):
    n, e = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    n, d = private_key
    return pow(ciphertext, d, n)


def sign(message, private_key):
    hashed_message = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    return encrypt(hashed_message, private_key)


def verify(message, signature, public_key):
    hashed_message = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    decrypted_signature = decrypt(signature, public_key)
    return hashed_message == decrypted_signature
