import bluetooth
import sys

def hexString(s, delim=' '):
    return delim.join('{:02x}'.format(ord(x)) for x in s)

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

'''
98:B6:E9:8B:78:B9	Joy-Con (L)
7C:BB:8A:B8:8A:43	Joy-Con (R)
'''

jcL = "98:B6:E9:8B:78:B9"
jcR = "7C:BB:8A:B8:8A:43"

bd_addr = "7C:BB:8A:B8:8A:43"

service_matches = bluetooth.find_service()

if len(service_matches) == 0:
    print "Couldn't connect to joy-con to get services"
    sys.exit(0)

for sm in service_matches:
    print "Got service:\n\tport: {}\n\tname: {}\n\thost: ".format(sm["port"], sm["name"], sm["host"])
    port = sm['port']

print "Got port: {}".format(port)

sock.connect((bd_addr, port))

print 'Connected'

commands = [
    "\x80\x01\x00\x01\x1F",
    "\x80\x02\x00\x01\x1F",
    "\x80\x03\x00\x01\x1F",
    "\x80\x91\x01\x00\x00\x00",
    "\x08\x00\x92\x00\x01\x1F",
    "\x08\x00\x92\x00\x01\x1F",
    "\x08\x00\x92\x00\x01\x1F",
    ]

for command in commands:
    print "\nsent : " + hexString(command)
    sock.send(command)
    data = sock.recv(1024)
    print "received : " + hexString(data)

sock.close()
