with open("{dest_name}", "wt") as boot_file:
line = ""
while (True):
line = input()
if line == "###END###":
break
###BACKSPACE
dummy=boot_file.write(line+"\n")



