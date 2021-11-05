#!/usr/bin/env python3

import os
import sys


n = int(sys.argv[1]) if len(sys.argv) == 2 else 1 

home = "/home/gchen1/Documents/micro-aevol2"
os.chdir(home + "/build")

cmd_compile = "rm -rf /home/gchen1/Documents/micro-aevol2/build/* &&"
cmd_compile += "cmake -S .. -B . -DUSE_OMP=on -DDO_TRACES=on &&"
cmd_compile += "make -C ."
cmd_execute = "./micro_aevol_cpu"
cmd_analyse = "./../getStats.py;"

print("Compiling...")
os.system(cmd_compile)

for i in range(n):
    print("Executing {} starts...".format(i))
    os.system(cmd_execute)
    exitToken = os.system(cmd_analyse)
    if(exitToken == 1):
        print("Open file failed.\n", os.error) 
        sys.exit(1)
    print("Executing {} ends...".format(i))

