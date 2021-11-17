#!/usr/bin/env python3

import os
import sys


n = int(sys.argv[1]) if len(sys.argv) >= 2 else 1 
mode = sys.argv[2] if (len(sys.argv) >= 3 ) else 'n'
fileName = sys.argv[3] if (len(sys.argv) >= 4 ) else 'example.csv'

home = "/home/gchen1/Documents/micro-aevol2"
os.chdir(home + "/build")

cmd_compile = "rm -rf /home/gchen1/Documents/micro-aevol2/build/* &&"
cmd_compile += "cmake -S .. -B . -DUSE_OMP=on -DDO_TRACES=on &&"
cmd_compile += "make -C ."

if(mode == 'c'):
    print("Compiling...")
    os.system(cmd_compile)
else:
    print("Continu with out recompiling...")

cmd_execute = "rm ./execTime.txt; ./micro_aevol_cpu"
cmd_analyse = "./../getStats.py " + fileName + ";"

cmd_check = 'res="init";'
cmd_check += "res=$(diff ./backup/backup_1000.zae ./../backup/backup_1000.zae);"
cmd_check += 'if ["$res" == ""]; then echo "the result is valid"; else exit 1; fi;'
exit = os.system(cmd_check)

if exit == 0:
    for i in range(n):
        print("Executing {} starts...".format(i))
        os.system(cmd_execute)
        exitToken = os.system(cmd_analyse)
        if(exitToken == 1):
            print("Open file failed.\n", os.error) 
            sys.exit(1)
        print("Executing {} ends...".format(i))
else: print("The modification is not valid, check diff file")

