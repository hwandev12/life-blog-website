from django.contrib import admin
from .models import Blog
from modeltranslation.admin import TranslationAdmin

@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('header',)}

