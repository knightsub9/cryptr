from decrypter import decrypter
from encrypter import encrypter

launcherSelection = input("Do you want to use the encrypter or the decrypter? (e/d): ").lower()
"""
Asks user what variable to use.
"""

if launcherSelection == "e":
    encrypter()

else:
    if launcherSelection == "d":
        decrypter()

    else:
        print("Input invalid")
