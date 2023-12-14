from django.shortcuts import render

# Create your views here.
def finder(request):
    return render(request,"finder/finder.html")