import os

flag = input("1: For main screen\n2: All screens\n")
print(flag)
if flag == "1":
    os.system("displayswitch.exe /internal")
if flag == "2":
    os.system("displayswitch.exe /extend")
