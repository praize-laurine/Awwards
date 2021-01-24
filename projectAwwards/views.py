from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout



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


