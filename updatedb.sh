#!/bin/bash

./manage.py makemigrations blog
./manage.py migration blog
./manage.py syncdb
