#!/bin/bash

# Define alias-line
ALIAS_LINE='alias cryptr='python3 ~/.pyapps/cryptr/launcher.py'

# Check if alias already exists
if ! grep -Fxq "$ALIAS_LINE" ~/.bashrc; then
  echo "$ALIAS_LINE" >> ~/.bashrc

fi

mkdir -p ~/.pyapps/cryptr
cp -r ./* ~/.pyapps/cryptr/
cd ~/.pyapps/cryptr
rm ~/.pyapps/cryptr/install.sh
