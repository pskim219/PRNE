# Create a LIST of DICTIONARIES to hold device information about multiple device
from pprint import pprint
devices = []

file = open('devices','r')
for line in file:
    device_info_list = line.strip().split(',') # Get device info into list

    device_info = {} # Create the inner dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['username'] = device_info_list[3]
    device_info['password'] = device_info_list[4]

print 'device_info:',device_info
print
pprint(device_info)

devices.append(device_info)
print
print

pprint(devices)

file.close()

