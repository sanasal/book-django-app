from django import forms
from . import models 
from .models import Add_Comment

#Form for add a user review about us 
class Comment(forms.ModelForm):
    class Meta:
        model  = models.Add_Comment
        fields = ['comment']