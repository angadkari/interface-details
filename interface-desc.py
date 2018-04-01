
from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.116.148',
    'username': 'ace',
    'password': 'cisco',
}

#all_devices = [R1]

#for devices in all_devices:
net_connect = ConnectHandler(**R1)
output = net_connect.send_command('show interface description')
print output 

