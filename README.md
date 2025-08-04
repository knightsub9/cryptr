# Cryptr

Cryptr is a Python-project for encrypting and decrypting text in a terminal with AES. It's supposed to be easy to use, so that anyone can encrypt and/or decrypt messages using Cryptr.

## Requirements

You need to have [Python 3.13](https://www.python.org/downloads/) and [Cryptography](https://pypi.org/project/cryptography/) installed on your device.
Cryptograhpy usually comes with Python.
If you are unsure if you installed Python or not, check on Windows using `winget list`, on Linux using your package manager (e. g. `apt list --installed` if you're using apt) or the GUI.
On MacOS you can use `pkgutil --pkgs` or another command, depending on how you installed Python.

To check if you have Cryptography installed, use the command `pip list` if you have pip installed, otherwise use the GUI (search for 'python-cryptography') or your package manager (e. g. `pacman -Ss python-cryptography` when using Pacman).

### Install Python and Cryptography

To install Python and Cryptography, you can either use the terminal, the GUI, or you can download them from [PyPi (Cryptography)](https://pypi.org/project/cryptography/) or [Python.org](https://python.org/downloads/).

#### Windows

On Windows, use the command `winget install Python.Python.3.13` to install Python.
Cryptography will be delivered wih Python.

#### Linux

When using apt, you need to use `sudo apt install python3.13` to install Python.
When using Pacman, you need to use `sudo pacman -S python` to install Python.
You will be asked to enter your password.

#### MacOS

Python 3 should be preinstalled, check using `python3 --version` in the terminal.

## Install Cryptr

### Linux & MacOS

1. Download the Tarball (file ending is .tar) from the releases page on Github.

2. Untar the Tarball, but keep all the extracted files in the same folder, but make sure that there aren't any other files/folders in the folder.

3. Run the `install.sh` using `install.sh`, `./install.sh` or `exec install.sh` whilst in the folder with the extracted files.

4. Close and reopen the terminal after the installation finished.

5. You can now start Cryptr using the command `cryptr`.

### Windows

1. Download the ZIP (file ending is .zip) from the releases page on Github.

2. Unzip the ZIP, but keep all the extracted files in the same folder, but make sure there aren't any other files/folders in the folder.

3. Run the `install.bat` using `install.bat` whilst in the folder with the extracted files or use the file explorer.

4. If you used the terminal, close and reopen the terminal after the installation finished.

5. You can now start Cryptr using the command `cryptr`.
