from django.conf.urls import url
from registration import views

urlpatterns = [
    url(r'^register/$', views.RegisterFormView.as_view()),
]