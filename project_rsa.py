#!/usr/bin/env python
# coding: utf-8

# In[76]:


from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


# In[77]:


class Gyurigma:
    def __init__(self):
        self.key = self.resetKey()
        self.pubkey = self.key.publickey()
        self.prikey = self.key.has_private()
        self.encryptor = PKCS1_OAEP.new(self.pubkey)
        self.decryptor = PKCS1_OAEP.new(self.key)

    def resetKey(self):
        random_generator = Random.new().read
        key = RSA.generate(2048, random_generator)
        return key
    
    def savePubKey(self,key,FileName):
        f = open(FileName+'.pem','wb')
        f.write(key.export_key('PEM'))
        f.close()
        print("the key was saved in your location with name of "+ FileName +".pem")
    
    def readKey(self,FileName):
        f = open(FileName+'.pem','r')
        self.key = RSA.import_key(f.read())
        self.pubkey = self.key.publickey()
        self.prikey = self.key.has_private()
        self.encryptor = PKCS1_OAEP.new(self.pubkey)
        self.decryptor = PKCS1_OAEP.new(self.key)
    
    def encrypMsg(self,msg):
        encryptedMsg = self.encryptor.encrypt(str.encode(msg))
        return encryptedMsg
    
    def decrypMsg(self,cryptxt):
        decryptedMsg = self.decryptor.decrypt(cryptxt)
        return decryptedMsg.decode()

