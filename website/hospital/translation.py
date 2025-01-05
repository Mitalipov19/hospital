from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Doctor)
class ProductTranslationOptions(TranslationOptions):
    fields = ('qualifications','department')