from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone

from main.form import NewForm
from main.models import Membership, News, Project


def index(request):
    context = {'news_list':News.objects.all(),'grup':request.user.has_perm('can_add_comment'), 'username':auth.get_user(request).username, 'grup': request.user.groups.filter()}
    return render(request, 'index.html', context)

def new_new(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        context = {'project': Project.objects.all(),'news_list': News.objects.all(), 'grup': request.user.groups.filter(),'username': auth.get_user(request).username}
        return render(request, 'projects.html', context)
    else:
        form = NewForm()
    return render(request, 'new.html', {'form': form, 'username': auth.get_user(request).username})

def new_del(request, pk):
    post = get_object_or_404(News, pk=pk)
    post.delete()
    return redirect('project')