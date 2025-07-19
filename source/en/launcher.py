from decrypter import decrypter
from encrypter import encrypter

launcherSelection = input("Do you want to use the encrypter or the decrypter? (e/d): ").lower()
"""_summary_
"""

if launcherSelection == "e":
    encrypter()
    """_summary_
    """

else:
    if launcherSelection == "d":
        decrypter()
        """_summary_
        """

    else:
        print("Input invalid")
