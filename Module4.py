import datetime, pathlib, os, netmiko, getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

USER = input("Enter your username: ")
PASS = getpass.getpass("Enter your Password: ")

d = pathlib.Path.cwd()
ip_address = '192.168.11.11'
backup = 'csrBackup'
write = 'w'
openFile = open(backup, write)

netDevices = {'ip': ip_address, 'username': USER, 'password': PASS, 'device_type': 'cisco_ios'}

try:
    c = netmiko.ConnectHandler(**netDevices)
    output = c.send_command('show run')
    openFile.write(output)
    openFile.close()
except (AuthenticationException):
    print("An authentication error occured while connecting to:", netDevices['ip'])
except (SSHException):
    print("An error occured while connecting to devivce")
except (NetMikoTimeoutException):
    print("The device timed out while trying to connect")
