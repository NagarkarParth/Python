from Account1 import Account


def create():
    a1 = Account(101, "Rahul", 5000)

    # Accessing properties
    return a1


def display(a1):
    # Displaying properties
    print(a1.accno)
    print(a1.cname)
    print(a1.accbal)