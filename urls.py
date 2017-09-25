from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^new/$', views.new, name='new'),
    url('^new-confirm/$', views.new_confirm, name='new_confirm'),
]
