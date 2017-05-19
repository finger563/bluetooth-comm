import bluetooth
import time
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

if sys.argv[1] and sys.argv[1] == 'left':
    bd_addr = jcL
else:
    bd_addr = jcR

port = 1

'''
service_matches = bluetooth.find_service()

if len(service_matches) == 0:
    print "Couldn't connect to joy-con to get services"
    sys.exit(0)

for sm in service_matches:
    print "Got service:\n\tport: {}\n\tname: {}\n\thost: ".format(sm["port"], sm["name"], sm["host"])
    port = sm['port']

print "Got port: {}".format(port)
'''

print 'Connecting to {}'.format(bd_addr)
sock.connect((bd_addr, port))
print 'Connected to  {}'.format(bd_addr)

commands = [
    # service search attribute request
    "\x06\x00\x00\x00\x0d\x35\x03\x19\x11\x24\x00\x0f\x35\x03\x09\x02\x02\x00",
    # testing
]
'''
    "\x80\x01\xA2\x12\x00\x01\x1F",
    "\x80\x01\xA2\x15\x00\x01\x1F",

    "\x80\x92\x00\x01\x00\x00\x00\x00\x1F",
    "\x80\x01\x00\x01\x1F",
    "\x80\x02\x00\x01\x1F",
    "\x80\x03\x00\x01\x1F",
    "\x80\x91\x01\x00\x00\x00",
    "\x08\x00\x92\x00\x01\x1F",
    "\x08\x00\x92\x00\x01\x1F",
    "\x08\x00\x92\x00\x01\x1F",
    "\x19\x01\x03\x08\x00\x92\x00\x01\x00\x00\x00\x2D\x1F"
'''

for command in commands:
    print ""
    print "sent : {}".format(hexString(command))
    sock.send(command)
    data = sock.recv(1024)
    print "received : {}".format(hexString(data))

time.sleep(5)

print ""
print 'Disconnecting from {}'.format(bd_addr)
sock.close()
print 'Disconnected from  {}'.format(bd_addr)
