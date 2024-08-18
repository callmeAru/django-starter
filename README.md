# django-starter
A simple Django project with home , user registration and login. Ideal for developers looking to learn basic Django setup and user authentication


# Project Structure:
Below is the structure of the project, organized into key folders and files:

flipkart/

├── .gitignore           
├── manage.py             
├── flipkart/            
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       
│   ├── urls.py           
│   ├── wsgi.py           
│
└── cartoon/              
    ├── __init__.py
    ├── admin.py         
    ├── apps.py          
    ├── backends.py      
    ├── models.py        
    ├── views.py          
    ├── tests.py          
    ├── migrations/        
    │
    └── templates/        
        ├── base.html
        ├── home.html
        ├── login.html
        └── register.html

# Getting Started with Django
## Django Project Setup Guide

A quick guide for setting up a Django project with Python and VS Code.

## Prerequisites

- **Python 3.x**: https://www.python.org/downloads/ (download the latest version. Follow the installation instructions)
- **Django**: Install via pip after setting up your virtual environment.

## Steps to Get Started

### 1. Set Up a Virtual Environment

- Navigate to your project directory in Terminal or Command Prompt.
- Create a virtual environment:

  ```bash
  python -m venv venv
  ```

- Activate the virtual environment:

  - **Windows**: `venv\Scripts\activate`
  - **macOS/Linux**: `source venv/bin/activate`

### 2. Install Django

- With the virtual environment activated, install Django:

  ```bash
  pip install django
  ```

### 3. Create a Django Project

- Start a new Django project:

  ```bash
  django-admin startproject myproject
  ```

  *(Replace `myproject` with your desired project name,for me it's flipkart)*

- Navigate into your project directory:

  ```bash
  cd myproject
  ```

### 4. Run the Development Server

- Start the server:

  ```bash
  python manage.py runserver
  ```

- Visit (http://127.0.0.1:8000/) in your browser to see the Django welcome page.

### 5. Create and Add a Django App

- Create a new app:

  ```bash
  python manage.py startapp myapp
  ```

  *(Replace `myapp` with your desired app name,for me it's cartoon)*

- Add your app to `INSTALLED_APPS` in `settings.py`.
   ```bash
     INSTALLED_APPS = [
       ...
       '''
       'myapp',   
   ]
   ```
### 6. Define Models, Views, and URLs

- Define your data models in `models.py`.
- Create views in `views.py`.
- Set up URLs in `urls.py`.

### 7. Apply Migrations

- Create and apply migrations:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### 8. Test Your Application

- Restart the server if needed and refresh the browser to see your changes.

### 9. Stop the Server

- Stop the server with `Ctrl+C` in Terminal or Command Prompt.

## Summary

- Install Python and Django.
- Set up a virtual environment.
- Create and run a Django project.
- Define models, views, and URLs to build your application.
