from django.contrib import admin
from .models import Team,Team_members

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name','slug')
    prepopulated_fields = {'slug':('team_name',)}

class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name','designation','team','social_link_1','social_link_2','social_link_3')


admin.site.register(Team,TeamAdmin)
admin.site.register(Team_members,TeamMembersAdmin)