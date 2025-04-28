# AES Encryption in Python

This project demonstrates how to securely encrypt and decrypt messages using the Advanced Encryption Standard (AES) in Python. It compares both CBC (Cipher Block Chaining) and ECB (Electronic Codebook) modes using the `cryptography` library.

---

##  Features

- AES-256 encryption using CBC and ECB modes
- Randomly generated secure key (256-bit) and IV (for CBC)
- Padding logic to meet AES block size requirements
- Clear output showing encrypted and decrypted messages
- Demonstrates differences between CBC and ECB encryption behavior

---

##  Example Output

Below is a screenshot showing the script successfully encrypting and decrypting a message using both AES modes:

![CBC and ECB Output](cbcebc_encryption_output.png)

---

##  Technologies Used

- Python 3.13
- [`cryptography`](https://cryptography.io/en/latest/) (PyCA)
- Windows Command Prompt

---

##  How to Run This Project

1. Install Python 3.13 and ensure it's added to your system PATH  
2. Install the cryptography library:
   ```bash
   pip install cryptography
   ```
3. Run the script:
   ```bash
   python aes_encryption.py
   ```

---

##  Notes

- CBC mode is more secure and recommended for actual use.
- ECB mode is included to demonstrate how different cipher modes affect encryption behavior.
- This project is for learning purposes and should not be used in production without additional security measures.

---

## Author

**Rachid Dwyer**  
Cybersecurity Intern @ Refonte  
Master’s in Cybersecurity Technology (UMGC) 
GitHub: [https://github.com/your-github-Rachid1026](https://github.com/Rachid1026)

