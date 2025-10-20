from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """首页视图，显示学生信息"""
    student_info = {
        'student_id': '20231201028',
        'name': '石珍',
        'class_name': '医学信息工程2023'
    }
    return render(request, 'hello/index.html', student_info)

def hello(request):
    """简单的hello视图"""
    return HttpResponse("Hello, 欢迎访问我的Django应用！")