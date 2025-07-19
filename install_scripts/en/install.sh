#!/bin/bash

# Define alias-line
ALIAS_LINE='alias cryptr='python3 ~/.pyapps/cryptr/launcher.py'

# Check if alias already exists
if ! grep -Fxq "$ALIAS_LINE" ~/.bashrc; then
  echo "$ALIAS_LINE" >> ~/.bashrc

fi

mkdir -p ~/.pyapps/cryptr
cd ~/.pyapps/cryptr
curl lorem.ipsum/domain/cryptr_linux.tar
tar -xf cryptr_linux.tar
rm cryptr_linux.tar
