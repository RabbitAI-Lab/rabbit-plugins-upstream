#!/bin/sh
# entrypoint.sh for Django containers
set -e

echo "Running database migrations..."
python manage.py migrate --noinput 2>/dev/null || echo "Migration skipped or failed"

echo "Starting Django server on 0.0.0.0:${PORT:-8000}..."
exec python manage.py runserver 0.0.0.0:${PORT:-8000}
