from dataclasses import fields
from django import forms

class RegistrationForm(forms.Form):
        fields = forms.EmailField(label='Your email')
