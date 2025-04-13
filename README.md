AES Encryption in Python

This project demonstrates how to securely encrypt and decrypt text using the Advanced Encryption Standard (AES) in Python. It supports both CBC (Cipher Block Chaining) and ECB (Electronic Codebook) modes and uses the cryptography library.

Features
	•	Encrypt plaintext messages using AES encryption
	•	Decrypt ciphertext back to readable plaintext
	•	Uses randomly generated keys and IVs
	•	Supports both CBC and ECB encryption modes
	•	Includes proper error handling

Technologies Used
	•	Python 3.x
	•	cryptography library (PyCA)

How to Run
	1.	Install the required library:
pip install cryptography
	2.	Run the script:
python aes_encryption.py

Example Output

Original Text: Hello World
Encrypted (CBC): b’g84F2jk1…’
Decrypted Text: Hello World

Notes
	•	CBC mode is more secure and recommended for actual use.
	•	ECB mode is included to demonstrate how different cipher modes affect encryption behavior.
	•	This project is for learning purposes and should not be used in production without additional security measures.

Author

Rachid Dwyer – Refonte Cybersecurity Internship Project
