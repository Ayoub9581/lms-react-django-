release: npm run build
release: python manage.py migrate --run-syncdb
web: gunicorn home.wsgi --log-file -