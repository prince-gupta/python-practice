def printinfo(age, name="Not Provided"):
    "This function will print passed info of a person with default name as 'Not Provided'"
    print "Name : ", name
    print "Age : ", age
    return;


printinfo(name="Mike", age=34)


def printinfoWithVarArgs(arg1, *varargs):
    print arg1
    for elem in varargs:
        print elem
    return;


printinfoWithVarArgs(10)
printinfoWithVarArgs(10, 70, 8, 87)

sum = lambda arg1, arg2: arg1 + arg2

print "Sum of 20 and 45 is : ", sum(20, 45)

printUpdatedInfo = lambda name, age: printinfo(age=age + 20, name=(name + "Updated"))

print printUpdatedInfo("Prince ", 9)
