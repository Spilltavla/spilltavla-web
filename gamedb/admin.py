from gamedb.models import Game
from django.contrib import admin

class GameAdmin(admin.ModelAdmin):
    """
    Admin settings for a game
    """
    list_display = ('name', 'number_of_owners')

admin.site.register(Game, GameAdmin)
