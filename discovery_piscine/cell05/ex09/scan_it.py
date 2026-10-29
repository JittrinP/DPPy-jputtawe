#!/usr/bin/env python3
import re ,sys

if len(sys.argv) != 3 :
    print("none")
else :
    if len(re.findall(sys.argv[1], sys.argv[2])) == 0 :
        print("none")
    else :
        print(len(re.findall(sys.argv[1], sys.argv[2])))