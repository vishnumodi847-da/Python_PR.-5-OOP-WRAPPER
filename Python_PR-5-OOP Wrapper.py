# PROJECT : EMPLOYEE MANAGEMENT SYSTEM (OOP WRAPPER)


class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    def get_data(self):
        return self.__employee_id, self.__salary

    def set_data(self, employee_id, salary):
        self.__employee_id = employee_id
        self.__salary = salary

    def display(self):
        print("ID : ", self.__employee_id)
        print("NAME : ", self.name)
        print("AGE : ", self.age)
        print("SALARY : ", self.__salary)


class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print("DEPARTMENT : ",self.department)


class Devloper(Employee):
    def __init__(self, employee_id, name, age, salary, programming_lung):
        super().__init__(employee_id, name, age, salary)
        self.programming_lung = programming_lung

    def display(self):
        super().display()
        print("PROGRAME : ",self.programming_lung)

print("================================================================")


print("Manager is subclass of Employee = ",issubclass(Manager,Employee))


print("================================================================")



while True:
    print("================================================================")
    print("                     1. EMPLOYEE DATA")
    print("                     2. MANAGER DATA")
    print("                     3. DEVLOPER DATA")
    print("                     4. EXIT")
    print("================================================================")
    choice=int(input("ENTER YOUR CHOICE : "))

    if choice==1:
        e=Employee(101,"VISHNU",21,"15LAC")
        e.display()
    elif choice==2:
        n=Manager(102,"VIJAY",22,"14LAC","HR")
        n.display()
    elif choice==3:
        v=Devloper(103,"RAHUL",22,"16LAC","PYTHON")
        v.display()
    elif choice==4:
        print("EXIT")
        break
    else:
        print("INVAILD CAPTURE")
