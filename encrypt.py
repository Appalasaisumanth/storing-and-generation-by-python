# dtat must be in bytes
from cryptography.fernet import Fernet
key=Fernet.generate_key()
f=Fernet(key)
my_string="fctfc"
my_bytes = memoryview(my_string.encode('utf-8')).tobytes()
k=f.encrypt(my_bytes)
d=f.decrypt(k)
print(d.decode())
