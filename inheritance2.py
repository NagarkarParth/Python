class employee :
    def accept(self):
        self.empid=int(input("Enter Employee ID -"))
        self.ename=input("Enter Employee Name - ")
        self.salary=int(input("Enter Salary -"))

    def display(self):
        print("EMPLOYEE ID -",self.empid)
        print("EMPLOYEE NAME -",self.ename)
        print("EMPLOYEE SALARY -",self.salary)

class Manager(employee):
    def getdata(self):
        self.accept()
        self.bonus=int(input("Enter Bonus Ammount -"))

    def putdata(self):
        self.display()
        print("BONUS AMOUNT - ",self.bonus)

class developer(employee):

    def inpdata(self):
        self.accept()
        self.noofhhr=int(input("Enter Number Of Hr -"))

    def outdata(self):
        self.display()
        print("NO OF HR -",self.noofhhr)

print("\n--- Manager Details ---")
m = Manager()
m.getdata()
m.putdata()
print("\n--- Developer Details ---")
d = developer()
d.inpdata()
d.outdata()
