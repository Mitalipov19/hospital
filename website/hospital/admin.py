from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from .translation import *

@admin.register(Doctor)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Appointments)
admin.site.register(MedicalRecord)
admin.site.register(Feedback)