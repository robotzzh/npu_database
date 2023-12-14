from django.urls import path
from . import views

urlpatterns = [
    path("", views.finder, name='/finder'),
    # 添加其他路径...
]