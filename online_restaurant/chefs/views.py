from django.shortcuts import render

# Create your views here.
def insert(request):
    if request.method == 'GET':
        return render(request, 'chefs/insert.html')


def kitchen(request):
    if request.method == 'GET':
        return render(request, 'chefs/kitchen.html')


def delete(request):
    if request.method == 'GET':
        return render(request, 'chefs/delete.html')

def alert(request):
    if request.method == 'GET':
        return render(request, "chefs/alert.html")


def select(request):
    if request.method == 'GET':
        return render(request, "chefs/select.html")