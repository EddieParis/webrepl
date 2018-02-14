
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

class NoAckError(Exception):
    pass


def send_python(serial, file_name):
    with open(file_name, "rt") as input_file:
        while True:
            # ~ line=input_file.readln()
            line=input_file.readline()
            if line == "":
                break
            elif line == "###BACKSPACE\n":
                serial.write(b"\x08")
                continue
            else:
                print(line)
                serial.write(line+"\r")
            #~ time.sleep(.01)
            lf = ""
            while lf != "\r":
                lf = serial.read(1)

serial = serial.Serial(port="COM8", baudrate=115200, timeout=5)
send_python(serial, "input.py")
send_python(serial, "boot.py")
serial.close()
