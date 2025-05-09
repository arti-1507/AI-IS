def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def egcd(a, b):
        if b == 0: return a, 1, 0
        g, x1, y1 = egcd(b, a % b)
        return g, y1, x1 - (a // b) * y1
    g, x, y = egcd(e, phi)
    return x % phi if g == 1 else None

def encrypt(text, e, n):
    return [pow(ord(c), e, n) for c in text]

def decrypt(cipher, d, n):
    return ''.join(chr(pow(c, d, n)) for c in cipher)

# Input primes
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
if not (is_prime(p) and is_prime(q)):
    print("Both numbers must be prime!")
    exit()

n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, phi)
if d is None:
    print("No modular inverse found for e. Try different primes.")
    exit()

print(f"\nPublic Key: ({e}, {n})")
print(f"Private Key: ({d}, {n})")

message = input("Enter message: ")
cipher = encrypt(message, e, n)
print("Encrypted:", cipher)

decrypted = decrypt(cipher, d, n)
print("Decrypted:", decrypted)
