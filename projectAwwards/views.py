from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import  Project, Profile
import json


# Create your views fhere.
def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return redirect(request,'registration/signUp_form.html', {'form':form})  

@login_required(login_url='/accounts/login/')
def index(request):
    project = Project.all_projects()
    json_projects = []
    for project in project:
        picture = profile.objects.filter(user=project.user.id).first()
        if picture:
            picture = picture.profile_pic.url
        else:
            picture = ''
        obj = dict(
            title = project.title,
            image = project.image,
            url_link = project.url_link,
            description = project.description,
            avatar = picture,
            date_created = project.date_created,
            author = project.user.username
        )   
        json_projects.append(obj) 
    return render(request, 'index.html', {"json_projects": json_projects})                   

@login_required(login_url='/accounts/login/')
def userProfile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance = request.user)
        prof_form = UserProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)

        if user_form.is_valid and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            message.success(request, f'Your account has been updated successfully!')
            return redirect('userProfile')

    else:
        user_form = UpdateUserForm(instance = request.user)
        prof_form = UserProfileUpdateForm(instance = request.user.profile)
    context = {
        'user_form': user_form,
        'prof_form': prof_form
    }     
    return render(request, 'userProfile.html', context) 

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            prof_form.save()

            return redirect('index')

    else:
        user_form = UpdateUserForm(instance = request.user)
        prof_form = UserProfileUpdateForm(instance = request.user)

        context = {
            'user_form' : user_form,
            'prof_form' : prof_form
        }        

    return render(request, 'update_profile.html', context)    

def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term =request.GET.get('project')
        searched_project = Project.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message,"projects":searched_project})

    else:
        message = "You haven't searched for any term"

        return render(request,'search.html',{'message':message})    


@login_required(login_url='/accounts/login/')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('index')

    else:
        form = PostProjectForm()
    return render(request, 'post_project.html', {"form": form})
    
