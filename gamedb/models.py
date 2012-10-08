# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GameBase(models.Model):
    name = models.CharField(max_length=255, verbose_name='navn')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Beskrivelse')
    owners = models.ManyToManyField(User, null=True, blank=True,
                                    verbose_name='eiere',
                                    related_name='games_owned')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    release_year = models.IntegerField(blank=True, null=True,
                                       verbose_name='Utgivelsesår')
    #TODO: Add links to BGG, brettspill.no and similar
    def __unicode__(self):
        return self.name

    def number_of_owners(self):
        '''
        Returns the number of owners for the given game. This is used for
        listing games in the admin.

        See list_display in admin.py
        '''
        return len(self.owners.all())
    number_of_owners.short_description = 'antall eiere'

#class Game(GameBase):
class Game(models.Model):
#    similar_games = models.ManyToManyField('self', null=True, blank=True,
#                                           verbose_name='lignende spill')
    name = models.CharField(max_length=255, verbose_name='navn')

    class Meta:
        ordering = ['name']
        verbose_name = 'spill'
        verbose_name_plural = 'spill'

class NewClass(models.Model):
    name = models.CharField(max_length=255, verbose_name='navn')
    class Meta:
        ordering = ['name']
        verbose_name = 'spill2'
        verbose_name_plural = 'spill2'


class GameEdition(GameBase):
    edition_of = models.ForeignKey(Game, verbose_name='Spillutgave',
                                   related_name='editions')
class GameExpansion(GameBase):
    expands = models.ManyToManyField(Game, verbose_name='Utvider',
                                     related_name='expansions')

    class Meta:
        ordering = ['name']
        verbose_name = 'utvidelsespakke'
        verbose_name_plural = 'utvidelsespakker'
