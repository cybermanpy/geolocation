from django.forms import ModelForm

from django import forms

from location.models import Position



class PositionForm(ModelForm):

	class Meta:

		model = Position

		fields = ('latitude', 'longitude', 'phone', 'count')
