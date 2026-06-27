from cryptography.fernet import Fernet
import time
key = Fernet.generate_key()
cipher = Fernet(key)
print("Generated Key:")
print(key.decode())
with open("Crypto.txt", "rb") as file:
    original_data = file.read()
start = time.perf_counter()

encrypted_data = cipher.encrypt(original_data)

end = time.perf_counter()

with open("encrypted_file.enc", "wb") as file:
    file.write(encrypted_data)


with open("encrypted_file.enc", "rb") as file:
    encrypted = file.read()

decrypted_data = cipher.decrypt(encrypted)

with open("decrypted_file.txt", "wb") as file:
    file.write(decrypted_data)
print("\nEncryption Time: {:.8f} seconds".format(end - start))