import bluetooth
import sys

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

bd_addr = "7C:BB:8A:B8:8A:43"

service_matches = bluetooth.find_service()

if len(service_matches) == 0:
    print "Couldn't connect to joy-con to get services"
    sys.exit(0)

for sm in service_matches:
    print "Got service:\n\t{}\n\t{}\n\t".format(sm["port"], sm["name"], sm["host"])

port = bluetooth.get_available_port( bluetooth.RFCOMM )
print "Got port: {}".format(port)

sock.connect((bd_addr, port))

sock.send(0x01)

data = sock.recv(1024)
print "received [%s]" % data

sock.close()
