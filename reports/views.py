from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from djgeojson.views import GeoJSONLayerView

from .models import Report

class ReportListView(ListView):
    model = Report
    template_name = 'report_list.html'

class ReportMapLayer(GeoJSONLayerView):
    model = Report
    properties = ('id', 'description')

