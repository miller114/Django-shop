from django.urls import re_path, include, path

from . import views

urlpatterns = [
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product')
]