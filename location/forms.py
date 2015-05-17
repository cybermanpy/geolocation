from django.forms import ModelForm, TextInput
from django import forms
from location.models import Position

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ('latitude', 'longitude', 'phone', 'count')
        widgets = {
            'count': TextInput(attrs={'type': 'hidden', 'value': '0'}),
            'latitude': TextInput(attrs={'type': 'hidden'}),
            'longitude': TextInput(attrs={'type': 'hidden'}),
        }