from cryptography.fernet import Fernet

def encrypter():

    # Selector
    selection = input("🔐 Do you want to use your own key? (y/n): ")
    """_summary_
    """

    # Generate/Load key
    if selection.lower() == "y":
        userkey = input("🔑 Enter your key: ")
        key = userkey.encode()
        """_summary_
        """
    else:
        key = Fernet.generate_key()
        """_summary_
        """
        print("🆕🔑 A new key was generated and will be used.")

    cipher = Fernet(key)

    # Nachricht
    message = input("✏️ Enter message: ")
    message_bytes = message.encode()
    """_summary_
    """

    # Schlüssel anzeigen
    print ("🔑 Key:", key.decode())

    # Verschlüsseln
    chiffretext = cipher.encrypt(message_bytes)
    """_summary_
    """
    print("🔐 Encrypted:", chiffretext)

    # Warning
    print("**WARNING**: Only the text between the two ' is encrypted text!")
