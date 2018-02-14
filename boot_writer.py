
#you must install PySerial module (pip install pySerial)
import serial

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
            print(line)
            serial.write(line)
            # ~ lf = serial.read(1)
            # ~ if lf != "\n":
               # ~ raise NoAckError()

serial = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=5)
send_python(serial, "input.py")
send_python(serial, "boot.py")
serial.close()
