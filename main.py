#A program in python to generate MD5 of string data

import hashlib

print(hashlib.md5(b'Sakshi Hardaha'))

#A program in python to add salting to your hashes

import binascii

name = hashlib.pbkdf2_hmac('md5', b'Sakshi Hardaha', b'acd', 1000)
binascii.hexlify(name)
print(name)
