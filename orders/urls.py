from django.urls import re_path, include, path

from . import views

urlpatterns = [
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    re_path(r'^checkout/$', views.checkout, name='checkout'),
    # path('shop/', views.shop, name='shop')
]