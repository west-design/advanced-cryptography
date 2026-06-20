from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Hello World"

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("Key:", key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)