from django.db import models

class TimeSlot(models.Model):
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50, blank=True)

    def _str_(self):
        return self.subject_name