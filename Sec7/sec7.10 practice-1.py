from pprint import pprint

file = open('devices','r')  # read devices file
file_line = file.readline().strip()  # read one line from the open file & strip any space
print
print file_line
print
device_info_list = file_line.split(',')   # create list on the fly and put content with commas

print device_info_list

device_info_dict = {} # create blank dictionary
device_info_dict['name'] = device_info_list[0]  # create key value "name" == value (1st from list)
device_info_dict['os-type'] = device_info_list[1] # create key value os-type and value of 2nd from list
device_info_dict['ip'] = device_info_list[2]
device_info_dict['username'] = device_info_list[3]
device_info_dict['password'] = device_info_list[4]

print "show dictionary which was filled with list:",device_info_dict
print
pprint(device_info_dict)

file.close()

