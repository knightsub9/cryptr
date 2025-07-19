from decrypter import decrypter
from encrypter import encrypter

launcherSelection = input("Do you want to use the encrypter or the decrypter? (e/d): ").lower()

if launcherSelection == "e":
    Encrypter()

else:
    if launcherSelection == "d":
        Decrypter()

    else:
        print("Input invalid")
