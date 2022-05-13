from modeltranslation.translator import register, TranslationOptions
from .models import Blog

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('header', 'text', 'link',)