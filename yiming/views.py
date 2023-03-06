from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# newapp/views.py

from django.http import HttpResponse


def call_chatGpt(request):
    if request.method == 'POST':
        # 处理POST请求
        return HttpResponse('POST请求成功')
    else:
        # 处理其他类型的请求
        return HttpResponse('不支持的请求类型')
