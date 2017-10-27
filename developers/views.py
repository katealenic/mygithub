from django.contrib.auth.models import Group
from django.http import Http404
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib import auth
from django.template.context_processors import csrf
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.utils import timezone

from developers.form import PersonForm, WikiForm, DiscusForm, CommentForm
from main.models import News, Project, Developer, Wiki, Discussions, Comment


def ProjectDetails(request, info_id):
    try:
        info = Project.objects.get(pk=info_id)
    except info.DoesNotExist:
        raise Http404
    return render(request, 'developers.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'username': auth.get_user(request).username,'object': info})

def DeveloperDetails(request, info_id):
    try:
        info = Project.objects.get(pk=info_id)
    except info.DoesNotExist:
        raise Http404
    return render(request, 'developers_project.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'develop': Developer.objects.all(),'username': auth.get_user(request).username,'object': info})

def developer_new(request,pk):
    p = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.users=p
            post.save()
            g = Group.objects.get(name='developer')
            post.peopl.groups.add(g)
            info=Project.objects.get(pk=pk)
            return render(request, 'developers_project.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'develop': Developer.objects.all(),'username': auth.get_user(request).username,'object': info})
    else:
        form = PersonForm()
    return render(request, 'developer_new.html', {'form': form,'username': auth.get_user(request).username})

def developer_del(request, pk):
    post = Developer.objects.get(pk=pk)
    info = post.users
    post.delete()
    return render(request, 'developers_project.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'develop': Developer.objects.all(),'username': auth.get_user(request).username,'object': info})

def WikiDetails(request, info_id):
    try:
        info = Project.objects.get(pk=info_id)
    except info.DoesNotExist:
        raise Http404
    return render(request, 'wiki.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'wiki': Wiki.objects.all(),'username': auth.get_user(request).username,'object': info})


def wiki_change(request, pk):
    post = get_object_or_404(Project, pk=pk)
    info = Project.objects.get(pk=pk)
    if request.method == "POST":
        form = WikiForm(request.POST, instance=post.wiki)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, 'wiki.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'wiki': Wiki.objects.all(),'username': auth.get_user(request).username,'object': info})
    else:
        form = WikiForm(instance=post.wiki)
    return render(request, 'wiki_new.html', {'form': form,'username': auth.get_user(request).username})

def DiscussionDetails(request, info_id):
    try:
        info = Project.objects.get(pk=info_id)
    except info.DoesNotExist:
        raise Http404
    return render(request, 'discussions.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'discus': Discussions.objects.all(),'username': auth.get_user(request).username,'object': info})


def discussion_new(request, pk):
    p = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = DiscusForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = auth.get_user(request).username
            post.published_date = timezone.now()
            post.discus=p
            post.save()
            info = Project.objects.get(pk=pk)
        return redirect('discus',pk)
    else:
        form = DiscusForm()
    return render(request, 'discus_new.html', {'form': form,'username': auth.get_user(request).username})

def discus_del(request, pk, id):
    post = Discussions.objects.get(pk=pk)
    p = Project.objects.get(pk=id)
    for c in Comment.objects.all():
        if c.body==post:
            c.delete()
    post.delete()
    return render(request, 'discussions.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'discus': Discussions.objects.all(),'username': auth.get_user(request).username,'object': p})

def CommentDetails(request, info_id):
    try:
        info = Discussions.objects.get(pk=info_id)
        p = info.discus
    except info.DoesNotExist:
        raise Http404
    return render(request, 'comments.html', {'news_list': News.objects.all(),'comment': Comment.objects.all(), 'grup': request.user.groups.filter(),'username': auth.get_user(request).username, 'discus': info,'object': p})


def comment_new(request, pk):
    p = get_object_or_404(Discussions, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.body=p
            post.save()
        return redirect('comment',pk)
    else:
        form = CommentForm()
    return render(request, 'comment_new.html', {'form': form,'username': auth.get_user(request).username})

def comment_del(request, pk, id):
    post = Comment.objects.get(pk=pk)
    p = Discussions.objects.get(pk=id)
    nn = p.discus
    post.delete()
    return render(request, 'comments.html', {'news_list': News.objects.all(), 'grup': request.user.groups.filter(), 'comment': Comment.objects.all(),'discus': p,'username': auth.get_user(request).username,'object': nn})
