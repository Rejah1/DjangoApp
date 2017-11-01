from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# render, renders the actual HTML template
# Create your views here.
def home(request):
	# return HttpResponse('Home Page!')
	
	numbers = [1,2,3,4]
	name = 'Rejah'

	args = {'myName' : name, 'numbers': numbers}
	return render(request, 'logbook/home.html', args)

def register(request):
	if request.method =='POST':
		form == UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/logbook')
	else:
		form = UserCreationForm()

		args = {'form': form}
		return render(request, 'logbook/register.html', args)