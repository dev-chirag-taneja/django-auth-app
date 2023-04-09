<h1>Django Authentication App</h1>

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2.12-brightgreen.svg)](https://djangoproject.com)

## Features
```
- Register, Login, Logout
- Change & Reset Password
- Account Activation
``` 

## Tech Stack
```
# Frontend   
- Html, Bootstrap

# Backend    
- Python, Django

# Database   
- Sqlite
```


## Installation
```
# Clone the Repo
- git clone https://github.com/dev-chirag-taneja/django-auth-app.git

# Go to directory
- cd django-auth-app

# Create a virtual environment
- python -m virtualenv env

# Activate the virtual environment
- source env/bin/activate

# Install the required dependency
- pip install -r requirements.txt

# Configure .env
- Rename env.example file to .env
- Put your credentials.

SECRET_KEY=
DEBUG=
EMAIL_HOST=
EMAIL_USE_TLS=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

# Make migrations
- python manage.py migrate

# Create superuser
- python manage.py createsuperuser

# Run the server
- python manage.py runserver
```

--- 

<p align="center">Made with ❤️ and Python</p>
