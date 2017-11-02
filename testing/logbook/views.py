from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from logbook.forms import RegistrationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Rejah'

    args = {'myName': name, 'numbers' : numbers }
    return render(request,'logbook/home.html', args)



def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/logbook')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'logbook/register.html', args)
