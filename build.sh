#!/usr/bin/env bash
set -o errexit  # Exit on first error

# Upgrade pip to avoid wheel/build issues
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
