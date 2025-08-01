from cryptography.fernet import Fernet

def decrypter():

    # Key Input
    key = input("🔑 Input key: ").encode()

    # Encrypted Text Input
    ciphertext = input("🔐 Input encrypted text: ").encode()

    # Decrypt
    cipher = Fernet(key)

    try:
        message = cipher.decrypt(ciphertext).decode()
        """
        Decrypts the message
        """
        print("✅ Decrypted message:", message)
    except ValueError as e:
        print("❌ Decryption failed.", e)
