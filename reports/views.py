from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView

from .models import Report

class ReportListView(ListView):
    model = Report
    template_name = 'report_list.html'



