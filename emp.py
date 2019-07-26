class Employee():
        
    def __init__(self,name,mname,salary):
        self.name = name
        self.mname = mname
        self.salary = salary
        
emp=Employee("John","Moses",34566)
print("Employees deatils:\n")
print("name:{}, manager name:{}, sal:{}".format(emp.name,emp.mname,emp.salary))
