from email.headerregistry import Group
from django.contrib import admin
from .models import Student
from django.contrib.auth.models import Group

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name')
    list_filter = ('roll_no','CG', 'FDS', 'OOP')
    search_fields = ('name__startswith', 'roll_no__startswith' )
    admin.site.site_header = "Admininstrative Portal"
    
    
admin.site.register(Student, StudentAdmin)
admin.site.unregister(Group)





