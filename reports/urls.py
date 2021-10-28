from django.urls import path
from .views import ReportListView
from djgeojson.views import GeoJSONLayerView
from .models import Report 

urlpatterns = [
    #path('reports', ReportListView.as_view(), name='report_list'),
    path('', GeoJSONLayerView.as_view(model=Report), name='data')
]