from cryptography.fernet import Fernet

def encrypter():

    # Selector
    selection = input("🔐 Do you want to use your own key? (y/n): ")
    """
    Asks the user if the want to use their own key.
    """

    # Generate/Load key
    if selection.lower() == "y":
        userkey = input("🔑 Enter your key: ")
        key = userkey.encode()

    else:
        key = Fernet.generate_key()
        print("🆕🔑 A new key was generated and will be used.")

    cipher = Fernet(key)

    # Nachricht
    message = input("✏️ Enter message: ")
    message_bytes = message.encode()

    # Schlüssel anzeigen
    print ("🔑 Key:", key.decode())

    # Verschlüsseln
    chiffretext = cipher.encrypt(message_bytes)
    """
    Encrypts the message.
    """
    print("🔐 Encrypted:", chiffretext)

    # Warning
    print("**WARNING**: Only the text between the two ' is encrypted text!")
