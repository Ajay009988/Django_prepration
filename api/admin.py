from django.contrib import admin
from . models import Employee,Student


@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','city','salary','email']
    search_fields=['name']

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','subject','fees','location']
    search_fields=['name']