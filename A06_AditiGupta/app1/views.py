from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'app1/homepage.html')

def about(request):
    return render(request, 'app1/about.html')