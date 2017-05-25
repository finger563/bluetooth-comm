import bluetooth
import time
import sys

def hexString(s, delim=' '):
    return delim.join('{:02x}'.format(ord(x)) for x in s)

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

jcL = "98:B6:E9:8B:78:B9"
jcR = "7C:BB:8A:B8:8A:43"

if len(sys.argv) > 1 and sys.argv[1] == 'left':
    bd_addr = jcL
else:
    bd_addr = jcR

port = 1 #0x1001

print 'Connecting to {}'.format(bd_addr)
sock.connect((bd_addr, port))
print 'Connected to  {}'.format(bd_addr)

def send(data):
    print ""
    print "sent : {}".format(hexString(data))
    sock.send(data)

def recv():
    data = sock.recv(1024)
    print "received : {}".format(hexString(data))

commands = [
    # service search attribute request HID
    "\x06\x00\x00\x00\x0f\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x00",
    # service search attribute request HID continuation
    "\x06\x00\x01\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x00\x26",
    # service search attribute request HID continuation
    "\x06\x00\x02\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x00\x4C",
    # service search attribute request HID continuation
    "\x06\x00\x03\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x00\x72",
    # service search attribute request HID continuation
    "\x06\x00\x04\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x00\x98",
    # service search attribute request HID continuation
    "\x06\x00\x05\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x00\xBE",
    # service search attribute request HID continuation
    "\x06\x00\x06\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x00\xE4",
    # service search attribute request HID continuation
    "\x06\x00\x07\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x01\x0A",
    # service search attribute request HID continuation
    "\x06\x00\x08\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x01\x30",
    # service search attribute request HID continuation
    "\x06\x00\x09\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x01\x56",
    # service search attribute request HID continuation
    "\x06\x00\x0A\x00\x11\x35\x03\x19\x11\x24\xff\xff\x35\x05\x0a\x00\x00\xff\xff\x02\x01\x7C",
]

'''
LOG FROM SUCCESSFUL CONNECTION TO JOYCON AND HANDSHAKING TO GET DATA:

# RECV Conn request (HID-Control, SCID 0x0040)
02 02 04 00 11 00 40 00
# SEND Conn response - success (SCID 0x0040 DCID 0x0040)
03 02 08 00 40 00 40 00 00 00 00
# SEND Configure request (DCID 0x0040)
04 02 04 00 40 00 00 00
# RECV Configure request (DCID 0x0040)   ## MTU (0x01) to 800 (0x0320)
04 03 08 00 40 00 00 00 01 02 20 03
# SENT Configure response success (SCID 0x0040)
05 03 0a 00 40 00 00 00 00 00 01 02 20 03
# RECV Configure response success (SCID 0x0040)
05 02 06 00 40 00 00 00 00 00
# RECV Connection request (HID-interrupt, SCID 0x0041)
02 04 04 00 13 00 41 00
# SENT Conn response pending (SCID 0x0041)
03 04 08 00 41 00 41 00 01 00 02 00
# SENT Conn response success (SCID 0x0041, DCID 0x0041)
03 04 08 00 41 00 41 00 00 00 00 00
# SENT Configure request (DCID 0x0041)
04 03 04 00 41 00 00 00
# RECV Configure request (DCID 0x0041)  ## MTU (0x01) to 800 (0x0320)
04 05 08 00 41 00 00 00 01 02 20 03
# SENT Configure response success (SCID 0x0041)
05 05 0a 00 41 00 00 00 00 00 01 02 20 03
# RECV Configure response success (SCID 0x0041)
05 03 06 00 41 00 00 00 00 00

# RECV DATA - Input - unknown type
a1 3f 00 00 05 00 80 00 80 00 80 00 80
# RECV DATA - Input - unknown type
a1 3f 00 00 08 00 80 00 80 00 80 00 80

# SENT DATA - Output - Keyboard - LEDS: none
A2 01 00

# RECV DATA - Input - unknown type
a1 21 b5 8e ......
'''


'''
# Connection request
"\x02\x48\x04\x00\x01\x00\x42",

# info request extended features
"\x0a\x01\x02\x00\x02\x00",

# testing HID
"\xa2\x01\x00",  # should be Keyboard LEDs set to 0

# service search attribute request
"\x06\x00\x00\x00\x0d\x35\x03\x19\x11\x24\x00\x0f\x35\x03\x09\x02\x02\x00",
'''

for command in commands:
    send(command)
    recv()

# SEND Information Request (Extended Features Mask)
send("\x0a\x01\x02\x00\x02\x00")

# RECV Conn request (HID-Control, SCID 0x0040)
"\x02\x02\x04\x00\x11\x00\x40\x00"
recv()

# SEND Conn response - success (SCID 0x0040 DCID 0x0040)
send("\x03\x02\x08\x00\x40\x00\x40\x00\x00\x00\x00")

# SEND Configure request (DCID 0x0040)
send("\x04\x02\x04\x00\x40\x00\x00\x00")

# RECV Configure request (DCID 0x0040)   ## MTU (0x01) to 800 (0x0320)
"\x04\x03\x08\x00\x40\x00\x00\x00\x01\x02\x20\x03"
recv()

# SENT Configure response success (SCID 0x0040)
sock.send("\x05\x03\x0a\x00\x40\x00\x00\x00\x00\x00\x01\x02\x20\x03")

# RECV Configure response success (SCID 0x0040)
"\x05\x02\x06\x00\x40\x00\x00\x00\x00\x00"
recv()

# RECV Connection request (HID-interrupt, SCID 0x0041)
"\x02\x04\x04\x00\x13\x00\x41\x00"
recv()

# SENT Conn response pending (SCID 0x0041)
send("\x03\x04\x08\x00\x41\x00\x41\x00\x01\x00\x02\x00")

# SENT Conn response success (SCID 0x0041, DCID 0x0041)
send("\x03\x04\x08\x00\x41\x00\x41\x00\x00\x00\x00\x00")

# SENT Configure request (DCID 0x0041)
send("\x04\x03\x04\x00\x41\x00\x00\x00")

# RECV Configure request (DCID 0x0041)  ## MTU (0x01) to 800 (0x0320)
"\x04\x05\x08\x00\x41\x00\x00\x00\x01\x02\x20\x03"
recv()

# SENT Configure response success (SCID 0x0041)
send("\x05\x05\x0a\x00\x41\x00\x00\x00\x00\x00\x01\x02\x20\x03")

# RECV Configure response success (SCID 0x0041)
"\x05\x03\x06\x00\x41\x00\x00\x00\x00\x00"
recv()

# RECV DATA - Input - unknown type
"\xa1\x3f\x00\x00\x05\x00\x80\x00\x80\x00\x80\x00\x80"
recv()

# RECV DATA - Input - unknown type
"\xa1\x3f\x00\x00\x08\x00\x80\x00\x80\x00\x80\x00\x80"
recv()

# SENT DATA - Output - Keyboard - LEDS: none
"\xA2\x01\x00"

# RECV DATA - Input - unknown type
recv()


time.sleep(5)

print ""
print 'Disconnecting from {}'.format(bd_addr)
sock.close()
print 'Disconnected from  {}'.format(bd_addr)
