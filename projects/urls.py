from django.conf.urls import url

from projects import views

urlpatterns = [
    url(r'^$', views.project, name='project'),
    url(r'^project/new/$', views.project_new, name='project_new'),
    url(r'^project/del/(?P<pk>[0-9]+)/$', views.project_del, name='project_del'),
    url(r'^project/manage/$', views.manager_new, name='manager_new'),

]