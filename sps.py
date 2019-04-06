#!/usr/bin/python3
#!Desenvolvido por:_carlosnericorreia_
#!email: hackerama@protonmail.com	
#!SPS - Simple TCP Port Scanner - versao 1.0t

print ("\n\n[+] Inciando o SPS - TCP Port Scanner [+]\n")

import socket
from threading import *
import time

def scan(porta):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	res = s.connect_ex((ip, porta),)
	if res == 0:
		print ("[+] Porta Aberta Encontrada: %d"% porta)
	s.close()
		

ip = input("Digite o IP que deseja escanear: ")
print()

time_start = time.time()
for porta in range(1, 1024):
	if active_count() > 700:     #Evita um Runtime Error
		time.sleep(1)
	t = Thread(target=scan, args=(porta,))
	t.setDaemon(True)	
	t.start()

print("\n"*2)	
total_time= time.time() - time_start	
print ("Scan Finalizado em %.2f segundos" % total_time)
