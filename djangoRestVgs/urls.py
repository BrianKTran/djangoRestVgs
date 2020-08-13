from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vgsRestApp import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^index/', views.index.as_view(), name='index'),
    # url(r'^ccGet/', views.ccGet.as_view(), name='ccGet'),
    # url(r'^ccPost/', views.ccPost.as_view(), name='ccPost'),
    path('index/', views.index.as_view(), name='index'),
    # path('index/', views.index, name='index'),
    path('ccPost/',views.ccPost.as_view(), name='ccPost'),
    path('ccGet/', views.ccGet.as_view(), name='ccGet'),
    # url(r'^/', views.insertCC.as_view(), name='ccinsert'),
    # path('index/', views.insertCC)

]


# urlpatterns = [
# path('admin/', admin.site.urls),
# path('index/', views.index, name='index'),
# path('ccPost/', views.ccPost, name='ccPost'),
# path('ccGet/', views.index, name='ccGet'),
# ]
#
urlpatterns = format_suffix_patterns(urlpatterns)
