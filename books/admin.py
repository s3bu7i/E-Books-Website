from django.contrib import admin
from .models import Ebook


@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'uploaded_at']
