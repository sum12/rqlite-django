
django-rqlite
-------------

rqlite backend for django



INSTALL
=======
```
git clone https://github.com/sum12/rqlite-django
pip install ./rqlite-django
git clone https://github.com/sum12/pyrqlite -b djangofixes
#git clone https://github.com/rqlite/pyrqlite
pip install ./pyrqlite
```

USAGE
=====
in settings.py of your django
```python
DATABASES = {
    'default': {
        'ENGINE': 'rqlite.djangobackend',
        OPTIONS':{
            'host': 'localhost',    # default
            'port': 4001            # default
        }
    }
}
```
