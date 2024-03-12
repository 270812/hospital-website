from django import forms
from .models import contactdata

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactdata
        fields = ['name', 'number', 'department', 'doctors', 'day']
