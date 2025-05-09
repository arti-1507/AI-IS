def encrypt(text, key):
    text = text.replace(" ", "x")
    return ''.join(text[i::key] for i in range(key))

def decrypt(cipher, key):
    cols = -(-len(cipher) // key)  # ceiling division
    rows = key
    shaded = rows * cols - len(cipher)
    result = [''] * cols
    idx = 0

    for r in range(rows):
        for c in range(cols):
            if c == cols - 1 and r >= rows - shaded:
                continue
            result[c] += cipher[idx]
            idx += 1

    return ''.join(result).replace("x", " ")

# Example usage
pt = input("Text to encrypt: ")
k = int(input("Key: "))

ct = encrypt(pt, k)
print("Encrypted:", ct)
print("Decrypted:", decrypt(ct, k))
