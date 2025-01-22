from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title', 'description')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('value', 'body','created')
    search_fields = ('value', 'body')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Review, ReviewAdmin)

