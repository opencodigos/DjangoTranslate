# Django Internacionalização PT-BR para EN

Configuração do projeto django para internacionalização. No caso fiz do PT-BR e EN. 
Utilizei bibliotecas nativas do Django para fazer essa configuração.

Vídeo Tutorial [Link](https://www.youtube.com/watch?v=B0urbukze04)

Instalar *gettext-iconv*

```python
**Linux**
sudo apt install gettext
```

```python
**Windows**
[https://mlocati.github.io/articles/gettext-iconv-windows.html](https://mlocati.github.io/articles/gettext-iconv-windows.html)
```

**Configurações Iniciais**

<details><summary><b>Ambiente Virtual Linux/Windows</b></summary>

- **Ambiente Virtual Linux/Windows**
     
    Lembrando… Precisa ter Python instalado no seu ambiente.
    
    **Criar o ambiente virtual Linux/Windows**
    
    ```python
    ## Windows
    python -m venv .venv
    source .venv/Scripts/activate # Ativar ambiente
    
    ## Linux 
    ## Caso não tenha virtualenv. "pip install virtualenv"
    virtualenv .venv
    source .venv/bin/activate # Ativar ambiente
    ```
    
    Instalar os seguintes pacotes.
    
    ```python
    pip install django
    ```
    
    Para criar o arquivo *requirements.txt*
    
    ```python
    pip freeze > requirements.txt
    ```
</details>

<details><summary><b>Criando o Projeto</b></summary>

- **Criando o Projeto**
    
    ## **Criando o projeto**
    
    “core” é nome do seu projeto e quando colocamos um “.” depois do nome do projeto significa que é para criar os arquivos na raiz da pasta. Assim não cria subpasta do projeto.
    
    ```python
    django-admin startproject core .
    ```
    
    **Testar a aplicação**
    
    ```python
    python manage.py runserver
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b413a084-7ed1-4480-a648-5049cebeba61/Untitled.png)
</details>

<details><summary><b>Criando Aplicativo</b></summary>
    
- **Criando Aplicativo**
    
    **Vamos criar nosso aplicativo no Django.**
    
    Para criar a aplicação no Django rode comando abaixo. “mysite_app” é nome do seu App.
    
    ```python
    python manage.py startapp mysite_app
    ```
    
    Agora precisamos registrar nossa aplicação no *INSTALLED_APPS* localizado em *settings.py*.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/99f24935-a25d-4e80-b2ab-44adc8cd1baf/Untitled.png)
</details>

<details><summary><b>Configura Arquivos Static</b></summary>
    
- **Configura Arquivos Static**
    
    ## **Vamos configurar nossos arquivos** *static*
    
    ```python
    import os 
    
    # base_dir config
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
    STATIC_DIR=os.path.join(BASE_DIR,'static')
    
    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
        }
    }
    
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    STATIC_URL = '/static/' 
    
    MEDIA_ROOT=os.path.join(BASE_DIR,'media')
    MEDIA_URL = '/media/'
    ```
    
    *core/urls.py*
    
    ```python
    from django.contrib import admin
    from django.conf import settings
    from django.conf.urls.static import static
    from django.urls import path
    
    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto
    ```
</details>

<details><summary><b>Configuração no Settings</b></summary>
    
- **Configuração no Settings**
    
    
    *core/settings.py*
    Para Português Brasil
    
    ```python
    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    ```
    
    ```python
    from django.utils.translation import gettext_lazy as _
    
    LANGUAGES = (
        ('pt-br', _('Portuguese')),
        ('en', _('English')),
    )
    ```
    
    ```python
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware', # Adiciona
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```
    
    ```python
    LOCALE_PATHS = [os.path.join(BASE_DIR,'locale'),]
    ```
</details>

<details><summary><b>Template e Bootstrap Configuração</b></summary>
    
- **Template e Bootstrap Configuração**
    
    No app *mysite_app* criar pasta templates e arquivo *templates*/*home.html*
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4de5df36-2e7d-401e-8040-7f6bdcb4511e/Untitled.png)
    
    ## Bootstrap configuração
    
    Doc: [https://getbootstrap.com/docs/5.2/getting-started/introduction/](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
    
    Com Base na documentação para utilizar os recursos Boostrap basta adicionar as tags de CSS e JS. No HTML da Pagina Base.
    
    ```python
    <!-- CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    
    <!-- JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    ```
    
    *templates*/home.html
    
    Para qualquer tipo de string no template que você precisa traduzir, é necessário adicionar tags **{% trans ‘TEXTO’ %}**
    
    ```python
    {% load i18n %} # importante
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<meta charset="UTF-8">
    	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<title>Translation</title>
    
    	<!-- CSS -->
    	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    
    </head>
    <body>   
    
    	<div class="container"> 
    
    		<h1>{% trans 'Testando Biblioteca para Tradução de Site' %}</h1>
    
    		<p>{% trans 'Para tornar um projeto Django traduzível, você deve adicionar um número mínimo de ganchos ao seu código e modelos' %}</p>
    
    	</div> 
     
    	<!-- JS-->
    	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    </body>
    </html>
    ```
    
    mysite_app/*views.py*
    
    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def mysite(request):
        return render(request, 'home.html')
    ```
    
    mysite_app/*urls.py*
    
    ```
    from django.urls import path 
    from mysite_app import views
    
    urlpatterns = [
        path('', views.mysite, name='mysite'), 
    ]
    ```
    
    urls.py do projeto. ***core/urls.py***
    
    ```python
    from django.contrib import admin
    from django.urls import path, include 
    from django.conf import settings
    from django.conf.urls.static import static 
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('mysite_app.urls')), 
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```
    
    Rodar o projeto para ver.
    
    ```python
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver
    ```
    
    É para ter um resultado como esse.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9be72221-ce06-429d-ba12-65cc1faf528c/Untitled.png)
</details>

<details><summary><b>Template e Bootstrap Configuração</b></summary>
    
- **MakeMessages**
    
    Esse comando vai criar os arquivos .po do conteúdo de todo projeto que tem as tags 
    
    **{% trans “TEXTO” %}**
    
    `django-admin makemessages --all --ignore=env`
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3c33300-f836-4020-90cf-ae298c32ecfc/Untitled.png)
    
    **no arquivo *locale*/br/LC_MESSAGES**
    
    copia msgid igual para msgtr. A linguagem padrão do nosso projeto é pt-br então não muda.
    
    ```python
    #: mysite_app/templates/home.html:19
    msgid "Testando Biblioteca para Tradução de Site"
    msgstr "Testando Biblioteca para Tradução de Site"
    
    #: mysite_app/templates/home.html:21
    msgid ""
    "Para tornar um projeto Django traduzível, você deve adicionar um número "
    "mínimo de ganchos ao seu código e modelos"
    
    msgstr ""
    "Para tornar um projeto Django traduzível, você deve adicionar um número "
    "mínimo de ganchos ao seu código e modelos"
    ```
    
    **no arquivo *locale*/en/LC_MESSAGES**
    
    Aqui já traduz do português para inglês. msgid é mensagem original (pt-br) e msgstr é tradução.
    
    ```python
    #: mysite_app/templates/home.html:19
    msgid "Testando Biblioteca para Tradução de Site"
    msgstr "Testing Library for Site Translation"
    
    #: mysite_app/templates/home.html:21
    msgid ""
    "Para tornar um projeto Django traduzível, você deve adicionar um número "
    "mínimo de ganchos ao seu código e modelos"
    
    msgstr ""
    "To make a Django project translatable, you must add a number "
    "minimum hooks to your code and templates"
    ```
    
    Depois que traduzir precisa compilar essas mensagens
    
    `django-admin compilemessages --ignore=env`
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc9ca893-5192-424c-b926-62e33d69669d/Untitled.png)
    
    em *core/urls.py* adicionar urlpatterns
    
    ```python
    from django.conf.urls.i18n import i18n_patterns
    
    urlpatterns = [
        *i18n_patterns(*urlpatterns, prefix_default_language=False),
        ]
    ```
    
    Para testar.
    
    ```python
    python manage.py runserver
    ```
    
    Padrão (pt-br)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec9db674-0479-4f2e-afb3-65cc77ef7c7e/Untitled.png)
    
    Inglês (en)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5295a45d-6c33-4f2b-826a-08fddfb9a03c/Untitled.png)
