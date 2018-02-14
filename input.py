with open("boot.py", "wt") as boot_file:
 line = ""
 while (True):
  line = raw_input()
  if line == "###END###":
    break
  boot_file.write(line+"\n")
  print("")

