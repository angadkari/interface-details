#! /usr/bin/env python

import getpass
import sys
import telnetlib
#ask  for username and password
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

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

	tn.write("terminal length 0\n")
# terminal length 0 to show running config output in one go
	tn.write("show run \n")
	tn.write("exit\n")

	readoutput = tn.read_all()
	saveoutput = open("switch" + HOST, "w")
	saveoutput.write(readoutput)

