from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import chef, dish
from django.urls import resolve
import queue
# Create your views here.
df_queue = queue.Queue()


def kitchen(request):
    if request.method == 'GET':
        return render(request, 'chefs/kitchen.html')


def insert(request):
    str_home = "http://127.0.0.1:8000/chefs//insert"
    if request.method == 'GET':
        return render(request, 'chefs/insert.html')
    if request.method == 'POST':
        try:
            if 'chef_submit' in request.POST:
                cno = request.POST["chef_cno"]
                c_description = request.POST["chef_description"]
                salary = request.POST["chef_salary"]
                if int(cno) <= 0 or int(salary) < 0:
                    return render(request, "chefs/error.html", {"error": " negative input", "home": str_home})
                if chef.objects.filter(cno=cno):
                    return render(request, "chefs/error.html", {"error": " the tuple exists", "home": str_home})
                if int(cno) > 0 or int(salary) >= 0:
                    temp_chef = chef(cno, c_description, salary)
                    temp_chef.save()
                    return render(request, "chefs/successful.html", {"home": str_home, "part": " insert"})
            if 'dish_submit' in request.POST:
                dno = request.POST['dish_dno']
                d_description = request.POST['dish_description']
                price = request.POST['dish_price']
                if int(dno) <= 0 or float(price) < 0:
                    return render(request, "chefs/error.html", {"error": " negative input", "home": str_home})
                if dish.objects.filter(dno=dno):
                    return render(request, "chefs/error.html", {"error": " the tuple exists", "home": str_home})
                if int(dno) > 0 or float(price) >= 0:
                    temp_dish = dish(dno, d_description, price)
                    temp_dish.save()
                    return render(request, "chefs/successful.html", {"home": str_home, "part": " insert"})
                return render(request, "chefs/successful.html",  {"home": str_home, "part": " insert"})
        except Exception as e:
            return render(request, "chefs/error.html", {"error": e, "home": str_home})


def delete(request):
    str_home = "http://127.0.0.1:8000/chefs//delete"
    if request.method == 'GET':
        return render(request, 'chefs/delete.html')
    if request.method == 'POST':
        try:
            if 'delete_cno' in request.POST:
                cno = request.POST["cno"]
                chef_tuple = chef.objects.filter(cno=cno)
                if chef_tuple:
                    chef_tuple.delete()
                    return render(request, "chefs/successful.html", {"home": str_home, "part": " chef_delete"})
                if not chef_tuple:
                    return render(request, "chefs/error.html", {"error": " this cno don't have chef", "home": str_home})
            if 'delete_dno' in request.POST:
                dno = request.POST['dno']
                dish_tuple = dish.objects.filter(dno=dno)
                if dish_tuple:
                    dish_tuple.delete()
                    return render(request, "chefs/successful.html", {"home": str_home, "part": " chef_delete"})
                if not dish_tuple:
                    return render(request, "chefs/error.html", {"error": " this dno don't have dish", "home": str_home})
        except Exception as e:
            return render(request, "chefs/error.html", {"error": e, "home": str_home})
        return render(request, "chefs/error.html", {"error": " no delete", "home": str_home})


def alert(request):
    str_home = "http://127.0.0.1:8000/chefs//alert"
    if request.method == 'GET':
        return render(request, "chefs/alert.html")
    if request.method == 'POST':
        try:
            if 'chef_submit' in request.POST:
                cno = request.POST["chef_cno"]
                c_description = request.POST["chef_description"]
                salary = request.POST["chef_salary"]
                if int(cno) <= 0 or int(salary) < 0:
                    return render(request, "chefs/error.html", {"error": " negative input", "home": str_home})
                if int(cno) > 0 or int(salary) >= 0:
                    temp_chef = chef(cno, c_description, salary)
                    temp_chef.save()
                    return render(request, "chefs/successful.html", {"home": str_home, "part": " insert"})
            if 'dish_submit' in request.POST:
                dno = request.POST['dish_dno']
                d_description = request.POST['dish_description']
                price = request.POST['dish_price']
                if int(dno) <= 0 or float(price) < 0:
                    return render(request, "chefs/error.html", {"error": " negative input", "home": str_home})
                if int(dno) > 0 or float(price) >= 0:
                    temp_dish = dish(dno, d_description, price)
                    temp_dish.save()
                    return render(request, "chefs/successful.html", {"home": str_home, "part": " insert"})
                return render(request, "chefs/successful.html",  {"home": str_home, "part": " insert"})
        except Exception as e:
            return render(request, "chefs/error.html", {"error": e, "home": str_home})



def select(request):
    str_home = "http://127.0.0.1:8000/chefs//alert"
    if request.method == 'GET':
        return render(request, "chefs/select.html")
    if request.method == 'POST':
        try:
            if "submit_cno" in request.POST:
                cno = request.POST["cno"]
                show_chef = chef.objects.filter(cno=cno)
                chef_information = ""
                for i in show_chef:
                    chef_information = chef_information+"chef number: "+str(i.cno)+"    "
                    chef_information = chef_information+"description: "+str(i.description)+"    "
                    chef_information = chef_information+"salary: "+str(i.salary)+"    "
                return render(request, "chefs/showtable.html", {"home": str_home, "chef_information": chef_information})
            if "submit_dno" in request.POST:
                dno = request.POST['dno']
                show_dish = dish.objects.filter(dno=dno)
                dish_information = ""
                for i in show_dish:
                    dish_information = dish_information+"chef number: "+str(i.dno)+"    "
                    dish_information = dish_information+"description: "+str(i.description)+"    "
                    dish_information = dish_information+"salary: "+str(i.price)+"    "
                return render(request, "chefs/showtable.html", {"home": str_home, "dish_information": dish_information})
        except Exception as e:
            return render(request, "chefs/error.html", {"error": e, "home": str_home})


def grab(request):
    str_home = "http://127.0.0.1:8000/chefs//grab"
    resolver_match = resolve(request.path_info)
    url_name = resolver_match.url_name
    if url_name == '/grab1':
        cno = 1
    if url_name == '/grab2':
        cno = 2
    if url_name == '/grab3':
        cno = 3