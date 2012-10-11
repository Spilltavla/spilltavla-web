from gamedb.models import Game, GameExpansion, GameEdition
from django.contrib import admin

class GameAdmin(admin.ModelAdmin):
    '''
    Admin settings for a game
    '''
    list_display = ('name',)

class GameEditionAdmin(admin.ModelAdmin):
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
admin.site.register(GameEdition, GameEditionAdmin)
