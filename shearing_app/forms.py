from django import forms
from .models import Textshearing

class Shearing(forms.ModelForm):
    class Meta:
        model = Textshearing
        fields = ['title', 'text']


