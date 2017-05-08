import bluetooth

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

bd_addr = bluetooth.read_local_bdaddr()
port = 0x1001

sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
