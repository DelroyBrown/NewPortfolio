from django.db import models
import datetime

class WelcomePageVisitorName(models.Model):
    visitors_name = models.CharField(
        max_length=200, blank=True, null=True, default='')
    submit_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.visitors_name
