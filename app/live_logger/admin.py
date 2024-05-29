from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('ip', 'city', 'region', 'country', 'loc', 'org', 'postal', 'timezone', 'bogon', 'success')

@admin.register(models.Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'location', 'user', 'start_time', 'end_time')

    @admin.display()
    def endpoint(self, obj):
        return obj.meta['PATH_INFO']
    