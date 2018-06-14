from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Value
from django.db.models.functions import Concat
from models import *
import bcrypt
import re
from django.contrib import messages 
  # the index function is called when root is visited
def index(request):
    return render(request, 'nip/login.html')

def new_user(request):
	errors = User.objects.regis_basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	first_name = request.POST['first_name'].lower()
	last_name = request.POST['last_name'].lower()
	email = request.POST['email'].lower()
	image = request.POST['picture']
	password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
	User.objects.create(first_name=first_name, last_name=last_name, email=email, image=image,password=password)
	request.session['id'] = User.objects.get(email=email).id
	request.session['first_name'] = User.objects.get(email=email).first_name
	return redirect('/socials')

def login(request):
	errors = User.objects.log_basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	email = request.POST['email']
	password = request.POST['password']
	user = User.objects.get(email=email)
	request.session['id'] = user.id
	print "===+=====+=====+====+======"
	print request.session['id']
	request.session['first_name'] = User.objects.get(email=email).first_name
	return redirect("/home")


def strength(request):
	if not 'id' in request.session:
		return redirect('/')
	context = {
		'stacks': Stack.objects.all()
		}
	return render(request, 'nip/strengths.html', context)

def strength_edit(request, id):
	user = User.objects.filter(id=id)
	context = {
		'user':User.objects.get(id=id),
		'stacks': Stack.objects.all()
		}
	
	return render(request, 'nip/strengths_edit.html', context)	

def socials(request):
	if not 'id' in request.session:
		return redirect('/')
	print request.session['id']
	return render(request, 'nip/registration.html')


def socials_process(request):
	errors = {}
	if len(request.POST['linkedin']) < 1:
		errors['linkedin'] = 'LinkedIn field is mandatory :)'
	# if len(request.POST['type']) < 1:
	# 	errors['post'] = 'Please answer if you are an instructor or student'
	if len(request.POST['github']) < 1:
		errors['github'] = 'GitHub field is mandatory :)'
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/socials')
	status = request.POST['type']
	linkedin = request.POST['linkedin']
	facebook = request.POST['facebook']
	github = request.POST['github']
	slack = request.POST['slack']
	instagram = request.POST['instagram']
	twitter = request.POST['twitter']
	user = User.objects.get(id=request.session['id'])
	user.status = status
	user.linkedin = linkedin
	user.facebook = facebook
	user.github = github
	user.slack = slack
	user.instagram = instagram
	user.twitter = twitter
	user.save()
	if request.POST['help'].lower() == 'yes':
		return redirect('/strengths')
	else: 
		return redirect('/home')

def home(request):
	if not 'id' in request.session:
		return redirect('/')
	print "==========================================="	
	print request.session['id']
	return render(request,'nip/home.html')	 

def process(request):
	if request.method == "POST":
		user = User.objects.get(id=request.session["id"])
		strengths = request.POST.getlist('sCheck')
		for num in strengths:
			print "++++++++"
			print num
			user.strengths.add(num)	 
		return redirect('/home')

def process_edit(request):
	if request.method == "POST":
		user = User.objects.get(id=request.session["id"])
		strengths = request.POST.getlist('sCheck')
		user.strengths = []
		for num in strengths:
			print "*********"
			print num
			user.strengths.add(num)	 
		return redirect('/home')

def help_search(request):
	if not 'id' in request.session:
		return redirect('/')
	return render(request, 'nip/help_search.html')

def user_search(request):
	if not 'id' in request.session:
		return redirect('/')
	return render(request, 'nip/user_search.html')

def searching_user(request):
	if not 'id' in request.session:
		return redirect('/')
	queryset = User.objects.annotate(search_name=Concat('first_name', Value(' '), 'last_name'))
	results = queryset.filter(search_name__icontains=request.POST["user_search"].lower())

	context = {
		'searches': request.POST['user_search'],
		'results': results,
		# 'count': results.count()
	}

	return render(request, 'nip/user_result.html', context)

def searching_help(request):
	if not 'id' in request.session:
		return redirect('/')
	strength = Skill.objects.filter(name__icontains=request.POST['tutor_search'])
	context = {
		'users': User.objects.filter(strengths=strength),
		'skill': request.POST['tutor_search']
	}
	return render(request, 'nip/help_result.html', context)

def profile(request, id):
	if not 'id' in request.session:
		return redirect('/')
	print request.session['id']
	print id 
	# if int(request.session['id']) != int(id):
	context = {
		'user':User.objects.get(id=id),
	}
	return render(request, 'nip/profile.html', context)
	# else:
	# 	context = {
	# 		'user':User.objects.get(id=id),
	# 	}
	# 	return render(request, 'nip/edit_profile.html', context)

def edit(request, id):
	context = {
		'user':User.objects.get(id=id),
	}
	return render(request, 'nip/edit_profile.html', context)


	
def edit_profile(request, id):
	if not 'id' in request.session:
		return redirect('/')
	errors = User.objects.regis_basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	first_name = request.POST['first_name'].lower()
	last_name = request.POST['last_name'].lower()
	email = request.POST['email'].lower()
	image = request.POST['picture']
	password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
	user = User.objects.filter(id=id)
	user.update(first_name=first_name, last_name=last_name, email=email, image=image,password=password)
	request.session['id'] = User.objects.get(email=email).id
	request.session['first_name'] = User.objects.get(email=email).first_name
	return redirect('/home')	
	

def logout(request):

	request.session.clear()
	return redirect('/')

def map(request):
	return	render(request,'nip/map.html')