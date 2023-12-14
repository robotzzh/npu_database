from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name='/menu'),
    path("order", views.order, name='/order'),
    path("product", views.product, name='/product')
    # 添加其他路径...
]