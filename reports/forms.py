from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {'geom' : LeafletWidget()}
