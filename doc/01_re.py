# regular expression
import re
pattern = r'ssh'
string = """
Trying 172.25.254.250...
Connected to 172.25.254.250.
Escape character is '^]'.
SSH-2.0-OpenSSH_7.8
"""
# from string to search pattern, and ignore case(lower ssh or upper ssh all is ok)
result = re.search(pattern, string, flags=re.IGNORECASE)
print(result)
