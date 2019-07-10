from pprint import pprint
file = open('devices','r')  # open string "devices" file
file_line = file.readline().strip()  # read line from the opened file

print "Print read content from device file:",file_line  # print the string

device_info = []   # create list "device_info"

# put 'file_line' string which that was read into device_info LIST
device_info = file_line.split(',')
print
print 'Print LIST:',device_info # print LIST (device_info)
pprint(device_info)

file.close()


