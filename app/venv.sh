#!/bin/bash

# Create a virtual environment named "luxe"
python3 -m venv luxe

# Activate the virtual environment
source luxe/bin/activate

# Install the required dependencies from the requirements file
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

echo "Virtual environment 'luxe' created and dependencies installed."
 
# RUN: chmod +x create_venv.sh
