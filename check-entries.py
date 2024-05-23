import re
def checkstr(str):
    strfound = 0
    strsaved = ""
    myfile = open("config.1", "r")
    myline = myfile.readline()
    while myline:
        myline1 = " ".join(myline.split())
        if str in myline1:
            strfound=1
            strsaved=myline1
        myline = myfile.readline()
    if strfound == 0:
        print("-")
    else:
        print(strsaved)
        strsaved = ""
    myfile.close()

myfile = open("config-orig", "r")
myline = myfile.readline()
while myline:
    myline1 = " ".join(myline.split())
    checkstr(myline1)
    myline = myfile.readline()
myfile.close()
