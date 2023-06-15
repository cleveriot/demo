# Python warm-up : Basic notions
#
# 1- import modules
# 2- lists
# 3- tuples
# 4- dictionaries
# 5- for loops
# 6- if statement
# 7- read and write files
# 8- exceptions
# 9- logging
# 10- 

# -----------------------
# 1-) IMPORT MODULES
#
# usage1: import <module>
# usage2: from <module> import <class/function/variable>
# usage3: from <module> import <class/function/variable> as mymodule

import os
import socket

#See what modules contains an put items into a list
content_os = dir(os)
content_socket = dir(socket)

#print(content_os)
#print(content_socket)

# get logged in user
login = os.getlogin()
#print(login)

# get environment variable ‘HOME’ directory and current directory 'PWD'
home = os.getenv('HOME')
cwd = os.getenv('PWD')
#print(home)
#print(cwd)

## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()

## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

## printing the hostname and ip_address
#print(f"Hostname: {hostname}")       #alternative: print(“Hostname: {}”.format(hostname) )
#print(f"IP Address: {ip_address}")


# -----------------------
# 2-) LISTS
#
content_os = dir(os)
# print(content_os)

list1 = ['item1', 'item2', 3, 'new_item', ['sublist1','sublist2'], {'key': 'value'} ]
# print(list1)

# #Get an item list
# print(content_os[0])
# print(list1[3])
# print(list1[4])
# print(list1[4][0])

#Iterate over a list
# for c in content_os:
#     print(c)

#Check if a list contains a given item:
# if 'item2' in list1:
#   print("item2 exist in list1")

#Create a list from another list  (list comprehension)
# new_list = [ x for x in list1 if type(x) == str ]
# print(new_list)

#Add a new item to a list
list1.append('appeded_item')
# print(list1)

#Change an item list
list1[0] = 'first_item'
# print(list1)

#Remove an item list and assign it to a variable
removed = list1.pop(0)
# print(list1)
# print(removed)

#Check the size of a list
# print( len(list1) )
# print( len(content_os) )




# -----------------------
#