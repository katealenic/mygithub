from django.conf.urls import url
from django.contrib import admin

from main import viewss

urlpatterns = [
    url(r'^$', viewss.index, name='index'),
]
