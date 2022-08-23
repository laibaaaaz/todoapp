from http.client import HTTPResponse
from turtle import title
from urllib.error import HTTPError
from xml.dom import ValidationErr
from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

def loginview(request):
    if request.method == "POST":
        username = request.POST['name']
        pass1 = request.POST['pwd']
        email = request.POST['email']

        user = authenticate(request, username = username, password = pass1)

        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            raise ValidationErr  
    return render(request, 'login.html')      

def signup(request):
    if request.method == "POST":
        pass1 = request.POST['pwd']
        username = request.POST['name']
        email = request.POST['email']
        user = User.objects.create_user(username = username, email=email, password = pass1)
        user.save()
       # new_person = Person(name=request.POST['name'], email= request.POST['email'])
        #new_person.save()

        return redirect('/main')

    return render(request, 'signup.html')   


def index(request):
    #pk2 = int(pk)#
    #user = Person.objects.get(id=pk2)
    todo = Todo.objects.all()
   

    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title'],
            person = request.user
        )

        new_todo.save()
        return redirect('/main')
    

    return render(request, 'index.html', {'todos': todo})


def delete(request, i):
    todo = Todo.objects.get(id=i)
    todo.delete()

    return redirect('/main')



def logoutview(request):
    logout(request)
    return redirect('login')

   