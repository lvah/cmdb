from django.shortcuts import render
from django.http import HttpResponse

from hostinfo.models import Server
from hostinfo.utils import get_active_hosts, is_ssh_up, login_ssh_key
from CMDB.settings import commands

# Create your views here.
"""
需求:
    1. 用户访问http://ip/hostscan/返回一个html页面
    表单[填写的是需要扫描的主机IP或者网段，用逗号分隔开](开始扫描按钮)
    
    2. 用户填写好网段/IP之后，将填写的信息提交给服务器路由处理(/hostscan/)
    POST方法;
"""


def hostscan(request):
    # print(request.method)
    if request.method == 'POST':
        # how to get form post data
        # {'scanhosts': '172.25.254.250,172.25.254.0/24'}
        # print(request.POST)
        """
        # 1. Get Dictionary key
        request.POST.get('scanhosts')
  
        # 2. split ip and network
        request.POST.get('scanhosts')[0].split(',')
        **
        s = "172.25.254.250,172.25.34.0/24"
        s.split(',')
        Out[3]: ['172.25.254.250', '172.25.34.0/24']
        """
        # ['172.25.254.250', '172.25.34.0/24']
        scanhosts = request.POST.get('scanhosts').split(',')
        servers = []

        for scanhost in scanhosts:
            print("正在扫描%s......" % (scanhost))
            # 获取所有可以ping通的主机IP
            active_hosts = get_active_hosts(scanhost)
            for host in active_hosts:
                if is_ssh_up(host):
                    # Instance Server(ORM)===> MySQL
                    # If ip exists ,How to manage?
                    server = Server()
                    server.IP = host
                    """
                    commands = {
                    'hostname': 'hostname',
                    'os_type': 'uname',
                    'os_distribution': 'dmidecode -s system-manufacturer',
                    'os_release': 'cat /etc/redhat-release',
                    'MAC': 'cat /sys/class/net/`[^vtlsb]`*/address',
                }
                    """
                    for command_name, command in commands.items():
                        # command_name="os_type", command="uname"
                        result = login_ssh_key(hostname=host, command=command)
                        # set server object attribute
                        setattr(server, command_name, result)
                    # save to mysql
                    server.save()
                    # Now Scan host info
                    servers.append(server)
        return render(request, "hostinfo/hostscan.html", {'servers': servers})
    return render(request, 'hostinfo/hostscan.html')
