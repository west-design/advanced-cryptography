from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Display Private Key
print("\nPRIVATE KEY\n")
print(
    private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()
)

# Display Public Key
print("\nPUBLIC KEY\n")
print(
    public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
)


message = input("Enter message: ").strip()

if not message:
    print("Message cannot be empty.")
    exit()


encrypted_message = public_key.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nORIGINAL MESSAGE\n")
print(message)

print("\nENCRYPTED MESSAGE (HEX)\n")
print(encrypted_message.hex())


decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nDECRYPTED MESSAGE\n")
print(decrypted_message.decode())


print("\nVALIDATION\n")
print(message == decrypted_message.decode())