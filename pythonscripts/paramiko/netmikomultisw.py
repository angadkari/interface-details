#! /usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_sw4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.116.204',
    'username': 'ace',
    'password': 'cisco',
}

iosv_l2_sw5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.116.205',
    'username': 'ace',
    'password': 'cisco',
}

iosv_l2_sw6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.116.206',
    'username': 'ace',
    'password': 'cisco',
}

all_devices = [iosv_l2_sw4, iosv_l2_sw5, iosv_l2_sw6]

for devices in all_devices:

	net_connect = ConnectHandler(**devices)
	#print "Connecting device" +  str(**ip)
	for n in range (2,5):
    		print "Creating VLAN " + str(n)
    		config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    		output = net_connect.send_config_set(config_commands)
		print output 
