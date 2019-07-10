# Create a Dictionary to Hold Device Information.

from pprint import pprint

file = open('devices','r')
file_line = file.readline().strip()  # create LIST

device_info_list = file_line.split(',')
print
print device_info_list

device_info = {}
device_info['name'] = device_info_list[0]
device_info['os-type'] = device_info_list[1]
device_info['IP'] = device_info_list[2]
device_info['username'] = device_info_list[3]
device_info['password'] = device_info_list[4]


print
print device_info
print
pprint(device_info)
