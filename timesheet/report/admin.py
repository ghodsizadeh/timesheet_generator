from django.contrib import admin

# Register your models here.
from . import models

# admin.site.register(models.TimeSheet)
admin.site.register(models.Holidays)
@admin.register(models.TimeSheet)
class TimesheetAdmin(admin.ModelAdmin):
    fields = ('user', 'time')
    list_display =['user','time']

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    actions = [models.TimeSheet.creat_user_timesheet]
    list_display =['firstname','lastname','user_id']