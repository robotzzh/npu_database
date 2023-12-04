from django.shortcuts import render
from online_restaurant.chefs.views import df_queue
from online_restaurant.chefs.models import dish
# Create your views here.


def menu(request):
    if request.method == 'GET':
        for i in dish.objects.all():


        return render(request, "customers/menu.html")
