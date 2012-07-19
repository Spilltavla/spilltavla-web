from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255, verbose_name='navn')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Beskrivelse')
    owners = models.ManyToManyField(User, null=True, blank=True,
                                    verbose_name='eiere',
                                    related_name='games_owned')
    disposers = models.ManyToManyField(User, null=True, blank=True,
                                       verbose_name='kan skaffes av',
                                       related_name='games_disposed')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    rules_known_by = models.ManyToManyField(User, null=True, blank=True,
                                            verbose_name='kan reglene',
                                            related_name='game_rules_known')
    similar_games = models.ManyToManyField('self', null=True, blank=True,
                                           verbose_name='lignende spill')
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'spill'
        verbose_name_plural = 'spill'
