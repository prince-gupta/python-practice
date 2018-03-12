# You have a record of N students. Each record contains the student's name,
# and their percent marks in Maths, Physics and Chemistry.
# The marks can be floating values. The user enters some integer N followed by the names and marks for N students.
# You are required to save the record in a dictionary data type. The user then enters a student's name.
# Output the average percentage marks obtained by that student, correct to two decimal places.
#
# Input Format
#
# The first line contains the integer N , the number of students.
# The next N lines contains the name and marks obtained by that student separated by a space.
# The final line contains the name of a particular student previously listed.
#
# Constraints
#
# 2 <= N <= 10
# 0 <= Marks <= 100
#
# Output Format
#
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#
# Sample Input 0
#
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0
#
# 56.00
# Explanation 0
#
# Marks for Malika are {52,56,60} whose average is ( 52 + 56 + 60 )/3
#
# Sample Input 1
#
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# Sample Output 1
#
# 26.50


class MarksAverage:
    marksheet = {}

    def take_input(self):
        for _ in range(int(raw_input("Enter number of students you want save :"))):
            line = raw_input().split()
            name, scores = line[0], line[1:]
            MarksAverage.marksheet[name] = map(float, scores)
        return

    def print_average(self):
        MarksAverage().take_input()
        name = raw_input("Enter name of student to calculate average : ")
        print ("{0:.2f}".format(sum(MarksAverage.marksheet[name])/len(MarksAverage.marksheet[name])))


MarksAverage().print_average()