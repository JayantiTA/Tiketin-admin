# Tiketin-admin

## Start Project

``` shell
pip3 install django
pip3 install django-environ
django-admin startproject Tiketin
cd Tiketin
python3 startapp core
python3 migrate
python3 createsuperuser
```

## App Directory

The core app directory will start with the following files inside:

```
core/
│
├── migrations/
│   └── __init__.py
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
├── .env.example
└── .env
```

## Set Up Environment Variables

Create file named `.env` that contains database environment variables, refer to `.env.example` file.

## Run Server

Run the Django development server using:

```shell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Reference

[Customize Django Admin Python](https://realpython.com/customize-django-admin-python)
