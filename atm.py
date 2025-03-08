from datetime import datetime
actual_pin=None
exit=True
inserted=False
balance=1000
transactions=[]
while True:
    print("Welcome to SBI")
    if not inserted:
        a=int(input("enter atm card\n1-for yes\n2-for no"))
        if a==1:
            if not actual_pin:
                actual_pin = input("please set the pin")
            pin = input("enter the pin")
            if pin == actual_pin:
                print(''' 
                      1.deposit
                      2.withdrawl
                      3.mini statement
                      4.pin change
                      5.exit
                      ''')
                option=int(input("choose any one of the option above"))
                if option==1:
                    amount=int(input("feed the amount"))
                    if amount%100==0:
                        print("cash has been accepted")
                        balance += amount
                        transactions.append(amount)
                    else:
                        print("feed only multiples of 100")
                elif option==2:
                    amount=int(input("enter the amount"))
                    if amount%100==0:
                        if amount<balance:
                            print("cash has been withdrawn")
                            balance -= amount
                            transactions.append(-amount)
                        else:
                            print("insufficient balance")
                    else:
                        print("enter only multiples of 100")
                elif option==3:
                    dt=datetime.now()
                    date=dt.strftime("%d-%m-%Y")
                    time=dt.strftime("%I:%M %p")
                    print(f'''
                                 State Bank Of India 
                          Date : {date}            Time :{time}
                            Transactions 
                            ''')
                    for transaction in transactions:
                        print(transaction)
                    print("balance=",balance)
                elif option==4:
                    old_pin=input("enter the old pin")
                    if old_pin!=actual_pin:
                        print("invalid pin")
                    else:
                        new_pin=int(input("enter the new pin"))
                        print("new pin entered succesfully")
                elif option==5:
                    print("do you want to exit")
                    exit=input("1:for yes 2:for no")
                    if exit==1:
                        print("exit")
                    
