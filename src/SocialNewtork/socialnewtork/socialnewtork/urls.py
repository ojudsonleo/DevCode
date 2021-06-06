"""socialnewtork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import * # home,login,register,frogotpassword,charts,cards,blank,now,buttons,tables,ua,ub,uc,uo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login', login),
    path('register', register),
    path('forgot-password', frogotpassword),
    path('charts', charts),
    path('cards', cards),
    path('blank', blank),
    path("404", now),
    path("buttons", buttons),
    path("tables", tables),
    path("utilities-animation", ua),
    path("utilities-border", ub),
    path("utilities-color", uc),
    path("utilities-other", uo),
    path("graphql/", grap),
]
 