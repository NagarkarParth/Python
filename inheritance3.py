class Account:

    def accept(self):
        self.accno = int(input("Enter account number: "))
        self.cname = input("Enter customer name: ")
        self.accbal = float(input("Enter account balance: "))

    def display(self):
        print("Account Number:", self.accno)
        print("Customer Name:", self.cname)
        print("Balance:", self.accbal)


class Savingaccount(Account):

    def inputdata(self):
        self.accept()
        self.interestrate = float(input("Enter interest rate: "))

    def displaydata(self):
        self.display()
        print("Interest Rate:", self.interestrate)


class Currentaccount(Account):

    def getdata(self):
        self.accept()
        self.companyname = input("Enter company name: ")

    def putdata(self):
        self.display()
        print("Company Name:", self.companyname)


s1 = Savingaccount()
s1.inputdata()
s1.displaydata()

c1 = Currentaccount()
c1.getdata()
c1.putdata()