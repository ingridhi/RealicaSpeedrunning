from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import Transaction
from django.contrib.auth import get_user_model, logout
# Create your views here.

def index(request): 
    return HttpResponse('mai')

@login_required
def aprill(request):
    username= request.user.username

    all_transactions = Transaction.objects.all().order_by('-dt')
    
    data= {}
    User = get_user_model()
    all_users = User.objects.all()
    print(all_users)
    for isik in all_users:
        
        
        data[isik.username.capitalize()] = 0
    for tehing in all_transactions:
        data[tehing.saatja.capitalize()] = data[tehing.saatja.capitalize()] - tehing.summa
        data[tehing.saaja.capitalize()] = data[tehing.saaja.capitalize()] + tehing.summa

    volgnevus = data[username.capitalize()]

    context = {'kasutajanimi': username, 'ylekanded': all_transactions, 'volgnevus': volgnevus}
    return render(request, 'myapp/index.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

