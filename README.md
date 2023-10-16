# Queue  Management

## Project Configuration

### Create virtual environment
```
python3.10 -m venv penv
```

Activate the environment:
```
. penv/bin/activate
```

### Create the django project package

```
django-admin startproject ${project_name} ${dir}
```

### Install the django package 

```
pip install django
```

### Create the server

```
python manage.py runserver
```

### Create an app to the existing project

```
django-admin startapp home
```

And add the app to the settings.py file under the INSTALLED_APPS

### Install djangorestframework

```
pip install djangorestframework
```

### Create Templates

Create a folder called template inside the app folder and have the same name as app like below. Include all html files inside there.

home/template/home/index.html


### Database changes

Apply db migrations,

```
python manage.py migrate
```

Create superuser,

```
python manage.py createsuperuser
```

### Django shell commands

Import Tables,

```
from home.models import Service, Counter
```

Get all rows,

```
Counter.objects.all()
```

Get a specific row,

```
Counter.objects.get(pk=1)
```

Create Service instance,

```
Service.objects.create(service_id=1, service_name='ServiceA')
```

Fetch the row,

```
srv_ins = Service.object.get(pk=1)
```

Create Counter instance,

```
Counter.objects.create(counter_id=1, service_id=srv_ins, status='open')
```

Filter the row,

```
Service.objects.filter(service_name__endswith="B")
```

Search the row,

```
Service.objects.filter(service_name__icontains="srv")
```

```
Service.objects.exclude(service_name__icontains="B")
```

