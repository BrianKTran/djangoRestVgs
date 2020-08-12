"""djangoRestVgs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vgsRestApp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    url(r'^ccGet/', views.ccGet.as_view(), name='ccGet'),
    url(r'^ccPost/', views.ccPost.as_view(), name='ccPost'),
    url(r'^index/', views.index.as_view(), name='index'),
    # url(r'^/', views.insertCC.as_view(), name='ccinsert'),
    # path('index/', views.insertCC)
  
]

urlpatterns = format_suffix_patterns(urlpatterns)