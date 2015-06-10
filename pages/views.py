from django.shortcuts import render, render_to_response, redirect, get_object_or_404, Http404
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm, NewListForm, NewListItemForm
from django import forms
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import newlist

def deleter(request, username, slug):

	if username == request.user.username:

		user = User.objects.get(username=username)

		listname = request.user.newlist_set.filter(slug__iexact=slug)

		listname.delete()

		return redirect("/user/%s/profile" %(request.user.username))
	return HttpResponse('not deleted')

def deleter2(request, username, slug, pk):

	if username == request.user.username:

		user = User.objects.get(username=username)
		
		listname = request.user.newlist_set.filter(slug__iexact=slug)

		listitem = request.user.newlistitem_set.filter(pk=pk)

		listitem.delete()

		return redirect("/user/%s/list/%s" %(request.user.username, slug))
	return HttpResponse('not deleted')

def register_page(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()


			# Update our variable to tell the template registration was successful.
			registered = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print user_form.errors

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()


	# Render the template depending on the context.
	return render(request,
			'register.html',
			{'user_form': user_form,'registered': registered} )

def login_page(request):
	# Like before, obtain the context for the user's request.
	context = RequestContext(request)
	loggedin = False
	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/user/%s/profile' %(username))
		else:
			loggedin = True
			return render(request,
			'login.html',
			{'loggedin': loggedin} )

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render_to_response('login.html', {}, context)

def main_page(request, **kwargs):
	context = RequestContext(request)

	return render_to_response('home.html', {}, context)

def notfound(request, **kwargs):
	context = RequestContext(request)

	return render_to_response('404.html', {}, context)

def mylistpage(request, username, slug):

	context = RequestContext(request)
	#make sure that the user is authenticated
	if username == request.user.username:
		#If the user is authenticated, then perform the following functions to the page
		if request.user.is_authenticated():
			#Store the current user request object into a variable
			user = User.objects.get(username=username)

			listname = request.user.newlist_set.filter(slug__iexact=slug).first()

			if request.method == "POST":
				form = NewListItemForm(request.POST)

				if form.is_valid():
					save_it = form.save(commit = False)
					save_it.user = request.user
					save_it.list_name = listname
					save_it.save()

			form = NewListItemForm()
			
			#Store the list name to the item that starts with the url input
			listname = request.user.newlist_set.filter(slug__iexact=slug)

			listitems = request.user.newlist_set.filter(slug__iexact=slug)

			listobject = get_object_or_404(newlist, slug__iexact=slug)

			listasslug = slug

			if not listname:
			    return redirect('/notfound')
	else:
		return redirect('/notfound')

	return render_to_response('listview.html', {'form2': form,'lista': listname, 'listb': listitems, 'obj':listobject, 'slugname':listasslug}, context)

def control_panel(request, username):

	context = RequestContext(request)

	if username == request.user.username:

		if request.user.is_authenticated():

			user = User.objects.get(username=username)

			lists = request.user.newlist_set.all()

			listitems = request.user.newlistitem_set.all()
			if request.method == "POST":
				form = NewListForm(request.POST, request.FILES)

				if form.is_valid():
					save_it = form.save(commit = False)
					save_it.user = request.user
					save_it.save()

			form = NewListForm()

			return render_to_response('controlpanel.html', {'form': form, 'lists': lists,'listitems':listitems,}, context)

		else:
			return render_to_response('login.html', {}, context)
	else:
		return render_to_response('controlpanel.html', {}, context)


