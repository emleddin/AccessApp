from django.contrib.gis.db import models
import uuid
import datetime

class Report(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('REVIEW', 'Under Review'),
        ('ACCEPTED', 'Accepted'),
        ('CLOSED', 'Resolved')
    ]

    id = models.AutoField(primary_key=True)
    
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='NEW')

    geom = models.PointField(geography=True) 
    description = models.TextField()
    date_added = models.DateTimeField(default=datetime.datetime.today,null=False,blank=False)
