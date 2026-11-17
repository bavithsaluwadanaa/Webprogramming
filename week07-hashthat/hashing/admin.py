from django.contrib import admin
from .models import HashRecord

@admin.register(HashRecord)
class HashRecordAdmin(admin.ModelAdmin):
    list_display = ("digest", "created_at")
    search_fields = ("digest", "text")
