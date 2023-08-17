from django import forms
from .models import Subject
class Subject_Form(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['author', 'created_at', 'section']