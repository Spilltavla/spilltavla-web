from user_management.models import Invitation, InvitationUsage
from django.contrib import admin

class InvitationAdmin(admin.ModelAdmin):
    '''
    Admin settings for a game
    '''
    list_display = ('code', 'created_by', 'usage_limit', 'number_of_usages',
                    'valid_from', 'valid_to')

class InvitationUsageAdmin(admin.ModelAdmin):
    '''
    Admin settings for a game expansion
    '''
    list_display = ('invitation', 'user', 'date')

admin.site.register(Invitation, InvitationAdmin)
admin.site.register(InvitationUsage, InvitationUsageAdmin)
