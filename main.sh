#!/bin/bash

ORIG_DIR=$(pwd)
cd "$(dirname "$0")" || exit 1
pip install -r requirements.txt > /dev/null 2>&1
echo "Dependency installation was successful!"
echo Repo: https://github.com/dinarovv/ip_collector
read -p "Press [Enter] to continue..."
clear
python3 main.py
clear
cd "$ORIG_DIR" || exit 1
exit 0