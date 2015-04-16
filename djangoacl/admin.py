from django.contrib import admin
from .models import Action


class ActionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('users', 'groups')

admin.site.register(Action, ActionAdmin)
