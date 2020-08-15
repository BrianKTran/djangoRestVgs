from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vgsRestApp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index.as_view(), name='index'),
    path('ccPost/',views.ccPost.as_view(), name='ccPost'),
    path('ccGet/', views.ccGet.as_view(), name='ccGet'),
    path('postReveal/',views.postReveal.as_view(), name='postReveal'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
