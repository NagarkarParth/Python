#Write a Program That Simulates An atm menu using a while TRUE loop with break and continue , supporting balance enquiry ,deposit,withdrawal,and exit and locking the account after 3 wrong pin attemnts

pin ="1234"
balance = 1000
att = 0 

while att < 3 :
    p = input ("Enter Pin - ")
    if p == pin :
        break
 
    else:
            att += 1
            print("Wrong PIN!")
    
            if att == 3:
                print("Account Locked!!!")

if att < 3:
        while True:
            print("\n1. Balance Enquiry")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Exit")

            ch = input ("Enter Choice -")
            if ch == "1" :
                print("Balance - ",balance)
                continue

            elif ch == "2":
                amount = float (input("Enter Amount To Deposit - "))
                balance += amount
                print("Amount Deposited Sucessfully !")
                continue

            elif ch == "3":
                amount = float(input("Enter withdrawal amount: "))
                if amount > balance:
                        print("Insufficient Fund")
                else :
                    balance -= amount
                print("Withdrawal successful")

            elif ch=="4" :
                print("ThankYou For Using ATM")
                break

            else :
                print("Invalid Choice!!!")
                continue
    