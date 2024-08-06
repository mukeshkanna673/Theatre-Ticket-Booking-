def seats():
    print("enter the number of seats:")
    j=int(input())
    print("prize:",j,"x","130","=",j*130)  
    print("\t\t\tBill\n \t\tName:",n,"\n\t\tNumber:",m)
    print("\t\tMovie:",d,"\n\t\tTickets:",j,"\n","\t\tTotal amount:",j*130)
    print("Are you sure That your booking the Tickets of worth Rs.",130,"yes/no")
    
    l=str(input())
    if l.lower()=="yes":
        print("payment mode (Cash/Online) ")
        p=str(input())
        if p.lower()=="cash":
            print("Please pay the cash\n Collect the bill \n Thank you for coming ")
        elif p=="online":
            upi=input("Enter UPI id: ")
            pay=int(input("Pay: " ))
            amount=j*130
            if(pay==amount):
                print("Your ticket is succesfully Booked")
            else:
                print("Sorry ! Transfer failed")
            print("Thank you for coming")
            
    elif l.lower()=="no":
        print("Thank you for coming please aproach us next time")

def full():
    print("Do you want to continue:yes/no")
    s=str(input())
    if s.lower()=="yes":
        print("Enter the option of the show timing:\n 1.11:00 AM  2.2:30 PM  3.6:30 PM   4.10:30 PM")
        i=int(input())
        if i==1:
            seats()
        elif i==2:
            seats()
        elif i==3:
            seats()
        elif i==4:
            seats()
        else:
            pass
    elif s.lower()=="no":
        h=str(input("Do you want to  [a].quit or [b].continue\n"))
        if h.lower()=="b":
            start()
        elif h.lower()=="a":
            pass
def start():
    global n,m,d
    y="=-=-=-=-=-=-=-=--=-"
    print(y.center(100))
    x="Welcome to GRAND Cinemas"
    print(x.center(100))
    print(y.center(100))
    n=str(input("Enter your Name:"))
    m=int(input("Enter your Phone Number:"))
    print("Movies".center(100))
    print("\n1.Raayan\n2.Deadpool&Wolverine\n3.Indian2\n4.Maharaja")
    d=str(input("Enter the Movie name: "))
    if d.lower()=="raayan":
        print("Raayan")
        import webbrowser as w
        w.open_new_tab("https://youtu.be/qQJJWhh-XRo?si=jhCmtlg8fFqHdoSl")
        full()
    elif d.lower()=="deadpool&Wolverine":
        print("Deadpool&Wolverine")
        import webbrowser as w
        w.open_new_tab("https://youtu.be/FvH1kuRCQrM?si=V6k_t2vPK5LbFvK_")
        full()
    elif d.lower()=="indian2":
        print("Indian2")
        import webbrowser as w
        w.open_new_tab("https://youtu.be/3bvBUT5pQYY?si=EAx2mIn-C5iMY3Us")
        full()
    elif d.lower()=="maharaja":
        print("Maharaja")
        import webbrowser as w
        w.open_new_tab("https://youtu.be/keE9JWBWJ7A?si=RBBguXU8vN5696g6")
        full()
start()  
