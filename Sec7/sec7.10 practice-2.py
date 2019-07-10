# Create a LIST of DICTIONARIES to hold device inforemation about multiple device

from pprint import pprint

file = open('devices','r')
#file_line = file.readline().strip()
# Open the file and read in the information one line at a time.
# Put the information for each device into a list.
for line in file:  # file is
    device_info_list = line.strip().split()
print
print device_info_list
