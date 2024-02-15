from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_AES(ciphertext, key, iv):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(ciphertext[AES.block_size:])
        plaintext = unpad(decrypted_data, AES.block_size)
        return plaintext
    except ValueError as e:
        print("Error: Decryption failed.", e)
        return None

def main():
    key = b'\xe4\x94J\xd8\xaa\xe8\xba\x97\xe5\xb1\xac\xf2\xf7&\xb4\xdf'

    print("Enter the encrypted content in hexadecimal format:")
    encrypted_content_hex = input()
    try:
        encrypted_content = bytes.fromhex(encrypted_content_hex)
        iv = encrypted_content[:AES.block_size]
        plaintext = decrypt_AES(encrypted_content, key, iv)
        if plaintext is not None:
            print("Decrypted plaintext:")
            print(plaintext.decode())  
        else:
            print("Decryption failed.")
    except ValueError:
        print("Invalid input format. Please enter hexadecimal ciphertext.")

if __name__ == "__main__":
    main()
