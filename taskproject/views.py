from django.shortcuts import render
from taskapp1.models import Task

def home(request):
    data = Task.objects.all()    
    context= {'tasks': data}
    return render(request, 'home.html', context)