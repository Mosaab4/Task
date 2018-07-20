#!/bin/bash

NAME="my_site"                                   # Name of the application
DJANGODIR=/media/mosaab/58BE837EBE835402/my_site               # Django project directory
SOCKFILE=/media/mosaab/58BE837EBE835402/venv/run/gunicorn.sock  # we will communicte using this unix socket
USER=mosaab                                         # the user to run as
GROUP=www-data                                        # the group to run as
NUM_WORKERS=3                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=my_site.settings      # which settings file should Django use
DJANGO_WSGI_MODULE=my_site.wsgi              # WSGI module name
echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $DJANGODIR
source /media/mosaab/58BE837EBE835402/task/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
