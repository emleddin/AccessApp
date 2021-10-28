from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from djgeojson.views import GeoJSONLayerView
from reports.forms import ReportForm

from django.contrib.gis.geos import Point

from .models import Report

class ReportListView(ListView):
    model = Report
    template_name = 'report_list.html'

class ReportMapLayer(GeoJSONLayerView):
    model = Report
    properties = ('id', 'description')

class ReportCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        lat = request.GET['lat']
        lon = request.GET['lon']

        if lat and lon:
            initial_data = {
                'geom' : Point([float(lon), float(lat)], srid=4326) #xy
            }

        form = ReportForm(initial=initial_data)
        context = {
            'form' : form
        }
        return render(request, "create_report.html", context)

    model = Report
    template_name = 'create_report.html'
    form_class = ReportForm
    success_url = '/'

    