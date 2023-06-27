from django import forms
from . import models 
from .models import Report_Issue


#Form to let user tell us about his problems in our site
class Issue(forms.ModelForm):
    class Meta:
        model = models.Report_Issue
        fields = ['issue']