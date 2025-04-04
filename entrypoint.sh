#!/usr/bin/env sh

cd lawproject
python manage.py migrate
gunicorn lawproject.wsgi --bind 0.0.0.0:8000