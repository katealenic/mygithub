"""itransition1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from developers import views
from files import view
from main import viewss

urlpatterns = [

    url(r'^news_del/(?P<pk>[0-9]+)/$',viewss.new_del, name='index'),
    url(r'^news/$',viewss.new_new, name='new'),
    url(r'^coment/del/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$', views.comment_del, name='comment_del'),
    url(r'^coment/new/(?P<pk>[0-9]+)/$', views.comment_new, name='comment_new'),
    url(r'^coment/discus/(?P<info_id>[0-9]+)/$', views.CommentDetails, name='comment'),
    url(r'^discus/del/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$', views.discus_del, name='discus_del'),
    url(r'^discus/new/(?P<pk>[0-9]+)/$', views.discussion_new, name='discus_new'),
    url(r'^discus/project/(?P<info_id>[0-9]+)/$', views.DiscussionDetails, name='discus'),
    url(r'^wiki/new/(?P<pk>[0-9]+)/$', views.wiki_change, name='wiki_change'),
    url(r'^wiki/project/(?P<info_id>[0-9]+)/$', views.WikiDetails, name='wiki'),
    url(r'^files/del/(?P<pk>[0-9]+)/$', view.file_del, name='file_del'),
    url(r'^files/upload/(?P<pk>[0-9]+)/$', view.file_new, name='file_new'),
    url(r'^files/project/(?P<info_id>\d+)/$', view.FileDetails, name='files'),
    url(r'^developer//project/(?P<info_id>\d+)/$', views.ProjectDetails),
    url(r'^developers_project//project/(?P<info_id>\d+)/$', views.DeveloperDetails, name='developer_user'),
    url(r'^developer/new/(?P<pk>[0-9]+)/$', views.developer_new, name='developer_new'),
    url(r'^developer/del/(?P<pk>[0-9]+)/$', views.developer_del, name='developer_del'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('projects.urls')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^auth/', include('authorization.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^projects/', include('projects.urls')),

]
