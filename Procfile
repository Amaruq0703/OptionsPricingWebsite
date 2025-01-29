web: gunicorn options_pricing.wsgi --log-file -
release: python manage.py migrate
release: python manage.py collectstatic --noinput