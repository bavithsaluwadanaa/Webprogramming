from django.contrib import admin
from .models import Module, Student

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "enrolment_date")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("modules",)
