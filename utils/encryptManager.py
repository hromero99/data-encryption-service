from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import secrets

class EncryptorManager(object):

    def __init__(self, public_key: str = None, private_key: str = None):
        if public_key:
            self.p_key = RSA.import_key(public_key)
        if private_key:
            self.private_key = RSA.import_key(private_key)

    def encrypt(self, msg: str) -> str:
        cipher = Cipher_PKCS1_v1_5.new(self.p_key)
        t_seed = secrets.token_hex(16)
        with open(f"/tmp/{t_seed}", "wb") as encrypted:
            encrypted.write(cipher.encrypt(msg.encode()))
            encrypted.close()
        return t_seed

    def decrypt(self, encrypted: bytes):
        decipher = Cipher_PKCS1_v1_5.new(self.private_key)
        return decipher.decrypt(encrypted, None).decode()

