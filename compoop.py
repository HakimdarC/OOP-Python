
    class employee():
        
        def __int__(sel,name,age,salary):
            self.name = name
            self.age = age
            self.mname = manager.mname
            self.salary = salary

    class manager():
        def __init__(self,mname,sal):
            self.empname = employee.name
            self.age = employee.age
            self.salary = employee.salary

        def manage(self,mname):
            self.mname = mname
            self.sal = 10000
            self.numemp = 6

    def compare(self,other):
        if self.salary < manager.sal:
                print("this is impossible")   
        else:
                print("boss always recieves high pay than his staffs")

    def details(self,a,b):
        self.emp = employee(n,a,sal)
        self.man = manage(n,s)
        compare(emp)
        print("Employees deatils:\n")
        print("name" + emp.name + "age" + emp.age + "Salary" + emp.salary)
        print("Managers deatils:\n")
        print("Managers name" + emp.name + "age" + emp.age + "Salary" + emp.salary)

emp = input ("Enter employees name,age,salary...")
list(emp)
employee(emp[0],emp[1],emp[2])
man = input("Enter managers,sal....")
manager(man[0],man[1])
details()

        
