from django.shortcuts import render

# Create your views here.
def index(request):
    print("index page")
    return render(request, 'index/index.html')