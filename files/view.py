from http import server

from attachments.forms import AttachmentForm
from attachments.models import Attachment
from django.contrib.auth.models import Group
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib import auth
from django.template import RequestContext
from django.template.context_processors import csrf
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.utils import timezone

from files.form import UploadForm
from main.models import News, Project, Developer, Files


def FileDetails(request, info_id):
    try:
        info = Project.objects.get(pk=info_id)
    except info.DoesNotExist:
        raise Http404
    return render(request, 'files.html', {'news_list': News.objects.all(),'file': Files.objects.all(), 'grup': request.user.groups.filter(),'develop': Developer.objects.all(),'username': auth.get_user(request).username,'object': info})

def first(request, info_id):
    try:
        info = Project.objects.get(pk=info_id)
    except info.DoesNotExist:
        raise Http404
    return render(request, 'files.html', {'news_list': News.objects.all(),'file': Files.objects.all(), 'grup': request.user.groups.filter(),'develop': Developer.objects.all(),'username': auth.get_user(request).username,'object': info})

def file_new(request,pk):
    p = get_object_or_404(Project, pk=pk)
    info = Project.objects.get(pk=pk)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.files:
            cloud_response = cloudinary.uploader.upload(request.FILES['file'],
                                                        resource_type  = 'raw',
                                                        use_filename=True,
                                                        unique_filename=False
                                                        )
            file_name = cloud_response['public_id']
            file_url = cloud_response['url']
            file = Files.objects.create(name=file_name, urls=file_url, publish=timezone.now(), files=p)
            file.save()
            return render(request, 'files.html', {'news_list': News.objects.all(),'file': Files.objects.all(), 'grup': request.user.groups.filter(),'develop': Developer.objects.all(),'username': auth.get_user(request).username,'object': info})
    else:
        form = UploadForm()
    return render(request, 'file_new.html', {'file': Files.objects.all(),'form': form,'username': auth.get_user(request).username})

def file_del(request, pk):
    post = Files.objects.get(pk=pk)
    info = post.files
    post.delete()
    return render(request, 'files.html', {'news_list': News.objects.all(),'file': Files.objects.all(), 'grup': request.user.groups.filter(),'develop': Developer.objects.all(),'username': auth.get_user(request).username,'object': info})

