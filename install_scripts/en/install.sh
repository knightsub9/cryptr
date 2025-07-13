#!/bin/bash

# Define alias-line
ALIAS_LINE='alias cryptr='python3 ~/.pyapps/cryptr/launcher.py'

# Check if alias already exists
if ! grep -Fxq "$ALIAS_LINE" ~/.bashrc; then
  echo "$ALIAS_LINE" >> ~/.bashrc

fi

mkdir -p ~/.pyapps/cryptr
cd ~/.pyapps/cryptr
curl lorem.ipsum/domain/cryptr.tar
tar -xf cryptr.tar
rm cryptr.tar
