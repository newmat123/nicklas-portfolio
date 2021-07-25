from django.shortcuts import render

def index(request):
    return render(request, 'portfolioTemplates/index.html', {})

def aboutMe(request):
    return render(request, 'portfolioTemplates/aboutMe.html', {})

def projects(request):
    return render(request, 'portfolioTemplates/projects.html', {})