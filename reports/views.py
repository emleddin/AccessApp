from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from djgeojson.views import GeoJSONLayerView
from reports.forms import ReportForm

from .models import Report

class ReportListView(ListView):
    model = Report
    template_name = 'report_list.html'

class ReportMapLayer(GeoJSONLayerView):
    model = Report
    properties = ('id', 'description')

class ReportCreateView(CreateView):
    model = Report
    template_name = 'create_report.html'
    form_class = ReportForm
    success_url = '/'