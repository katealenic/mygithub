from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms.models import modelform_factory

class Manager(models.Model):
    name = models.ForeignKey(User, related_name='name')

class Wiki(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    txt = models.TextField()

class Project(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    wiki = models.ForeignKey(Wiki, related_name='wiki')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "/project/%i/" % self.id


class Discussions(models.Model):
    discus = models.ForeignKey(Project, related_name='discus')
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    txt = models.TextField()
    def get_absolute_url(self):
        return "/discus/%i/" % self.id

class Comment(models.Model):
    body = models.ForeignKey(Discussions, related_name='discuss')
    author = models.ForeignKey(User, related_name='autor')
    text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Developer(models.Model):
    users = models.ForeignKey(Project, related_name='developers')
    peopl = models.ForeignKey(User, related_name='user')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class News(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Membership(models.Model):
    news = models.ManyToManyField(News)

class Files(models.Model):
    name = models.CharField(max_length=50)
    urls  = models.CharField(max_length=500)
    publish = models.DateTimeField(default=timezone.now)
    files = models.ForeignKey(Project, related_name='file')

    def get_absolute_url(self):
        return "/file/%i/" % self.id