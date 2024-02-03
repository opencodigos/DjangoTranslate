from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Article(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'))
    city = models.CharField(_('City'), max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title