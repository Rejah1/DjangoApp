from django.shortcuts import render, HttpResponse

# render, renders the actual HTML template
# Create your views here.
def home(request):
	# return HttpResponse('Home Page!')
	return render(request, 'logbook/login.html')
	