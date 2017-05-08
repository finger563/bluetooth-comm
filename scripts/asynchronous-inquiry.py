import bluetooth
import select

class MyDiscoverer(bluetooth.DeviceDiscoverer):
    
    def pre_inquiry(self):
        self.done = False
    
    def device_discovered(self, address, device_class, name):
        print "%s - %s" % (address, name)

        '''
        services = bluetooth.find_service(address=address)

        if len(services) > 0:
            print("found %d services on %s" % (len(services), sys.argv[1]))
            print("")
        else:
            print("no services found")

        for svc in services:
            print("Service Name: %s"    % svc["name"])
            print("    Host:        %s" % svc["host"])
            print("    Description: %s" % svc["description"])
            print("    Provided By: %s" % svc["provider"])
            print("    Protocol:    %s" % svc["protocol"])
            print("    channel/PSM: %s" % svc["port"])
            print("    svc classes: %s "% svc["service-classes"])
            print("    profiles:    %s "% svc["profiles"])
            print("    service id:  %s "% svc["service-id"])
            print("")
        '''
            
    def inquiry_complete(self):
        self.done = True

d = MyDiscoverer()
d.find_devices(lookup_names = True)

readfiles = [ d, ]

while True:
    rfds = select.select( readfiles, [], [] )[0]

    if d in rfds:
        d.process_event()

    if d.done: break
