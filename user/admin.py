from django.contrib import admin
from user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    List_display = ('user', 'agre', 'image')
    list_friends = ('user',)
