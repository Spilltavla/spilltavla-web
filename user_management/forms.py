# coding=utf-8

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def username_validator(value):
    if len(User.objects.filter(username=value)) > 0:
        raise ValidationError('Brukernavnet finnes allerede')

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30,
                               validators=[username_validator],
                               label='Brukernavn')
    first_name = forms.CharField(label='Fornavn')
    last_name = forms.CharField(label='Etternavn')
    gender = forms.ChoiceField(choices=(('M', 'Mann'), ('F', 'Kvinne')),
                               label='Kjønn')
    birthday = forms.DateField(label='Fødselsdag')
    invitation_code = forms.CharField(label='Invitasjonskode')

