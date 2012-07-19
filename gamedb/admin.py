from gamedb.models import Game, GameExpansion
from django.contrib import admin

class GameAdmin(admin.ModelAdmin):
    '''
    Admin settings for a game
    '''
    list_display = ('name', 'number_of_owners')

class GameExpansionAdmin(admin.ModelAdmin):
    '''
    Admin settings for a game expansion
    '''
    list_display = ('name', 'number_of_owners')

admin.site.register(Game, GameAdmin)
admin.site.register(GameExpansion, GameExpansionAdmin)
