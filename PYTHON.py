
# Initialieses the program
from tkinter import * 
root = Tk()
root.title("Ticketing software")
root.geometry("400x150")
staff_id1=""
name1=""
email1=""
issue1=""
#Opens up the stats file for further use in the program
with open("stats.txt","r") as f:
    x=f.readlines()[0]
    y=x.strip("Tickets Submitted: \n")
    z=int(y)+1
with open("stats.txt","r") as f1:
    a=f1.readlines()[1]
    b=a.strip("Tickets Resolved: ")
    c=int(b)
with open("stats.txt","r") as f2:
    s=f2.readlines()[2]
    t=s.strip("Tickets to Solve: ")
    u=int(t)+1

#Exits the Program
def dead():
    root.destroy()

#Main submit ticket button command
def submit():
    label24 = Label(root, text = "Ticket has been submitted").place(x = 0, y = 107)
    label25 = Button(root, text = "Exit", width  = 10, command = dead).place(x = 160, y = 81)
    ticket_status="Open"
    response="Not Yet Provided"

    #Class for writing the ticket
    class Ticket():
        staff_id:"None";
        name:"None";        
        email:"None";
        issue:"None";

    ticket1 = Ticket()
    ticket1.staff_id=label1.get()
    ticket1.name=label3.get()
    ticket1.email=label5.get()
    ticket1.issue=label7.get()

    
    # Password Change Code
    if label7.get()=="Password Change":
        newpassword=str(ticket1.staff_id[0:2])+str(ticket1.name[0:3])
        ticket_status="Closed"
        xy = c+1
        label34 = Label(root, text = newpassword).place(x = 0, y = 130)

        with open("stats.txt","r") as f9:
            editor = f9.readlines()[1]
            editor = str("Tickets Resolved: "+str(xy))
            print(editor)
        with open("stats.txt","w") as file1:
            file1.write("Tickets Submitted: "+str(z)+
                   "\n"+editor+
                   "\nTickets to Solve: "+str(u))
    else:
        with open("stats.txt","w") as file1:
            file1.write("Tickets Submitted: "+str(z)+
                   "\nTickets Resolved: "+str(c)+
                   "\nTickets to Solve: "+str(u))
    
    #Writes ticekt information to file.
    title="ticket {}".format(z)
    with open(title+'.txt','w') as file:
        file.write("Staff ID: "+str(ticket1.staff_id)+
                   "\nName: "+str(ticket1.name)+
                   "\nEmail: "+str(ticket1.email)+
                   "\nIssue: "+str(ticket1.issue)+
                   "\nTicket Status: "+str(ticket_status)+
                   "\nResponse: "+str(response))    

#Main response definition
def response():
    root1=Toplevel(root)
    root1.title("Responses")
    root1.geometry("400x200")
    
    #Code for reading and outputting ticket to screen
    def submit1():
        ticketnumber=label11.get()
        root1.title("Ticket: "+str(ticketnumber))
        with open("ticket "+str(ticketnumber)+".txt","r") as f3:
            i=f3.readlines()[0]
        with open("ticket "+str(ticketnumber)+".txt","r") as f3:
            j=f3.readlines()[1]
        with open("ticket "+str(ticketnumber)+".txt","r") as f3:
            k=f3.readlines()[2]
        with open("ticket "+str(ticketnumber)+".txt","r") as f3:
            l=f3.readlines()[3]
        with open("ticket "+str(ticketnumber)+".txt","r") as f3:
            m=f3.readlines()[4]
        with open("ticket "+str(ticketnumber)+".txt","r") as f3:
            n=f3.readlines()[5]
            label13=Label(root1,text=i)
            label14=Label(root1,text=j)
            label15=Label(root1,text=k)
            label16=Label(root1,text=l)
            label17=Label(root1,text=m)
            label18=Label(root1,text=n)
            label13.place(x=0,y=67)
            label14.place(x=0,y=87)
            label15.place(x=0,y=107)
            label16.place(x=0,y=127)
            label17.place(x=0,y=147)
            label18.place(x=0,y=167)
        
        #Code for responding to a ticket
        def edit():
            with open("ticket "+str(ticketnumber)+".txt","r") as f4:
                editor = f4.readlines()
                editor[4] = str("Ticket Status: Closed\n")
                editor[5] = str("Response: "+label20.get())
            with open("ticket "+str(ticketnumber)+".txt","w") as f4:
                f4.writelines(editor)
                f4.close()
        # Code for reopening a ticket
        def reopen():
            with open("ticket "+str(ticketnumber)+".txt","r") as f5:
                editor = f5.readlines()
                editor[4] = str("Ticket Status: Open\n")
            with open("ticket "+str(ticketnumber)+".txt","w") as f5:
                f5.writelines(editor)
                f5.close()
        #Buttons responding to/ Reopening tickets. 
        label21=Label(root1,text="Respond:").place(x=200, y=0)
        label20=Entry(root1,width=25)
        label20.place(x=200,y=20)
        label19=Button(root1,text="Respond",width=20,command=edit).place(x=200,y=40)
        label23=Label(root1,text="Reopen ticket:").place(x=200,y=70)
        label22=Button(root1,text="Reopen",width = 20,command=reopen).place(x=200,y=90)

    #Buttons for searching for ticket  
    label10 = Label(root1,text="Enter Ticket Number").place(x=0,y=0)
    label11 = Entry(root1,width=20)
    label11.place(x=0,y=20)
    label12 = Button(root1,text="Search",width=20,command=submit1)
    label12.place(x=0,y=40)

#Statistics Page
def statistics():
    root2 = Toplevel(root)
    root.title("Stats")
    label31 = Label(root2, text = x).place(x = 0, y = 0)
    label32 = Label(root2, text = a).place(x = 0, y = 20)
    label33 = Label(root2,text = s).place(x = 0 ,y = 40)

#First page information entry and other buttons. 
label1=Entry(root,width=20,)
label=Label(root,text="Staff ID :").place(x=0, y=0)
label1.place(x=47, y = 1)
label2=Label(root,text="Name   :").place(x=0, y=20)
label3=Entry(root,width=20)
label3.place(x = 47, y = 21)
label4=Label(root,text="Email    :").place(x=0, y=40)
label5=Entry(root,width=20,)
label5.place(x=47, y=41)
label6=Label(root,text="Issue     :").place(x=0, y=60)
label7=Entry(root,width=50, )
label7.place(x=47, y=61)
label8=Button(root,text="Submit ticket",command=submit).place(x=0, y=81)
label9=Button(root,text="Resolve Tickets",command=response).place(x=80, y=81)
label30 = Button(root,text="View Stats", command = statistics).place(x=168, y =81)

root.mainloop()