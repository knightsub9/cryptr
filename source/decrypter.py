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
lang_file = os.path.join(os.path.dirname(__file__), "lang", f"{language_code}.json")

if not os.path.exists(lang_file):
    print(f"[WARN] Language '{language_code}' not found.")
    lang_file = os.path.join(os.path.dirname(__file__), "lang", "en.json")

with open(lang_file, "r", encoding="utf-8") as f:
    translations = json.load(f)

def translate(key):
    return translations.get(key, f"[MISSING:{key}]")


def decrypter():

    # Key Input
    key = input(translate("input_key_encrypter")).encode()

    # Encrypted Text Input
    ciphertext = input(translate("encryptedtext_input")).encode()

    # Decrypt
    cipher = Fernet(key)

    try:
        message = cipher.decrypt(ciphertext).decode()
        """
        Decrypts the message
        """
        print(translate("decrypted_message"), message)
    except ValueError as e:
        print(translate("decryption_failed"), e)
