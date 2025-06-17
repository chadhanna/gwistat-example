.PHONY: help reset import migrate runserver clean

help:
	@echo "Available targets:"
	@echo "  reset      - Clear all data from the database"
	@echo "  import     - Import data from test_data/range.csv"
	@echo "  migrate    - Run database migrations"
	@echo "  runserver  - Start the Django development server"
	@echo "  clean      - Remove generated CSV file"

test_data/range.csv:
	./test_data/scripts/fake_range > $@

reset:
	python test_data/scripts/reset_database.py

import: test_data/range.csv
	python manage.py import_ranges test_data/range.csv

migrate:
	python manage.py makemigrations
	python manage.py migrate

runserver:
	python manage.py runserver

clean:
	rm test_data/range.csv
