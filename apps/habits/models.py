from django.db import models


class Habit(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    start_at = models.DateTimeField(blank=True)
    end_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """ Habit representation as string """
        return self.title