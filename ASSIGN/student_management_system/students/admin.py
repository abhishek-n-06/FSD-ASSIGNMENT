from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'course', 'email', 'date_of_birth')
    search_fields = ('name', 'roll_number', 'course', 'email')

admin.site.register(Student, StudentAdmin)
