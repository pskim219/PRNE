from pprint import pprint

# Create three dictionaries holding device information for specific devices
dev30 = {'name':'xrv-0','ip':'10.1.1.30','user':'cisco'}
dev31 = {'name':'xrv-1','ip':'10.1.1.31','user':'cisco'}
dev32 = {'name':'xrv-2','ip':'10.1.1.32','user':'cisco'}

print "Print new dictionary for dev30",dev30
print "Print new dictionary for dev31",dev31
print "Print new dictionary for dev32",dev32
print
print

pprint (dev30)
pprint (dev31)
pprint (dev32)

# Create a list to hold information about all of my devices created above
dev_list = [i for i in range(3)]
dev_list[0] = dev30 # sets list item 0 to dictionary dev30
dev_list[1] = dev31 # sets list item 1 to dictionary dev31
dev_list[2] = dev32 # sets list item 2 to dictionary dev32


# Create a list to hold information about all of my devices created above
# dev_list = [i for i in range(3)]
# dev_list[0] = dev30 # sets list item 0 to dictionary dev30
# dev_list[1] = dev31 # sets list item 1 to dictionary dev31
# dev_list[2] = dev32 # sets list item 2 to dictionary dev32
# print
# print

#Instead of creating a list with 3 items and then assigning the dictionaries to those items,
# you could have created an empty set and used the append function to add the dictionaries to the list.
# The code would look similar to:

dev_list = []
dev_list.append(dev30) # sets list item 0 to dictionary dev 30
dev_list.append(dev31) # sets list item 1 to dictionary dev31
dev_list.append(dev32) # sets list item 2 to dictionary dev3
print
print 'print device list that created by LIST'

pprint(dev_list)

