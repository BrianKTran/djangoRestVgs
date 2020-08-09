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
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vgsRestApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),
    # url(r'^creditCardInfo/', views.creditCardList.as_view(), name='creditCardInfo'),
    url(r'^index/', views.index_view.as_view(), name='index'),
    # url(r'^index/', views.creditCardList.index, name='index')
    # path('index/', views.indexPost, name='index'),
    # path('index/', views.indexGet, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)