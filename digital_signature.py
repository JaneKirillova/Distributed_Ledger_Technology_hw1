import hashlib
import random
from sympy import mod_inverse, gcd, randprime


def generate_prime(bits=10 ** 3) -> int:
    return randprime(2 ** (bits - 1), 2 ** bits)


def get_different_primes():
    while True:
        p = generate_prime()
        q = generate_prime()
        if p != q:
            return p, q


def get_coprime(m):
    while True:
        d = random.randint(2, m - 1)
        if gcd(m, d) == 1:
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
