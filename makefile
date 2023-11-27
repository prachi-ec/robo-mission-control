.PHONY: migrations run celeryworker

migrations:
	cd roboapp/ && \
	python manage.py makemigrations && \
	python manage.py migrate

run:
	cd roboapp/ && \
	python manage.py runserver

celeryworker:
	cd roboapp/ && \
	celery -A roboapp worker --loglevel=info -P solo
