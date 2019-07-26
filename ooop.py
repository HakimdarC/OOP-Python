class employee():
    def __int__(self):
        self.name = "Mhhjj"
        self.age = 3333
        self.mname = "Moses"
        self.salary = 33333
        
    def emp(self,name,mname,salary):
        self.name = name
        self.mname = manage.mname
        self.salary = salary

class manager():
    def __init__(self):
        self.age = 22

    def manage(self,mname,sal,nemp):
        self.mname = mname
        self.sal = sal
        self.numemp = numemp

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

emp = input ("Enter name,man name,salary...")
e = list(emp.split())
emp(e[0],e[1],e[2])
man = input("Enter name,salary,nemp...")
m = list(man.split())
manage(m[0],m[1],m[1])
details()
