#!/bin/bash

#ensure python is installed 

echo "Running the app"
APP_FILE="main.py"

if ! command -v python3 &> /dev/null; then
    echo "Python is not installed!"
    exit 1
fi

if [ ! -f "$APP_FILE" ]; then 
    echo "Error: main.py not found."
fi

if [ ! -d "venv" ]; then    
    echo "Error: venv not found. Run build.sh first."
    exit 1
fi

source venv/bin/activate

python3 "$APP_FILE"
