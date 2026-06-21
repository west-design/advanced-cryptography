def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


print("Enter message:")
message = input()

if message.strip() == "":
    print("Error: Message cannot be empty")
    exit()

print("Enter shift value:")
shift_input = input()

if not shift_input.isdigit():
    print("Error: Shift must be a number")
    exit()

shift = int(shift_input)


encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)


print("Encrypted:", encrypted)
print("Decrypted:", decrypted)