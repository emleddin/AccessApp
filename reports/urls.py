from django.urls import path
from .views import home_page_view, ReportListView, ReportAPIView

urlpatterns = [
    path('', home_page_view, name='home'),
    #path('reports', ReportListView.as_view(), name='report_list'),
    path('reports/', ReportAPIView.as_view())
]