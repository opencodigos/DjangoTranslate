from django.shortcuts import render
from myapp import models
# Create your views here.
def mysite(request):
    posts = models.Article.objects.all()
    return render(request, 'home.html', {'posts': posts})