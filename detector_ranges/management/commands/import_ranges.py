import csv
from django.core.management.base import BaseCommand
from detector_ranges.models import DetectorRange

class Command(BaseCommand):
    help = 'Import detector ranges from CSV file'
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    
    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        # Clear existing data
        DetectorRange.objects.all().delete()
        self.stdout.write('Cleared existing data')
        
        # Import new data
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            batch = []
            batch_size = 1000
            count = 0
            
            for row in reader:
                batch.append(DetectorRange(
                    ifo=row['ifo'].strip(),
                    start=int(row['start'].strip()),
                    stop=int(row['stop'].strip()),
                    range=float(row['range'].strip())
                ))
                
                if len(batch) >= batch_size:
                    DetectorRange.objects.bulk_create(batch)
                    count += len(batch)
                    self.stdout.write(f'Imported {count} records...')
                    batch = []
            
            # Import remaining records
            if batch:
                DetectorRange.objects.bulk_create(batch)
                count += len(batch)
            
            self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} records'))