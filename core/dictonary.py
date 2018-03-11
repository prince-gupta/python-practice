dictonary = {(1, 2, 3, 4, 5): 'Tuple', (1, 2, 3, 4, 5): 'tuple2'}

print dictonary

dictonary2 = {'Name': 'Jhon', 'Age': 7}

print cmp(dictonary,dictonary2)

list = ['Name', 'Age', 'Address']
dict = dict.fromkeys(list, 'Not Assigned')
print dict

print dictonary2.items()
