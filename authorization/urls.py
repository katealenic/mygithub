from django.conf.urls import include, url

from authorization import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
]
