from django.shortcuts import render
from .models import Homepage, Skillset, Learning, Alternative, Second_Profile, Projects

def index(request):
    home = Homepage.objects.all()
    skills = Skillset.objects.all()
    learning = Learning.objects.all()
    alternative = Alternative.objects.all()
    second = Second_Profile.objects.all()
    projects = Projects.objects.all()

    context = {'home':home, 'skills':skills, 'learning':learning, 'alternative':alternative, 'second':second,
    'projects':projects}

    return render(request, 'main/index.html', context)