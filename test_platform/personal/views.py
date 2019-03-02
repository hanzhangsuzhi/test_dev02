from django.shortcuts import render
from django.http import HttpResponse

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
        elif username == "admin" and password == "admin123":
            return HttpResponse("登录成功")
        else:
            return render(request, "index.html", {
                "error": "登录失败"
            })


# def login_action(request):
#     """
#     处理登录的请求
#     """


