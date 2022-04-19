# Mashal Buhamad 2022
# MEWRE Training

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def ReadPrivateKey(filename):
    with open(filename, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
    return(private_key)
            
def ReadPublicKey(filename):
    with open(filename, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
    return(public_key)

def EncryptIt(plain_text):
    public_key=ReadPublicKey('public_key.pem')
    cipher_text_bytes = public_key.encrypt(plaintext=plain_text.encode(),
                                           padding=padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                algorithm=hashes.SHA512(),
                                                                label=None))
    return(cipher_text_bytes)


def DecryptIt(cipher_text):
    private_key=ReadPrivateKey('private_key.pem')
    decrypted_cipher_text_bytes = private_key.decrypt(ciphertext=(cipher_text), 
                                                      padding=padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA512(),label=None))
    return (decrypted_cipher_text_bytes)
 