class Employee:
    'Class to showcase class hierarchy in python'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

    def display_count(self):
        print "Total number of Employee : %d" % Employee.empCount

    def display_employee(self):
        print "%s has %f LPA salary : " % (self.name, self.salary)


# emp = Employee("Prince", 17.65)
# emp2 = Employee("Prince 2", 17.65)
#
# emp.display_employee()
# emp2.display_employee()
#
# emp.display_count()
#
# print hasattr(emp, "name")
# print hasattr(emp, "empCount")
# print getattr(emp, "empCount")
