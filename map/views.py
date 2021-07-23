from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        context = {
            'user':User.objects.get(),
        }
        return render(request, template_name='home.html', context=context)
    else:
        return render(request, template_name='home.html', context={})


