from django.conf.urls import url

from profiles import views

urlpatterns = [
    url(r'^$', views.profile),
]