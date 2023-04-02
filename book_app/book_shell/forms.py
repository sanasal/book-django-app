from django import forms
from . import models 
from .models import Add_Comment


class Comment(forms.ModelForm):
    class Meta:
        model  = models.Add_Comment
        fields = ['comment']