from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    input_name = request.GET.get("name", '')
    if input_name == '':
        return HttpResponse("Please input name=name")
    return render(request, "index.html", {'name': input_name})