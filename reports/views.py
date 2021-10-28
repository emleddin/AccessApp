from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView

from rest_framework import generics

from .models import Report
from .serializers import ReportSerializer

class ReportListView(ListView):
    model = Report
    template_name = 'report_list.html'

class ReportAPIView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

def home_page_view(request):
    return HttpResponse('Hello, World!')