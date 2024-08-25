from Crypto.Cipher import AES, DES
import base64
import rsa

def pad(text, block_size):
    while len(text) % block_size != 0:
        text += ' '
    return text

def aes_encrypt(text, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypted_text = base64.b64encode(cipher.encrypt(pad(text, 16).encode('utf-8')))
    return encrypted_text.decode('utf-8')

def aes_decrypt(encrypted_text, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

def des_encrypt(text, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    encrypted_text = base64.b64encode(cipher.encrypt(pad(text, 8).encode('utf-8')))
    return encrypted_text.decode('utf-8')

def des_decrypt(encrypted_text, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

def rsa_generate_keys():
    (public_key, private_key) = rsa.newkeys(512)
    return public_key, private_key

def rsa_encrypt(text, public_key):
    encrypted_text = rsa.encrypt(text.encode('utf-8'), public_key)
    return encrypted_text

def rsa_decrypt(encrypted_text, private_key):
    decrypted_text = rsa.decrypt(encrypted_text, private_key).decode('utf-8')
    return decrypted_text

def main():
    text = input("Enter the text to be encrypted: ")
    algorithm = input("Choose the encryption algorithm (AES/DES/RSA): ").upper()
    key = None
    public_key = None
    private_key = None

    if algorithm == "AES":
        key = input("Enter the AES key (16 characters): ")
        encrypted_text = aes_encrypt(text, key)
        print("Encrypted text (AES):", encrypted_text)
        print("Decrypted text (AES):", aes_decrypt(encrypted_text, key))

    elif algorithm == "DES":
        key = input("Enter the DES key (8 characters): ")
        encrypted_text = des_encrypt(text, key)
        print("Encrypted text (DES):", encrypted_text)
        print("Decrypted text (DES):", des_decrypt(encrypted_text, key))

    elif algorithm == "RSA":
        public_key, private_key = rsa_generate_keys()
        encrypted_text = rsa_encrypt(text, public_key)
        print("Encrypted text (RSA):", encrypted_text)
        print("Decrypted text (RSA):", rsa_decrypt(encrypted_text, private_key))

    else:
        print("Invalid algorithm selected.")

if __name__ == "__main__":
    main()