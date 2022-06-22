from django.urls import re_path, include, path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^landing123/$', views.landing, name='landing'),
    re_path(r'^about/$', views.about, name='about'),
]
