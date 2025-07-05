from django import forms
from .models import Booking
from django.core.exceptions import ValidationError
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }