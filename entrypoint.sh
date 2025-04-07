#!/usr/bin/env sh

cd lawproject
python manage.py migrate
python manage.py loaddata fixtures/hardcode.json
gunicorn lawproject.wsgi --bind 0.0.0.0:8000