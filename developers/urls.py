from django.conf.urls import url

from developers import views

urlpatterns = [
    url(r'^developer/new/$', views.developer_new, name='developer_new'),
    url(r'^developer/del/(?P<pk>[0-9]+)/$', views.developer_del, name='developer_del'),
]