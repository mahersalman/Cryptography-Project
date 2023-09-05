import random
from hashlib import sha256
import elgamal
import rsa
from CBC import *

hash_function = sha256()
key_length = 128

# Bob Generates public and private key of RSA keys,
bit_length = 256
q = rsa.getRandomPrime(bit_length)
p = rsa.getRandomPrime(bit_length)
while p == q:
    q = rsa.getRandomPrime(bit_length)
public, private = rsa.getKeys(p, q)
print(">>> Bob generates a pair of RSA keys and shared the public key")

# Generate a pair of ELGamal keys, public and private and ElGamal sytems
print(">>> Alice generates ElGamal DS system")
alice_elgsys = elgamal.generate_system(key_length, hash_function)
alice_sig_keys = elgamal.generate_keys(alice_elgsys)
print(">>> Alice shares with Bob public key")

# generates hex key (128 bit and iv 64 bit) for Cast128 CBC
print(">>> Alice generates private cast128-CBC key and IV")
key = random.getrandbits(128)
iv = hex(random.getrandbits(64))

# Encrypt the key
encrypted_key = rsa.encrypt(str(key), public)
print(">>> Alice encrypted cast128-CBC key using RSA ")

# Use the ElGamal private key to sign the key
print(">>> Alice signs on the Key cipher-text ")
signatureOnCipher = elgamal.sign(alice_elgsys, ''.join(str(encrypted_key)), alice_sig_keys[0])
# encrypt mail
print(">>> Alice write and encrypt mail and send encrypted message")
message = "Hi Bob, Congratulations you getting a 100 in Data Security and Cryptography"
hex_key = hex(key)[2:]
cipher_text = cbc_encrypt(message, hex_key, iv)
print("-The  Email cipherText : ", cipher_text)

print('>>> Alice shared the encrypted mail,encrypted key ,iv ,digital signature')

# verify digital signature
print('>>> Bob verify the Key')
isVerified = elgamal.verify(alice_elgsys, ''.join(str(encrypted_key)), signatureOnCipher, alice_sig_keys[1])
if not isVerified:
    print("ERROR - the message is fake ")
else:
    # decrypt key
    print(">>> Bob decrypts the CAST128 key using his private RSA key")
    decrypted_key = hex(int(rsa.decrypt(encrypted_key, private)))[2:]
    print("-The CAST128 key in Hex : ",decrypted_key)
    print(">>> Bob decrypts the Email")
    decryptedEmail = cbc_decrypt(cipher_text,decrypted_key,iv)
    print("-Decrypted email  :  " + decryptedEmail)
