from django.contrib import admin

# Register your models here.
from .models import Profile, Skill

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'created')
    search_fields = ('user', 'name', 'email')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'created')
    search_fields = ('owner', 'name')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
