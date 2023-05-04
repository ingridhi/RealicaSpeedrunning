from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Member
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            Member(name=User.objects.all().values()[len(User.objects.all()) - 1].get('username')).save()
            return redirect('/login')
        
    else:
        form = UserCreationForm()    

    return render(request, 'register/register.html', {'form': form})