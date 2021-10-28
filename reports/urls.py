from django.urls import path
from .views import ReportCreateView, ReportListView, ReportMapLayer
from djgeojson.views import GeoJSONLayerView
from .models import Report 

urlpatterns = [
    #path('reports', ReportListView.as_view(), name='report_list'),
    path('', ReportMapLayer.as_view(), name='data'),
    path('new/', ReportCreateView.as_view(), name='new_report'),

]