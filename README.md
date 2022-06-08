# Tiketin-admin

## Start Project

``` shell
pip3 install django
django-admin startproject Tiketin
cd Tiketin
python3 startapp core
python3 migrate
python3 createsuperuser
```

## Modify settings.py

```py
# Tiketin/settings.py
# ...

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",    # Add this line
]
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': *database_name*,
        'USER': *user_database*,
        'PASSWORD': *password*,
        'HOST': *host*,
        'PORT': *port*,
    }
}
```

## App Directory

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
└── views.py
```

## Reference

[Customize Django Admin Python](https://realpython.com/customize-django-admin-python)
