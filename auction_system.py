import random
import time
name = ""
print("\t\t\t*ONLINE AUCTION SYSTEM*\t\t\t")
i=int(input("enter the value 1 or 2 \n1:new user \n2:exsisting user\n"))
file = open('gobi.txt','w') 
def create():
    name=str(input("Enter your name\n"))
    file.write(name)
    file.write("\n")
    contact()
    auction()
def contact():
        conno=str(input("Enter your contact number\n"))
        mobno=len(conno)
        if int((mobno)==10):
            print("OTP SENT TO YOUR MOBILE NUMBER")
            contents = "1234567890"
            pw_length =1
            out= ""
            for i in range(pw_length):
                next_index = random.randrange(len(contents))
                out = out +contents[next_index]
                print(out)
                print("ENTER YOUR OTP")
                a=str(input(""))
                if a == out:
                    file.write(conno)
                    file.write("\n")
                    add=str(input("Enter your address\n"))
                    file.write(add)
                    file.write("\n")
                    file.close()
                else:
                    print("Password is wrong ,if you want re-enter press 1")
                    i=int(input(""))
                    if i==1:
                        contact()
                    else:
                        create()
                    
        else:
            contact()

def exsistinguser():
    name=str(input("Enter your name\n"))
    contacts()
def contacts():
    conno=str(input("Enter your contact number\n"))
    mobno=len(conno)
    if int((mobno)==10):
        print("OTP SENT TO YOUR MOBILE NUMBER")
        contents = "1234567890"
        pw_length =1
        out= ""
        for i in range(pw_length):
            next_index = random.randrange(len(contents))
            out = out +contents[next_index]
            print(out)
            print("ENTER YOUR OTP")
            a=str(input(""))
            if a == out:
                auction()
            else:
                print("Password is wrong ,if you want re-enter press 1")
                i=int(input(""))
                if i==1:
                    contacts()
            
    else:
        contacts()
def amount():
    print("Online payment only")
    print("Enter your credit card number")
    cn=str(input(""))
    cvv=str(input("enter CVV number\n"))
    lencn=len(cn)
    lencvv=len(cvv)
    if lencn==16 and lencvv==3:
        print("PAYMENT SUCCESSFUL!\n")
        print("**********************\n")
        print("The house details are\n")
        print("**********************\n")
    else:
        amount()
def amountcar():
    print("online payment only")
    print("Enter your credit card number")
    cn=str(input(""))
    cvv=str(input("Enter CVV number\n"))
    lencn=len(cn)
    lencvv=len(cvv)
    if lencn==16 and lencvv==3:
        print("PAYMENT SUCCESSFUL!\n")
        print("**********************\n")
        print("The car details are")
        print("**********************\n")
    else:
        amount()
    
def auction():
    print("\t\t\t*WELCOME TO AUCTION*\t\t\t")
    print("Auction products are \n1: Car \n2: House ")
    print("*****************Week Schedule For Auction*************")
    print(" _________________________________________________________________")
    print("|        |                 |       Time           |               |")
    print("| Date   |   Car Name      |----------------------|   Starting    |")
    print("|        |                 |Starting   |   Ending |     Rate      |")
    print("|-----------------------------------------------------------------|")
    print("| 14-dec |     Swift       | 10:00:00  | 10:30:00 |    3lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 15-dec |     I10         | 10:30:00  | 11:00:00 |    2lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 16-dec |     City        | 11:00:00  | 11:30:00 |    5lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 17-dec |     Polo        | 11:30:00  | 12:00:00 |    3lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 18-dec |     WagonR      | 12:00:00  | 12:30:00 |    2.5lakhs   |")
    print("|-----------------------------------------------------------------|")
    print("| 19-dec |     Brezza      | 12:30:00  | 1:00:00  |    3lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 20-dec |     Scorpio     | 12:30:00  | 1:00:00  |    5lakhs     |")
    print("|_________________________________________________________________|")
    print(" _______________________________________________________________")
    print("|        |                 |       Time           |             |")
    print("|  Date  |   House area    |----------------------|   Starting  |")
    print("|        |                 |Starting   |   Ending |     Rate    |")
    print("|---------------------------------------------------------------|")
    print("| 14-dec |   Gandhipuram   |  1:00:00  |  1:30:00 |   23lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 15-dec |   Kuniyamuthur  |  1:30:00  |  2:00:00 |   12lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 16-dec |     Ukkadam     |  2:00:00  |  2:30:00 |   25lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 17-dec |     Hopes       |  2:30:00  |  3:00:00 |   23lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 18-dec |    Singanallur  |  3:00:00  |  3:30:00 |   2lakhs    |")
    print("|---------------------------------------------------------------|")
    print("| 19-dec |  Saravanampatti |  3:30:00  |  4:00:00 |   13lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 20-dec |  Ramanathapuram |  3:30:00  |  4:00:00 |   13lakhs   |")
    print("|_______________________________________________________________|")

    print("House auction from 10:00:00  to 10:30:00")
    print("Car auction from 12:00:00 to 12:30:00")
    i=time.strftime("%I:%M:%S")
    print(i)
    i='01:10:00'
    #i='01:25:20'
    # print(i)
    if i<'01:30:00'and i>'01:00:00':
        print("House at auction")
        print("MAX Bid amount is 2,30,00,000 INR \nIf you want to buy this house Press 1")
        hr=int(input(""))
        if hr==1:
            g=int(input("Enter your Bidding Amount "))
           #for i in range(g,23000000,225000):
            #    print(i)
            print("The winner is final amount=",g)
            amount()
        else:
            auction()
    elif i<'10:30:00'and i>'10:00:00':
        print("Car at auction")
        print("MAX Bid amount is 1,00,00,000 INR \n")
        hr=int(input(""))
        if hr==1:
            g=int(input("Enter your Bidding Amount "))
            #for i in range(g,10000000,225700):
             #   print(i)
            print("The winner is final amount=",g)
            amountcar()
        else:
            auction()
        
    else:
        print("Sorry! Better luck next time.")
     
if i==1:
    print("new user\n")
    create()
elif i==2:
    print("Exsisting user\n")
    exsistinguser()
else:
    print("Enter valid number 1 or 2\n")

