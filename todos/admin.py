from django.contrib import admin
from .models import Task
from django.contrib.auth.models import Group
# Register your models here.
admin.site.site_header = 'Admin Deshboard'

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','created')
    list_filter = ('created')

admin.site.register(Task)

admin.site.unregister(Group)