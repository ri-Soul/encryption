import RSA

def generate(bitsize):
    (public_key, private_key) = rsa.newkeys(bitsize, poolsize = 8)
    return public_key, private_key

def encrypt(msg, key):
    msg = str(msg).encode("utf-8")
    return msg.encrypt(msg, key)
    
def decrypt(msg, key):
    msg.decrypt(msg, key)
    return msg.decode("utf-8")
