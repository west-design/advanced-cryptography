import time
def rc4(key, data):
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = 0
    j = 0
    output = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        output.append(byte ^ k)
    return output
message = input("Enter message: ")
if message.strip() == "":
    print("Error: Message cannot be empty.")
    exit()
key = input("Enter key: ")
if key.strip() == "":
    print("Error: Key cannot be empty.")
    exit()
start = time.perf_counter()
encrypted = rc4(key, message.encode())
decrypted = rc4(key, encrypted)
end = time.perf_counter()
print("Original Message :", message)
print("Encrypted :", encrypted.hex())
print("Decrypted:", decrypted.decode())

print("\nExecution Time: {:.8f} seconds".format(end - start))