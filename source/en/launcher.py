from decrypter import Decrypter
from encrypter import Encrypter

launcherSelection = input("Do you want to use the encrypter or the decrypter? (e/d): ").lower()

if launcherSelection == "e":
    Encrypter()

else:
    if launcherSelection == "d":
        Decrypter()

    else:
        print("Input invalid")
