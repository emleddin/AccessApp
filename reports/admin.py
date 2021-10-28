from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Report

admin.site.register(Report, LeafletGeoAdmin)