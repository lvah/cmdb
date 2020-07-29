import nmap
import telnetlib
import re
import paramiko


def get_active_hosts(host='172.25.254.250'):
    """Get IP is active or get network how many server is active"""
    # 实例化对象, portScanner()类用于实现对指定主机进行端口扫描
    nm = nmap.PortScanner()
    # 以指定方式扫描指定主机或网段的指定端口
    result = nm.scan(hosts=host, arguments='-n -sP')
    # print("扫描结果: ", result)
    # 返回nmap扫描的主机清单，格式为列表类型
    # print("主机清单: ", nm.all_hosts())
    return nm.all_hosts()


def is_ssh_up(host='172.25.254.250', port=22, timeout=5):
    try:
        # 实例化对象
        tn = telnetlib.Telnet(host=host, port=port, timeout=timeout)
        # read_until读取直到遇到了换行符或超时秒数。默认返回bytes类型，通过decode方法解码为字符 串。
        tn_result = tn.read_until(b"\n", timeout=timeout).decode('utf-8')
        # 通过正则匹配且忽略大小写， 寻找是否ssh服务开启。
        ssh_result = re.search(pattern=r'ssh', string=tn_result, flags=re.I)
    except Exception as e:
        print("%s ssh is down, Beacuse %s" % (host, str(e)))
        return False
    else:
        # 如果能匹配到内容， 说明ssh服务开启， 是Linux服务器.
        return True if ssh_result else False


def login_ssh_key(hostname='172.25.254.250', port=22, username='root',
                  private_key='./id_rsa', command='df -h'):
    # 0. Read private key file
    pkey = paramiko.RSAKey.from_private_key_file(private_key)
    # 1. Instance a Object
    client = paramiko.SSHClient()
    # 5.(tips) When first ssh connect server, have a question (Yes|no),
    # So we want auto answer
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 2. connect Server
    client.connect(hostname, port, username, pkey=pkey)
    # 3. execute command
    stdin, stdout, stderr = client.exec_command(command)
    # 4. print stdout result
    return stdout.read().decode('utf-8')


if __name__ == '__main__':
    # get_active_hosts()
    # print(is_ssh_up(host='172.25.254.100'))
    print(login_ssh_key())
