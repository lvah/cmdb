from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
"""
需求:
    1. 用户访问http://ip/hostscan/返回一个html页面
    表单[填写的是需要扫描的主机IP或者网段，用逗号分隔开](开始扫描按钮)
    
    2. 用户填写好网段/IP之后，将填写的信息提交给服务器路由处理(/hostscan/)
    POST方法;
"""

def hostscan(request):
    print(request.method)
    if request.method == 'POST':
        # how to get form post data
        print(request.POST)
        return  HttpResponse("Upload scan host")
    return  render(request, 'hostinfo/hostscan.html')

