#!/bin/sh

set -e

python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
DJANGO_SUPERUSER_PASSWORD=mySQLabcd0 python3 manage.py createsuperuser --username webadmin --email webadmin\@email.com --noinput

uwsgi --socket :8000 --master --enable-threads --module prodTasksProj.wsgi
