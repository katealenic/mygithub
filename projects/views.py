from django.contrib.auth.models import Group
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib import auth
from django.template.context_processors import csrf
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.utils import timezone

from main.models import Project, Membership, News, Wiki, Developer, Discussions, Comment, Files
from projects.form import PostForm, ManagerForm


def project_new(request):
    w = Wiki(title="",txt="")
    w.save()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.wiki = w
            post.save()
            return redirect('project')
    else:
        form = PostForm()
    return render(request, 'project_new.html', {'form': form,'username': auth.get_user(request).username})

def project_del(request, pk):
    post = get_object_or_404(Project, pk=pk)
    post.wiki.delete()
    for d in Developer.objects.all():
        if d.users==post:
            d.delete()
    for d1 in Discussions.objects.all():
        if d1.discus==post:
            for c in Comment.objects.all():
                if c.body == d1.discus:
                    c.delete()
            d1.delete()
    for f in Files.objects.all():
        if f.files==post:
            f.delete()
    post.delete()
    return render(request, 'projects.html',{'develop': Developer.objects.all(),'project': Project.objects.all(),'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'username': auth.get_user(request).username})

def project(request):
    return render(request, 'projects.html',{'develop': Developer.objects.all(),'project': Project.objects.all(),'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'username': auth.get_user(request).username})

def manager_new(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print(post.name)
            g = Group.objects.get(name='manager')
            post.name.groups.add(g)

            return redirect('project')
    else:
        form = ManagerForm()
    return render(request, 'manager.html', {'form': form,'username': auth.get_user(request).username})
