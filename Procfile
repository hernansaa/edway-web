web: python src/manage.py migrate --noinput && python src/manage.py collectstatic --noinput && gunicorn config.wsgi --pythonpath src --bind 0.0.0.0:$PORT --workers 3 --threads 2
