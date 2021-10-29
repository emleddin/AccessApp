from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Report

#admin.site.register(Report)

@admin.register(Report)
class ReportAdmin(LeafletGeoAdmin):
    list_display = ['description', 'status', 'date_added', ]