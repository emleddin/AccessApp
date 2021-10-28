from django.contrib.gis.db import models
import uuid
import datetime

class Report(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    
    geometry = models.PointField(geography=True) 
    description = models.TextField()
    date_added = models.DateTimeField(default=datetime.datetime.today,null=False,blank=False)
