"""The mode r+ means it can both read and write in a file simultaneously.
The same applies for the w+ mode.
whereas for the a+ mode it appends and reads data in the file .
the examples are as follows."""

with open("myfile.txt","r+") as myfile:
    myfile.write("This is the updated data using r+ mode")
    print(myfile.read())

#The w+ mode
with open("myfile.txt","w+") as myfile:
    myfile.write("This is the updated data using w+ mode")
    print(myfile.read())

#The a+ mode
with open("myfile.txt","a+") as myfile:
    myfile.write("This is the updated data using a+ mode")
    print(myfile.read())



