# Queue  Management

## Project Configuration

### 1. Creating virtual environment
```
python3.10 -m venv penv
```

Activate the environment:
```
. penv/bin/activate
```

### 2. Create the django project package

```
django-admin startproject ${project_name} ${dir}
```

### 3. Install the django package 

```
pip install django
```

### 4. Create the server

```
python manage.py runserver
```

### 5. Create an app to the existing project

```
django-admin startapp home
```

And add the app to the settings.py file under the INSTALLED_APPS

### Install djangorestframework

```
pip install djangorestframework
```
