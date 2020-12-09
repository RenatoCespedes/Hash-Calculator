import hashlib
import md5p
import md4p 
import hmac
from hashlib import md5

def hmac_sha1(key, msg):
    m=hmac.new(key,msg,hashlib.sha1)
    # m.update(msg)
    return m.hexdigest()

def hmac_md5(key, msg):
    m=hmac.new(key,msg,hashlib.md5)
    # m.update(msg)
    return m.hexdigest()

def hmac_sha512(key, msg):
    m=hmac.new(key,msg,hashlib.sha512)
    # m.update(msg)
    return m.hexdigest()

def hmac_sha256(key, msg):
    m=hmac.new(key,msg,hashlib.sha256)
    # m.update(msg)
    return m.hexdigest()

def generateHash(filename,key):
    with open(filename, 'rb') as f:
        content = f.read()
        print(content)
        # SHA-1
        sha1 = hashlib.sha1(content).hexdigest()
        # SHA-224
        sha224 = hashlib.sha224(content).hexdigest()
        # SHA-256
        sha256 = hashlib.sha256(content).hexdigest()
        # SHA-384
        sha384 = hashlib.sha384(content).hexdigest()
        # SHA-512
        sha512 = hashlib.sha512(content).hexdigest()
        # hmac sha1
        hmac = hmac_sha1(key.encode(),content)
        # hmac_md5
        hmacmd5 = hmac_md5(key.encode(),content)
        # hmac 256
        hmac256 = hmac_sha256(key.encode(),content)
        # hmac 512
        hmac512 = hmac_sha512(key.encode(),content)
        ## FUNCION MD5
        md5 = md5p.md5sum(content)
        ##FUNCION MD4

        md4 = md4p.md4H(content)


    return {'sha1':sha1, 'sha224':sha224, 'sha256':sha256, 'sha384':sha384,
            'sha512':sha512, 'hmac':hmac, 'hmacmd5':hmacmd5,
            'hmac256':hmac256, 'hmac512':hmac512, 'md5':md5, 'md4':md4}