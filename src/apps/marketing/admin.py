from django.contrib import admin

from .models import DemoRequest


@admin.register(DemoRequest)
class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "company", "phone", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "email", "company", "message"]
    readonly_fields = ["created_at"]
    date_hierarchy = "created_at"