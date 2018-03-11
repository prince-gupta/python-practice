print """Hello,Python!"""

print "\n\nPrint variable example"

a, b, c = 1, 2, 'Jhon'

print a
print b
print c

print "\n\nPrint string example"

str = "Hello, World !"

print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + "TEST"

print "\n\nPrint list example"

list = ['abcd', 786, 2.23, 'jhon', 70.2]
tinyList = [123, 'smith']

print list
print list[0]
print list[2:3]
print list[2:]
print tinyList * 2
print list + tinyList

print "\n\nPrint tuple example"

tuple = ('abcd', 786, 2.23)
tinyTuple = (123, 'Hello')

print tuple
print tuple[0]
print tuple[2:5]
print tuple[2:]
print tuple + tinyTuple

print "\n\nPrint dictionary example"

dict = {'name': 'john', 'code': 453, 'address': 'NewYork'}

print dict['name']
print dict
print dict.keys()
print dict.values()



str1 = "this is string example....wow!!!"
print "\n\nstr1.center(40, 'a') : ", str1.center(40, 'a')



var1 = 'Hello World!'
print "\n\nUpdated String :- ", var1[:6] + 'Python \a'

print 'C:\\Folder'

print r'C:\\Folder'
print R'C:\\Folder'
