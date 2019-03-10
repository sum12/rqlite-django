django-rqlite
-------------

(UNTESTED) rqlite backend for django

untested: because django has a huge list of features for sqlite
which cannot be tested. [further](#missing-functionality)
)

INSTALL
=======
```
git clone https://github.com/sum12/rqlite-django
pip install ./rqlite-django
git clone https://github.com/rqlite/pyrqlite
pip install ./pyrqlite
```

USAGE
=====
in settings.py of your Django
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
Missing Functionality
=====================
Django has a huge number of functions added on top of plain SQLite,
to provide advanced manipulations have a look [here](https://github.com/django/django/blob/142e1ead76fd452dc9bca0ab0f12bad56a116fb5/django/db/backends/sqlite3/base.py#L194), these
function cannot be used anymore as they are no longer available in `go`.

For more information: https://github.com/rqlite/rqlite/pull/523
