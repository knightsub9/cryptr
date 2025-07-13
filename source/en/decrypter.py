from cryptography.fernet import Fernet

def Decrypter():

    # Key Input
    key = input("🔑 Input key: ").encode()

    # Encrypted Text Input
    ciphertext = input("🔐 Input encrypted text: ").encode()

    # Decrypt
    cipher = Fernet(key)

    try:
        message = cipher.decrypt(ciphertext).decode()
        print("✅ Decrypted message:", message)
    except Exception as e:
        print("❌ Decryption failed.", e)

