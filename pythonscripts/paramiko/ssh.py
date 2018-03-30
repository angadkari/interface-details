#! /usr/bin/env python

import getpass
import sys
import telnetlib
#ask  for username and password
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()
ssh = getpass.getpass()

#open a file called switches
f = open("switches")


for line in f:
	print "getting running config from  switch" + (line)
	HOST = line.strip()
#strip() is used to remove any redundant white spaces in the file
#telnet into the  devices from file switches
	tn  = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
    		tn.read_until("Password: ")
    		tn.write(password + "\n")
	tn.write("conf t\n")
	tn.write("do terminal length 0 \n")
	tn.write("ip domain name akhil.local\n")
	tn.write("crypto key generate rsa \n")
	if ssh:
        	tn.read_until("Do you really want to replace them? [yes/no]:")
            	tn.write(ssh + "\n")

	tn.write("1024\n")
	tn.write("exit\n")
	print tn.read_all()
	

