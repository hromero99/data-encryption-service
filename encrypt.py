from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

class EncryptorManager(object):
    # Class to manage the encription actions

    def generate_rsa_key(self,):
        key = RSA.generate(2048)
        return key.exportKey()
    
    
    def encrypt_rsa_msg(self,msg:str,key) -> str:
        try:
            load = RSA.import_key("key.pub")
            
        except ValueError as error:
            return error
    
