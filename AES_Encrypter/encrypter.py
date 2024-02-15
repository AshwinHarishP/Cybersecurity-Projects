from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def encrypt_AES(plaintext, key, iv):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        return iv + ciphertext  
    except ValueError as e:
        print("Error: Invalid key size:", e)
        return None

def main():
    key = b'\xe4\x94J\xd8\xaa\xe8\xba\x97\xe5\xb1\xac\xf2\xf7&\xb4\xdf'
    iv = os.urandom(AES.block_size)

    print("Enter the plaintext to encrypt:")
    plaintext = input().encode()

    encrypted_content = encrypt_AES(plaintext, key, iv)
    if encrypted_content is not None:
        print("Encrypted content:")
        print(encrypted_content.hex())  

    else:
        print("Encryption failed.")

if __name__ == "__main__":
    main()
