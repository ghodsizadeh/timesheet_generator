from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.User)
# admin.site.register(models.TimeSheet)
admin.site.register(models.Holidays)
@admin.register(models.TimeSheet)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('user', 'time')
    list_display =['user','time']

