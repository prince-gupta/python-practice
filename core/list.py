list = ['physics', 'chemistry', 1997, 1993]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print list[2:4]

print list2

del list2[len(list) - 1]

print list2

print 100 in list2

for elem in list:
    print 'Element : %s' % elem

print list[-3]

print list[1:]

print cmp(list, list2)

list2.append('chemistry')

print list2

tuple = (1, 2, 3, 4, 5, 6, 7, 8)

list.extend(tuple)
print list

list.insert(3, 'physics')

print list

list.sort()

print list
