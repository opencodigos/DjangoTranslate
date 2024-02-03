from django.contrib import admin
from myapp import models
from modeltranslation.admin import TranslationAdmin

@admin.register(models.Article)
class ArticleAdmin(TranslationAdmin):
    group_fieldsets = True # no admin esse separa por grupo
    list_display = ("title",)
    
    # class Media: # opcional só pra deixa bonito
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }