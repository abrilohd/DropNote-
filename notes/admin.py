from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "updated_at")
    list_filter = ("category",)
    search_fields = ("title", "content")