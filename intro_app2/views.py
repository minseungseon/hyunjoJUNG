from django.shortcuts import render

# Create your views here.
def artwork(request):
	return render(request, 'artwork.html')