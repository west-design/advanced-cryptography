def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97

            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97

            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


print("Enter message:")
message = input()

if message.strip() == "":
    print("Error: Message cannot be empty")
    exit()

print("Enter key:")
key = input()

if key.strip() == "":
    print("Error: Key cannot be empty")
    exit()

encrypted = vigenere_encrypt(message, key)
decrypted = vigenere_decrypt(encrypted, key)


print("Encrypted:", encrypted)
print("Decrypted:", decrypted)