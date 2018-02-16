#!/usr/bin/python

import webrepl_cli


import sys
if sys.version_info >= (3,0):
    import tkinter as tk
    import tkinter.filedialog as filedialog
else:
    import Tkinter as tk
    import tkFileDialog as filedialog

import os

default_port = 8266

class MainApplication(tk.Frame,object):
    def __init__(self, parent, *args, **kwargs):
        super(MainApplication,self).__init__(parent, *args, **kwargs)
        self.filename = ""

        label_ip = tk.Label(self, text="Destination ip").grid(sticky=tk.W)
        tk.Label(self, text="Password").grid(sticky=tk.W)
        label_src = tk.Label(self, text="Source file").grid(sticky=tk.W)
        tk.Label(self, text="Destination").grid(sticky=tk.W)
        self.dest_ip = tk.Entry(self)
        self.dest_ip.grid(row=0, column=1, sticky=tk.E)

        self.passwd = tk.Entry(self)
        self.passwd.grid(row=1, column=1)

        self.src = tk.Entry(self)
        self.src.grid(row=2, column=1)

        bt_select = tk.Button(parent, text="Select", command=self.select_file)
        bt_select.grid(row=2,column=2,sticky=tk.E)

        self.dest_file = tk.Entry(self)
        self.dest_file.grid(row=3, column=1)

        bt_send = tk.Button(parent, text="Send", command=self.send_file)
        bt_send.grid(row=4, columnspan=2, sticky=tk.W)

    def select_file(self):
        filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("python files","*.py"),("all files","*.*")))
        print (filename)
        # ~ self.src_label.config(text = filename)
        self.src.delete(0, tk.END)
        self.src.insert(0,filename)
        self.dest_file.delete(0, tk.END)
        self.dest_file.insert(0,os.path.basename(filename))

    def send_file(self):
        if self.dest_ip.get().find(":") == -1:
            port = 8266
            host = self.dest_ip.get()
        else:
            host, port = self.dest_ip.get.split(":")

        webrepl_cli.do_operation(host, port, self.passwd.get(), "put", self.src.get(), dst_file="")

if __name__ == "__main__":
    root = tk.Tk()
    # ~ MainApplication(root).pack(side="top", fill="both", expand=True)
    MainApplication(root).grid()
    root.mainloop()
