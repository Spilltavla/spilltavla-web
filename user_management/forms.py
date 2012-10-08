# coding=utf-8
from django.utils.timezone import now
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from user_management.models import Invitation

def username_validator(value):
    if len(User.objects.filter(username=value)) > 0:
        raise ValidationError('Brukernavnet finnes allerede')

def invitation_validator(value):
    invitations = Invitation.objects.filter(code=value, valid_from__lte=now(),
                              valid_to__gte=now())
    if len(invitations)<1:
        raise ValidationError('Ugyldig invitasjonskode')
    invitation = invitations[0]
    if invitation.usage_limit != -1:
        if invitation.usage_limit < invitation.number_of_usages():
            raise ValidationError('Invitasjonskoden er allerede brukt opp')


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

