import os

try:
    fo = open("./test.txt", "wb+")
    print "File Name : ", fo.name
    print "File is closed ? : ", fo.closed
    print "Opening Mode : ", fo.mode
    fo.write("Java is also an awesome language, we should learn it.")

    fo.seek(0, 0)

    str = fo.read(10)

    print str

    position = fo.tell()
    print "Current file position : ", position
except IOError, Argument:
    print  "Error: can\'t find file or read data", Argument

else:
    print "Content written successfully."
    fo.close()




os.rename("./test.txt","./test2.txt");