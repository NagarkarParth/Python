class a :
    def hello(self):
        print("Hello A")

class b(a): 
    def welcome(self):
        print("Welcome B")

b1=b()
b1.hello()
b1.welcome()