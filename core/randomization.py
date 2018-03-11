import random

list = [12, 4, 34, 54, 223, 55, 25, 66, 43, 667, 432]

print "choice(list) : ", random.choice(list)
print "choice('A lazy dog jumps over a crazy fox')", random.choice("A lazy dog jumps over a crazy fox")

#   random.seed(10)
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)


print "Shuffling a list "

print random.shuffle(list)

print list

print "Random Float uniform(5, 10) : ",  random.uniform(5, 10)
print "Random Float uniform(7, 14) : ",  random.uniform(7, 14)
