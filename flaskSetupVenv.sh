#!/bin/bash

# install pytest
pip install pytest

# Create virtual environment
python3 -m venv flask

# Activate virtual environment
source flask/bin/activate

# Install dependencies
flask/bin/pip install flask 
flask/bin/pip install flask-login 
flask/bin/pip install flask-mail 
flask/bin/pip install flask-sqlalchemy 
flask/bin/pip install flask-migrate 
flask/bin/pip install flask-whooshalchemy 
flask/bin/pip install flask-wtf 
flask/bin/pip install flask-bcrypt
flask/bin/pip install flask-babel 
flask/bin/pip install coverage 

export FLASK_APP=run.py
export FLASK_DEBUG=1

# Confirm completion
echo "Virtual environment setup complete. Use 'source flask/bin/activate' to activate."
