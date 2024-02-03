from myapp import models
from modeltranslation.translator import TranslationOptions, register

@register(models.Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'description')