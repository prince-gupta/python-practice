from employee import Employee

class Manager(Employee):
    managerCount = 0

    def __init__(self, name, salary, location):
        Employee.name = name
        Employee.salary = salary
        self.location = location
        Manager.managerCount += 1
        Manager.empCount += 1
        self.__isPromoted = False

    def display_employee(self):
        print "%s has %f LPA salary at location %s : " % (self.name, self.salary, self.location)

    def is_promoted(self):
        return self.__isPromoted

emp = Manager("Prince", 27, "Gurgaon")
emp.display_employee()
emp.display_count()
print emp.is_promoted()
print emp.__isPromoted