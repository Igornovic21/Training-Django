from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from account.forms import LoginForm

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def login_user(request):
    login_form = LoginForm()
    
    context = {
        'form': login_form
    }
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'connexion reussie')
            return redirect(index)
        else:
            messages.error(request, 'informations de connexion incorrectes')
            return render(request, 'account/login.html', context)
    else:            
        return render(request, 'account/login.html', context)