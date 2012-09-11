from django.contrib.auth.models import User
from django.db import models

class Invitation(models.Model):
    code = models.CharField(max_length=255, verbose_name='invitasjonskode',
                            primary_key=True)
    created_by = models.ForeignKey(User, verbose_name='laget av')
    usage_limit = models.IntegerField(default=1, verbose_name='bruksgrense',)
    valid_from = models.DateTimeField(verbose_name='gyldig fra', blank=True,
                                      null=True)
    valid_to = models.DateTimeField(verbose_name='gyldig til', blank=True,
                                    null=True)

    def __unicode__(self):
        return 'Invitasjon(%s)' % self.code

    def number_of_usages(self):
        '''
        Returns the number of owners for the given game. This is used for
        listing games in the admin.

        See list_display in admin.py
        '''
        return len(self.usages.all())
    number_of_usages.short_description = 'antall brukt'

    class Meta:
        ordering = ['-valid_to']
        verbose_name = 'Invitasjon'
        verbose_name_plural = 'Invitasjoner'

class InvitationUsage(models.Model):
    invitation = models.ForeignKey(Invitation, unique=True,
                                   related_name='usages',
                                   verbose_name='invitasjon')
    user = models.OneToOneField(User, verbose_name='bruker')
    date = models.DateTimeField(auto_now_add=True, verbose_name='bruksdato')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Invitasjonsbruk'
        verbose_name_plural = 'Invitasjonsbruk'