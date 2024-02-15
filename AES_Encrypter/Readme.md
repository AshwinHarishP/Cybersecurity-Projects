# AES Encryption and Decryption

This repository contains Python scripts for encrypting and decrypting data using the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining) mode. The scripts utilize the `pycryptodome` library for AES encryption and decryption operations.

## Installation

Before running the scripts, ensure you have the necessary packages installed. You can install the required packages using pip:

```bash
pip install pycryptodome
```

# Usage

The repository contains the following Python scripts:

- `encrypter.py`: Encrypts plaintext data read from `input.txt` and saves the encrypted content to `encrypted.txt`.
- `decrypter.py`: Decrypts ciphertext data read from `encrypted.txt` and prints the decrypted plaintext.
- `main.py`: Provides a menu-driven interface to either encrypt or decrypt data.
- `README.md`: Instructions and overview of the repository.

To use the scripts:

1. Ensure the required packages are installed.
2. Place the plaintext data to be encrypted in `input.txt`.
3. Run `main.py` and choose the appropriate option to encrypt or decrypt data.

## Example


You can run `main.py`, choose the encryption option, and enter the text you want to encrypt. For example, you can input "Cryptography". It will be encrypted, and the encrypted content will be displayed. Then, choosing the decryption option will print the decrypted plaintext.

Please note that you need to run `main.py` and input the text you want to encrypt during the encryption process.


## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
