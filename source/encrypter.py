from cryptography.fernet import Fernet
import json
import os

# Path to config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

# Standard language (as fallback)
language_code = "en"
translations = {}

# Load config
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
        language_code = config.get("language", "en")

# Load language file
lang_file = os.path.join(os.path.dirname(__file__), "languages", f"{language_code}.json")

if not os.path.exists(lang_file):
    print(f"[WARN] Language '{language_code}' not found.")
    lang_file = os.path.join(os.path.dirname(__file__), "languages", "en.json")

with open(lang_file, "r", encoding="utf-8") as f:
    translations = json.load(f)

def translate(key):
    return translations.get(key, f"[MISSING:{key}]")

def encrypter():

    # Selector
    selection = input(translate("ownkey_ask"))
    """
    Asks the user if they want to use their own key.
    """

    # Generate/Load key
    if selection.lower() == "y":
        userkey = input(translate("key_input_encrypter"))
        key = userkey.encode()

    else:
        key = Fernet.generate_key()
        print(translate("newkey_generated"))

    cipher = Fernet(key)

    # Nachricht
    message = input(translate("enter_message"))
    message_bytes = message.encode()

    # Schlüssel anzeigen
    print (translate("show_key"), key.decode())

    # Verschlüsseln
    chiffretext = cipher.encrypt(message_bytes)
    """
    Encrypts the message.
    """
    print(translate("message_encrypted"), chiffretext)

    # Warning
    print(translate("warning_encrypter"))
