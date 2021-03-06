#!/usr/bin/python
import sh
import sys

out = sh.gphoto2("--get-config=imagequality")
#1: print all the image formats, both current (marked with N) and possible (marked with P)
#2: print the current image format
#3: print all the available image formats
if sys.argv[1] == "1":
    for line in out.splitlines():
        if b'Current:' in line:
            print "N", line.replace("Current: ", "")
            
        elif b'Choice:' in line:
            print "P", line.replace("Choice:", "").split(" ")[2]
            
elif sys.argv[1] == "2":
    for line in out.splitlines():
        if b'Current:' in line:
            print line.replace("Current: ", "")
            sys.exit(0)
            
elif sys.argv[1] == "3":
    for line in out.splitlines():
        if b'Choice:' in line:
            print  line.replace("Choice:", "").split(" ")[2]
