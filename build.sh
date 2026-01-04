#!/bin/bash

echo "Starting the build..."

#Creating venv if it does not exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/avtivate

echo "Installing requirements..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Deactivating virtual envronment..."
deactivate

echo "Giving run.sh excute permission..."
chmod +x run.sh

echo "Build complete !"

