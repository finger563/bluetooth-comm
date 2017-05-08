import bluetooth

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    print "Found: {}".format(bluetooth.lookup_name( bdaddr ))
    print "     : {}".format(bdaddr)
