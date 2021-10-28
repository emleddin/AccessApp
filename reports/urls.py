from django.urls import path
from .views import ReportListView, ReportMapLayer
from djgeojson.views import GeoJSONLayerView
from .models import Report 

urlpatterns = [
    #path('reports', ReportListView.as_view(), name='report_list'),
    path('', ReportMapLayer.as_view(), name='data')
]