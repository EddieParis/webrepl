
#you must install PySerial module (pip install pySerial)
import serial

import time
import sys
if sys.version_info >= (3,0):
    import tkinter as tk
    import tkinter.filedialog as filedialog
else:
    import Tkinter as tk
    import tkFileDialog as filedialog

import argparse

class NoAckError(Exception):
    pass

def send_python(serial, src_name, args_dict, check=False):
    with open(src_name, "rt") as input_file:
        while True:
            # ~ line=input_file.readln()
            line=input_file.readline()
            line = line.format(**args_dict)
            if line == "":
                break
            elif check:
                continue
            elif line == "###BACKSPACE\n":
                serial.write(b"\x08")
                continue
            else:
                print(line)
                serial.write(line+'\r\n')
            #~ time.sleep(.01)
            lf = ""
            while lf != "\n":
                lf = serial.read(1)

parser = argparse.ArgumentParser(description='Micropython serial file writer.')


parser.add_argument('-s', '--serial', metavar='serial', type=str, help='serial device', nargs=1, required=True)

parser.add_argument('-p', '--param', metavar='param', type=str, help='parameter', nargs='*')

parser.add_argument('-b', '--baudrate', metavar='baudrate', type=int, nargs=1, default=[115200],
                help='baurate for serial, default 115200')

parser.add_argument("file", type=str, help="file to send")

args = parser.parse_args()

print args

transfered_args = { 'dest_name':'boot.py'}
for param in args.param:
    name, value = param.split('=')
    transfered_args.update( {name:value} )

send_python(serial, "input.py", transfered_args, True)
send_python(serial, "boot.py", transfered_args, True)

serial = serial.Serial(port=args.serial[0], baudrate=args.baudrate[0], timeout=1)
send_python(serial, "input.py", transfered_args)
send_python(serial, "boot.py", transfered_args)
serial.close()
