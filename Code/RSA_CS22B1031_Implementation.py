import random

# Function to find GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Function to generate RSA keys
def generate_keys():
    print("Generating RSA keys...")
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17  # Choose e such that gcd(e, phi) = 1

    if gcd(e, phi) != 1:
        raise Exception("e and phi are not coprime!")

    d = mod_inverse(e, phi)
    if d is None:
        raise Exception("Failed to find modular inverse")

    public_key = (e, n)
    private_key = (d, n)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    return public_key, private_key

# Encryption: c = m^e mod n
def encrypt(plaintext, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

# Decryption: m = c^d mod n
def decrypt(ciphertext, private_key):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Main user interaction
def main():
    print("==== RSA Encryption/Decryption ====")
    public_key, private_key = generate_keys()

    message = input("\nEnter your message to encrypt: ")
    cipher = encrypt(message, public_key)
    print(f"\n🔒 Encrypted Message: {cipher}")

    decrypted = decrypt(cipher, private_key)
    print(f"🔓 Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
