from django.urls import path
from . import views

# the first parameter is about internet address,the next is view's function,the last is name to link to templates


urlpatterns = [
    path("/insert", views.insert, name='/insert'),
    path("/delete", views.delete, name='/delete'),
    path("/alert", views.alert, name='/alert'),
    path("/select", views.select, name='/select'),
    path("", views.kitchen, name='/kitchen')
]