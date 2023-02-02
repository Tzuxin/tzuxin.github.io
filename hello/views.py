from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request, *kwargs):
    email= 'jhaz@email.com'
    user = User.objects.get(email=email)
    print (user)
    context = {
        "name": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "date_joined": user.date_joined,
        "last_login": user.last_login,
    }
    return render(request, 'chat.html', context)

def greet(request, name):
    return HttpResponse(f'Hello, {name.capitalize()}!')

