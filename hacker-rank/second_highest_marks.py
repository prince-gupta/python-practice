#https://www.hackerrank.com/challenges/nested-list/problem

marksheet = []

for _ in range(0,int(input())):
    name = raw_input()
    marks = float(raw_input())
    marksheet.append([name, marks])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))