</details>


<details><summary><b>Alterar idioma no botão (template)</b></summary>

- **Alterar idioma no botão (template)**
    
    Criar um arquivo *languege.py* na pasta do seu projeto. 
    
    *core/language.py*
    
    ```python
    from urllib.parse import urlparse
    from django.conf import settings
    from django.http import HttpResponseRedirect
    from django.urls.base import resolve, reverse
    from django.urls.exceptions import Resolver404
    from django.utils import translation
    
    def set_language(request, language):
        for lang, _ in settings.LANGUAGES:
            translation.activate(lang)
            try:
                view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
            except Resolver404:
                view = None
            if view:
                break
        if view:
            translation.activate(language)
            next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
            response = HttpResponseRedirect(next_url)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        else:
            response = HttpResponseRedirect("/")
        return response
    ```
    
    *core/urls.py*
    
    ```python
    from django.contrib import admin
    from django.urls import path, include
    from django.conf.urls.i18n import i18n_patterns
    from django.conf import settings
    from django.conf.urls.static import static
    from core.language import set_language # new
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('mysite_app.urls')), 
    ]
    
    urlpatterns = [
        *i18n_patterns(*urlpatterns, prefix_default_language=False),
    		 path("set_language/<str:language>", set_language, name="set-language"), # new
    
        ] 
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```
    
    no template *myapp_app/home.html*
    
    ```python
    <div class="container">
    		
    		<a href="{% url 'set-language' 'pt-br' %}">BR</a> # adiciona
    
    		<a href="{% url 'set-language' 'en' %}">EN</a> # adiciona
    
    		<h1>{% trans 'Testando Biblioteca para Tradução de Site' %}</h1>
    
    		<p>{% trans 'Para tornar um projeto Django traduzível, você deve adicionar um número mínimo de ganchos ao seu código e modelos' %}</p>
    
    	</div>
    ```
</details>


Veja tambem Internacionalização dos Modelos no Django [Link](https://www.youtube.com/watch?v=kkyAi6-s6J4&t=0s)
