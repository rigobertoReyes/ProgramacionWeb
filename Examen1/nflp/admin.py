from django.contrib import admin

# Register your models here.
from nflp.models import Player,Team,Stadium

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Stadium)

