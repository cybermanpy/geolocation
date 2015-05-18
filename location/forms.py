from django.forms import ModelForm, TextInput
from django import forms
from .models import Position

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ('latitude', 'longitude', 'phone', 'count')
        widgets = {
            'count': TextInput(attrs={'type': 'hidden', 'value': '0'}),
            'latitude': TextInput(attrs={'type': 'hidden'}),
            'longitude': TextInput(attrs={'type': 'hidden'}),
        }
class VideoDown(forms.Form):
	link = forms.CharField(label='Video link', max_length=500)
	path = forms.CharField(label='Path video download', max_length=500)