import datetime, pathlib, os, netmiko, getpass

USER = input("Enter your username: ")
PASS = getpass.getpass("Enter your Password: ")

d = pathlib.Path.cwd()
ip_address = '192.168.11.11'
backup = 'csrBackup'
write = 'w'
openFile = open(backup, write)

netDevices = {'ip': ip_address, 'username': USER, 'password': PASS, 'device_type': 'cisco_ios'}

c = netmiko.ConnectHandler(**netDevices)

output = c.send_command('show run')

openFile.write(output)
openFile.close()
