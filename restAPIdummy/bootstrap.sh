#!/bin/sh
export FLASK_APP=index.py
source $(activate wordprocessing)
flask run -h 0.0.0.0