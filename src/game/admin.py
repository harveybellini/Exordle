from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from auth.models import GameUser
from .models import Locations, Words, Guesses, Hints

class GameUserInline(admin.StackedInline):
    model = GameUser
    can_delete = False
    verbose_name_plural = 'gameuser'


class UserAdmin(BaseUserAdmin):
    inlines = (GameUserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register([Locations, Words, Guesses, Hints])

