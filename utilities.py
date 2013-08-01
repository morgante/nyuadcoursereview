# -*- coding: utf-8 -*-
filename= raw_input('Enter filename: ')

f = open(filename, "r")

mylist=[]

for line in f:
    line2 = line.strip('\n')
    mylist.append(line2)

f.close()
print mylist


