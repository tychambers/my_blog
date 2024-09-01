from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	context = {
	"variable1":[0,1,2,3,4,5,6],
	"variable2": "Hello All!"
	}
	return render(request, 'about.html', context)
