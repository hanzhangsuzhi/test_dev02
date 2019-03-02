from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def say_hello(request):
    input_name = request.POST.get("name", '')
    if input_name == '':
        return HttpResponse("Please input name=name")
    return render(request, "index.html", {'name': input_name})

def index(request):
    """
    登录首页
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == '' or password == '':
            return render(request, "index.html", {
                "error": "用户名或密码不可为空"})
        user = auth.authenticate(username=username, password=password)

        print("user-->", user)
        if user is None:
           return render(request, "index.html", {
                "error": "登录失败"
            })
        else:
            auth.login(request, user)# 记录用户的登录状态
            return HttpResponseRedirect("/manage/")


# def login_action(request):
#     """
#     处理登录的请求
#     """

# @login_required
def manage(request):
    return render(request, "manage.html")

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")

