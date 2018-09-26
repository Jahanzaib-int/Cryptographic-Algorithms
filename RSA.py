# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:39:35 2018

@author: Jahanzaib Malik
"""

import random
'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
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
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi
def generate_keypair(p, q):
    # Calcuating N
    n = 919 * 1033
    # Calculating Phi
    phi = (919 - 1) * (1033 - 1)
    # Choose an integer e such that e and phi(n) are coprime
    #In our given case Phi will be 947376
    # e should in between(1, phi)
    e = 517
    # Looping and using Euclid's Algorithm to verify that GCD of e and phi(949327) is 1
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    # Use Extended Euclid's Algorithm to generate the private key
    d = modinv(e, phi)
    #d = 358063
    # Return public and private keypair
    # Public key(e, n) and private key (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    # Seperating public key and n from 'pk'
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    #cipher = [pow(ord(char), key, n) for char in plaintext]
    cipher = []
    for char in plaintext:
        order = ord(char)
        print("ASCII is : ", order)
        Encryptedletter = pow(order, key, n)
        print("Power : ",Encryptedletter)
        cipher.append(Encryptedletter)
    print(cipher)
    # Return the array of bytes
    return cipher
def decrypt(pk, ciphertext):
    # Seperating private key and n from 'pk'
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    print(ciphertext)
    #plain = [chr(pow(char, key, n)) for char in ciphertext]
    plain = []
    for char in ciphertext:
        print(char)
        power = pow(char, key) % n
        print("ASCII is : ", power)
        DecryptedMessage = chr(power)
        print("Decrypted : ", DecryptedMessage)
        plain.append(DecryptedMessage)
    # Return the array of bytes as a string
    return ''.join(plain)
if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("RSA Encryption Assignment---Jahanzaib Malik")
    public, private = generate_keypair(919, 1033)
    print ("Encypting using Public key ",public," and Private key ",private," . . .")
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(public, message)
    print("**********************************************\nYour encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("**********************************************\nhiYour message is:")
    print(decrypt(private, encrypted_msg))

