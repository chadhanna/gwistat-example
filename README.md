# gwistat-example

A Django web application for querying gravitational wave detector operational status and sensitivity ranges at specific GPS times.

## Overview

This application allows users to query the operational status of gravitational wave detectors (H1, L1, V1, K1) at any given GPS time. It displays whether each detector was operational and, if so, what its sensitivity range was in Megaparsecs (Mpc).

## Features

- Query detector status by GPS time
- View detector operational status (On/Off/Unknown)
- Display sensitivity ranges for operational detectors
- Bootstrap-based responsive UI
- Bulk data import from CSV files
- Database management utilities

## Requirements

- Python 3.8+
- Django 4.2+

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd gwistat-example
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run database migrations:
```bash
make migrate
# or manually:
python manage.py makemigrations
python manage.py migrate
```

4. Generate and import sample data:
```bash
make import
# This will generate test_data/range.csv if it doesn't exist
# and import it into the database
```

## Usage

1. Start the development server:
```bash
make runserver
# or manually:
python manage.py runserver
```

2. Open your browser and navigate to http://127.0.0.1:8000/

3. Enter a GPS time in the search box (e.g., 1434001500)

4. View the results showing:
   - Which detectors were operational
   - Their sensitivity ranges in Mpc
   - "Unknown" for detectors with no data at that time

## Makefile Commands

- `make help` - Show available commands
- `make migrate` - Run database migrations
- `make import` - Generate sample data (if needed) and import to database
- `make reset` - Clear all data from the database
- `make runserver` - Start the Django development server
- `make clean` - Remove generated CSV file

## Project Structure

```
gwistat-example/
├── detector_ranges/          # Django app for detector range queries
│   ├── models.py            # DetectorRange model
│   ├── views.py             # Query view logic
│   ├── templates/           # HTML templates
│   └── management/          # Import command
├── gwistat_project/         # Django project settings
├── test_data/               # Sample data and scripts
│   ├── scripts/             # Data generation and reset scripts
│   └── range.csv            # Generated sample data
├── manage.py                # Django management script
├── Makefile                 # Convenience commands
└── requirements.txt         # Python dependencies
```

## Data Format

The CSV data format for importing detector ranges:
```csv
ifo, start, stop, range
H1, 1434000000, 1434001000, 0
H1, 1434001000, 1434002200, 97.25756048982008
...
```

- `ifo`: Interferometer name (H1, L1, V1, K1)
- `start`: GPS start time of the segment
- `stop`: GPS stop time of the segment
- `range`: Sensitivity range in Mpc (0 indicates detector was off)

## Development

To reset the database and reimport data:
```bash
make reset
make import
```

To import your own data:
```bash
python manage.py import_ranges path/to/your/data.csv
```