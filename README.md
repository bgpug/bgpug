BG PUG
=========
Required environment settings (fill in accordingly)
---------------------------------------------------
```bash
export DB_NAME='bgpug'
export DB_USER='postgres'
export DB_PASSWORD='password'
```

Optional environment settings (fill in accordingly)
---------------------------------------------------
```bash
export DEBUG=1  # or unset DEBUG

export DB_ENGINE='django.db.backends.postgresql_psycopg2'
export DB_HOST='localhost'
export DB_PORT='5432'

export ALLOWED_HOSTS='127.0.0.1 localhost'  # Required for DEBUG True

export MEDIA_ROOT='..' # If you need to change the default media files location
export STATIC_ROOT='..' # If you need to change the default static files location

export SECRET_KEY='secret_key' # Required for production cryptography
export RAVEN_CONFIG_DSN='..' # For DEBUG True
```


Bower requirements
------------------

```bash
./manage.py bower_install
```


Instructions for running in development
---------------------------------------

```bash
git clone
mkvirtualenv -p /usr/bin/python3.? bgpug
vim "$WORKON_HOME"/bgpug/bin/postactivate # export db variables, secret key, debug, etc.
workon bgpug
pip install -r requirements/dev.txt
./manage.py bower_install
createdb bgpug
./manage.py migrate
./manage.py runserver
```
