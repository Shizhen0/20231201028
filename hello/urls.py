from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 首页，显示学生信息
    path('hello/', views.hello, name='hello'),  # 简单的hello页面
]