from django.db import models

class DetectorRange(models.Model):
    ifo = models.CharField(max_length=10, db_index=True)
    start = models.BigIntegerField(db_index=True)
    stop = models.BigIntegerField(db_index=True)
    range = models.FloatField()
    
    class Meta:
        ordering = ['ifo', 'start']
        indexes = [
            models.Index(fields=['ifo', 'start', 'stop']),
        ]
    
    def __str__(self):
        return f"{self.ifo} [{self.start}-{self.stop}]: {self.range}"
