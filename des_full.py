# Initial Permutation table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation table
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Expansion D-box Table
EXPANSION = [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]

# S-box (only one shown here for simplicity)
SBOX = [[[14, 4, 13, 1],
         [2, 15, 11, 8],
         [3, 10, 6, 12],
         [5, 9, 0, 7]],

        [[0, 15, 7, 4],
         [14, 2, 13, 1],
         [10, 6, 12, 11],
         [9, 5, 3, 8]]]

# Permutation P-box Table
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

def permute(block, table):
    return ''.join([block[i-1] for i in table])

def xor(a, b):
    return ''.join(['0' if i == j else '1' for i, j in zip(a, b)])

def sbox_substitution(block):
    # Simplified S-box operation
    row = int(block[0] + block[5], 2)
    col = int(block[1:5], 2)
    val = SBOX[0][row % 4][col % 4]
    return f"{val:04b}"

def feistel(right, subkey):
    expanded = permute(right, EXPANSION)
    xored = xor(expanded, subkey)
    substituted = ''
    for i in range(0, len(xored), 6):
        substituted += sbox_substitution(xored[i:i+6])
    return permute(substituted, P)

def des_encrypt(plain, key):
    plain = permute(plain, IP)
    left = plain[:32]
    right = plain[32:]

    for _ in range(2):  # only 2 rounds shown for simplicity
        subkey = key[:48]  # fixed subkey for example
        f_out = feistel(right, subkey)
        new_right = xor(left, f_out)
        left = right
        right = new_right

    combined = left + right
    return permute(combined, FP)

# Sample Input (64-bit plaintext & key)
plaintext = "0001001000110100010101100111100010011010101111001101111011110001"
key =      "0001001100110100010101110111100110011011101111001101111111110001"

cipher = des_encrypt(plaintext, key)
print("Encrypted:", cipher)
