from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, PasswordResetForm, AdminPasswordChangeForm, \
	ReadOnlyPasswordHashField, UserModel, UserCreationForm
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth


def profile(request):
	return render_to_response('profile.html', {'user': auth.get_user(request),'grup': request.user.groups.filter(), 'username': auth.get_user(request).username})
