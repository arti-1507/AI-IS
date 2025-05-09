from Crypto.Cipher import DES
import binascii

def generate_des_subkeys(key):
    """Manually generate 16 different 48-bit round keys without using PC1 and PC2 matrices"""
    key_bits = bin(int.from_bytes(key, "big"))[2:].zfill(64)  # Convert to 64-bit binary
    subkeys = []

    # Generate 16 different round keys by shifting bits
    for i in range(16):
        shifted_key = key_bits[i:] + key_bits[:i]  # Left circular shift
        subkey = shifted_key[:48]  # Take the first 48 bits
        subkeys.append(subkey)

    return subkeys

def binary_to_hex(binary_str):
    """Convert a binary string to hexadecimal (for displaying 48-bit subkeys)"""
    hex_str = hex(int(binary_str, 2))[2:].upper().zfill(12)  # 48-bit hex (12 hex digits)
    return hex_str

def des_encrypt(plaintext, key):
    """Encrypt plaintext using DES"""
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def des_decrypt(ciphertext, key):
    """Decrypt ciphertext using DES"""
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# User Input
plaintext = input("Enter a message (max 8 characters): ").encode().ljust(8)[:8]  # Ensure 8 bytes
key_hex = input("Enter 8-character hexadecimal key (16 hex digits): ").strip()
key = binascii.unhexlify(key_hex)  # Convert hex key to bytes

# Generate and display unique 48-bit subkeys
subkeys = generate_des_subkeys(key)
print("\nGenerated DES Round Keys (48-bit each, in hex):")
for i, subkey in enumerate(subkeys, start=1):
    print(f"Round {i} Key: {binary_to_hex(subkey)}")

# Encryption
ciphertext = des_encrypt(plaintext, key)
print("\nEncrypted Ciphertext (Hex):", binascii.hexlify(ciphertext).decode().upper())

# Decryption
decrypted_text = des_decrypt(ciphertext, key)
print("Decrypted Plaintext:", decrypted_text.decode().strip())