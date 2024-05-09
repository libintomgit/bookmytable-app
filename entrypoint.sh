#!/bin/bash

# APP_PORT = ${PORT:-8000}

# cd /app/

# /opt/venv/bin/gunicorn bookmytable.wsgi:application --bind "0.0.0.0:"${APP_PORT}

# #--worker-temp-dir /dev/shm

APP_PORT=${APP_PORT:-8000}

# Run migrations (if applicable)
python manage.py migrate

# Start Django development server
python manage.py runserver 0.0.0.0:${APP_PORT}