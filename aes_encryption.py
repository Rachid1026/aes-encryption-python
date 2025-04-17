from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Create a 256-bit key (32 bytes) and 128-bit IV (16 bytes)
key = os.urandom(32)  # AES-256
iv = os.urandom(16)   # IV for CBC mode

# Message to encrypt
plaintext = b"Hello, this is my first encrypted message!"

# Encrypt using AES in CBC mode
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()

# Pad the plaintext so it's a multiple of 16 bytes (AES block size)
padding_length = 16 - len(plaintext) % 16
padded_plaintext = plaintext + bytes([padding_length]) * padding_length

ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

print("Encrypted (CBC):", ciphertext)

# Decrypt the message
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

# Remove padding after decryption
unpadded_plaintext = decrypted_padded[:-decrypted_padded[-1]]

print("Decrypted (CBC):", unpadded_plaintext.decode())

# -------------------- ECB MODE --------------------

# Encrypt using AES in ECB mode (note: IV is not used in ECB)
cipher_ecb = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
encryptor_ecb = cipher_ecb.encryptor()

# Pad the plaintext again (same as before)
padded_plaintext_ecb = plaintext + bytes([padding_length]) * padding_length

ciphertext_ecb = encryptor_ecb.update(padded_plaintext_ecb) + encryptor_ecb.finalize()

print("Encrypted (ECB):", ciphertext_ecb)

# Decrypt with ECB
decryptor_ecb = cipher_ecb.decryptor()
decrypted_padded_ecb = decryptor_ecb.update(ciphertext_ecb) + decryptor_ecb.finalize()
unpadded_plaintext_ecb = decrypted_padded_ecb[:-decrypted_padded_ecb[-1]]

print("Decrypted (ECB):", unpadded_plaintext_ecb.decode())


