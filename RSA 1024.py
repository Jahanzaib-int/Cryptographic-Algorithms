# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:42:09 2018

@author: Jahanzaib Malik
"""

import random
import math
import sys
from random import randint
'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
'''
if a number is prime according to fermat's theorm
'''
def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True
def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    # Choose an integer e such that e and phi(n) are coprime
    # e should in between(1, phi)
    e = 517

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    '''g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
'''
    # Use Extended Euclid's Algorithm to generate the private key
    #d = modinv(e, phi)
    d = 358063

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(publicKey, plaintext):
    # Unpack the key into it's components
    key, n = publicKey
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = []
    for char in plaintext:
        order = ord(char)
        # print("Order is : ", order)
        coded = pow(order, key, n)
        # print("Power : ",coded)
        cipher.append(coded)
    # print(cipher)
    # Return the array of bytes
    return cipher
def decrypt(privateKey, ciphertext):
    # Unpack the key into its components
    key, n = privateKey
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = []
    for char in ciphertext:
        # print(char)
        power = pow(char, key) % n
        # print("power is : ", power)
        uncoded = chr(power)
        # print("uncoded : ", uncoded)
        plain.append(uncoded)
    # Return the array of bytes as a string
    return ''.join(plain)
if __name__ == '__main__':

    print("RSA Encryption Assignment---Jahanzaib Malik")
    print("Generating your public/private keypairs now . . .")
    p = generate_big_prime(1024)
    q = generate_big_prime(1024)
    print("large p & q Generated")
    public, private = generate_keypair(p, q)
    #public, private = generate_keypair(p, q)
    print("Your public key is ", public, " \n and your private key is ", private)
    message = "bear"

    '''              Given Input...
                     "bear",
                     "kangaroo",
                     "wombat",
                     "A koala is not a bear even if its Chinese translation means bear without tail.",
                     "Longer text messages will be given next week."
'''
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with private key ", private, " . . .")
    print("Your message is:")
    print(decrypt(private, encrypted_msg))

