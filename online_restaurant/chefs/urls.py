from django.urls import path
from . import views

# the first parameter is about internet address,the next is view's function,the last is name to link to templates


urlpatterns = [
    path("/insert", views.insert, name='/insert'),
    path("/delete", views.delete, name='/delete'),
    path("/alert", views.alert, name='/alert'),
    path("/select", views.select, name='/select'),
    path("/grab1", views.grab, name='/grab1'),
    path("/grab2", views.grab, name='/grab2'),
    path("/grab3", views.grab, name='/grab3'),
    path("", views.kitchen, name='/kitchen')
]