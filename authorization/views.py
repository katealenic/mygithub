from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.template.context_processors import csrf


def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username = username, password = password)
		if user is not None and user.is_active == True:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = "User not found"
			return render_to_response('authorization.html', args)
	else:
		return render_to_response('authorization.html', args)

def logout(request):
	auth.logout(request)
	return redirect("/")
