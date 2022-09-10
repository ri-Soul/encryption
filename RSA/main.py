import RSA_module

RSA_module.generate(4096) = public_key, private_key

msg = RSA_module.encrypt(input("MSG: "), public_key)
print(msg)
RSA_module.decrypt(msg, private_key)