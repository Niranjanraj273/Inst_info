#!/bin/bash

# Clear screen
clear

echo -e "\e[1;35m[*] Insta Info Tool Setup Starting...\e[0m"

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "\e[1;31m[!] Python3 not found. Installing Python3...\e[0m"
    pkg install python -y || apt install python3 -y
else
    echo -e "\e[1;32m[✓] Python3 is already installed.\e[0m"
fi

# Upgrade pip
echo -e "\e[1;34m[*] Upgrading pip...\e[0m"
pip install --upgrade pip

# Install required Python packages
echo -e "\e[1;34m[*] Installing required Python packages...\e[0m"
pip install instaloader rich pyfiglet

echo -e "\e[1;32m[✓] All dependencies installed successfully!\e[0m"
echo -e "\e[1;33m[>] Run the tool with: python3 your_script_name.py\e[0m"
# run
   python ig.py

