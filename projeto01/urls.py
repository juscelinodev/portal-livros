"""projeto01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# When importing a file, Python only searches the directory that the entry-point script 
# is running from and sys.path which includes locations such as the package installation directory
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'c:/dev/devweb/projeto01/portal')
import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('autor', views.autor, name='autor'),
    path('livro', views.livro, name='livro'),
    path('livro/add', views.livro_add, name='livro_add'),
    path('livro/edit/<int:livro_pk>', views.livro_edit, name='livro_edit'),
    path('livro/delete/<int:livro_pk>', views.livro_delete, name='livro_delete'),
    path('autor/add', views.autor_add, name='autor_add'),
    path('autor/edit/<int:autor_pk>', views.autor_edit, name='autor_edit'),
    path('autor/delete/<int:autor_pk>', views.autor_delete, name='autor_delete'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),    
]
