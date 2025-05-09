from Crypto.Cipher import DES
import binascii
def pad(text):
    while len(text) % 8 != 0:
        text += ' '  # Padding with space
    return text
plaintext = input("Enter the message to encrypt: ")
key = input("Enter an 8-character key: ").encode()
if len(key) != 8:
    print("Error: Key must be exactly 8 characters long!")
    exit()
padded_text = pad(plaintext)
cipher = DES.new(key, DES.MODE_ECB)  # Using ECB mode
encrypted_text = cipher.encrypt(padded_text.encode())
print("\nEncrypted (Hex):", binascii.hexlify(encrypted_text).decode())
decrypted_text = cipher.decrypt(encrypted_text).decode().rstrip()
print("Decrypted:", decrypted_text)