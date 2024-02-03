# Django: Internacionalização dos Modelos

Como internacionalizar seus modelos no Django. No caso vou fazer do PT-BR e EN. 
Mas com base na configuração que vou passar pra vocês podem fazer com quantos idiomas quiser. Não tem limite!...Vamos utilizar bibliotecas nativas do Django e uma biblioteca nova django-modeltranslation.

Vamos partir desse projeto anteriror [Link](https://www.youtube.com/watch?v=B0urbukze04&t=0s)

Vídeo Tutorial [Link](https://www.youtube.com/watch?v=kkyAi6-s6J4)

Vamos utilizar projeto do vídeo anterior. 
***Baixar Projeto anterior***

```python
https://github.com/djangomy/django-translate.git
```
  
Vamos utilizar uma biblioteca.

`pip install django-modeltranslation`

Documentação: [https://pypi.org/project/django-modeltranslation/](https://pypi.org/project/django-modeltranslation/)

<details><summary><b>Configurar no Settings</b></summary>

- **Configurar no Settings**
    
    Acessar o *core/settings.py*
    
    ```python
    INSTALLED_APPS = [
    	 	'modeltranslation', # adicionar em primeiro
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles', 
        'mysite_app',
    ]
    ```
    
    ```python
    # Internationalization
    
    MODELTRANSLATION_DEFAULT_LANGUAGE = 'pt-br'
    
    MODELTRANSLATION_LANGUAGES = ('pt-br', 'en')
    ```

</details>

<details><summary><b>Criando Modelo</b></summary>

- **Criando Modelo**
    
    ***mysite_app/models.py***
    
    Quando colocamos **_('Title')**. Esse _ está definindo que essa Label também será traduzida. 
    
    ```python
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
    ```
    
    criar arquivo ***mysite_app/translation.py***
    
    Esses *fields* são os campos que receberam a tradução. Coloque somente os campos que serão traduzidos.
    
    ```python
    from mysite_app import models
    from modeltranslation.translator import TranslationOptions, register
    
    @register(models.Article)
    class ArticleTranslationOptions(TranslationOptions):
        fields = ('title', 'description')
    ```
    
    ***mysite_app/admin.py***
    
    Nosso modelo registrado no admin. Essa ***class Media*** é opcional**.**
    
    ```python
    from django.contrib import admin
    from mysite_app import models
    from modeltranslation.admin import TranslationAdmin
    
    @admin.register(models.Article)
    class ArticleAdmin(TranslationAdmin):
    		group_fieldsets = True # no admin esse separa por grupo
        list_display = ("title",)
        class Media: # opcional só pra deixa bonito
            js = (
                'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
            }
    ```
    
    Vamos rodar aplicação e acessar o Django Admin
    
    ```python
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver
    ```
    
    No Django Admin estará assim. como definimos `group_fieldsets = True` fica uma faixa azul separando os grupos de campos que precisa ser traduzido. O Class Media deixa essas Aba com visual legal.
    
    Outra observação.
    
    `django-admin makemessages --all --ignore=env`
    
    Como no modelo colocamos a *label* em inglês então nas mensagens *br* vamos traduzir para português.
    
    ***locale/br/LC_MESSAGES/django.po***
    
    ```python
    #: mysite_app/models.py:6
    msgid "Title"
    msgstr "Titulo"
    
    #: mysite_app/models.py:7
    msgid "Description"
    msgstr "Descrição"
    ```
    
    Nas mensagens em *en* é só manter. 
    
    ***locale/en/LC_MESSAGES/django.po***
    
    ```python
    #: mysite_app/models.py:6
    msgid "Title"
    msgstr "Title"
    
    #: mysite_app/models.py:7
    msgid "Description"
    msgstr "Description"
    ```

</details>

<details><summary><b>Lista Artigos na Home</b></summary>

- **Lista Artigos na Home**
    
    No template vamos listar os artigos. Para isso precisamos adicionar na view o context e renderizar na home os objetos.
    
    *mysite_app/views.py*
    
    ```python
    from django.shortcuts import render
    from mysite_app import models
    # Create your views here.
    def mysite(request):
        posts = models.Article.objects.all()
        return render(request, 'home.html', {'posts': posts})
    ```
    
    *mysite_app/home.html*
    
    ```python
    {% load i18n %}
    <!doctype html>
    <html lang="en">
    
    <head>
    	<meta charset="utf-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1">
    	<title>Translation</title>
    	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
    	integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    </head>
    
    <body> 
    
    	<div class="container">
    		
    		<a href="{% url 'set-language' 'pt-br' %}">BR</a>
    
    		<a href="{% url 'set-language' 'en' %}">EN</a>
    
    		<h1>{% trans 'Testando Biblioteca para Tradução de Site' %}</h1>
    
    		<p>{% trans 'Para tornar um projeto Django traduzível, você deve adicionar um número mínimo de ganchos ao seu código e modelos' %}</p>
    
    		<div class="row gap-2">
    
    			{% for post in posts %} # Adiciona for para lista os Artigos
    			<div class="card p-3">
    				<h2>{% trans post.title %}</h2>
    				<p>{% trans post.description|truncatechars:200 %}</p>
    			</div>
    			{% endfor %}
    			
    		</div>
    	 
    	</div>
     
    	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
    		integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
    		crossorigin="anonymous"></script>
    
    </body>
    
    </html>
    ``` 

</details>

