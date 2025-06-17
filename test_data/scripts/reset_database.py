#!/usr/bin/env python
"""
Reset the database by clearing all detector range data.
"""
import os
import sys
import django

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwistat_project.settings')
django.setup()

from detector_ranges.models import DetectorRange

def reset_database():
    print("Resetting database...")
    
    # Clear all detector range data
    count = DetectorRange.objects.count()
    DetectorRange.objects.all().delete()
    print(f"Deleted {count} records from database")
    
    # Verify database is empty
    remaining = DetectorRange.objects.count()
    if remaining == 0:
        print("Database reset complete. All detector ranges cleared.")
    else:
        print(f"Warning: {remaining} records still remain in database.")

if __name__ == '__main__':
    reset_database()