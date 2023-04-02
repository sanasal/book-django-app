from django import forms
from . import models 
from .models import Report_Issue


class Issue(forms.ModelForm):
    class Meta:
        model = models.Report_Issue
        fields = ['issue']