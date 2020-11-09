from tkinter import *
from random import choice
from tkinter import Toplevel, ttk, messagebox , filedialog
from tkinter.ttk import Treeview
import mysql.connector as mysql
import PIL
from PIL import ImageTk, Image
from pandas import *

def feesDB():



    def connectDB():
        def connmysql():
            global mycursor
            global con
            host = hostvalue.get()
            user = uservalue.get()
            password = passvalue.get()
            try:
                con = mysql.connect(host=host, user=user, passwd=password)
                mycursor = con.cursor()

            except:
                messagebox.showerror('Error!', 'Please Try Again')
            try:
                mycursor.execute('create database feesmanagement')
                mycursor.execute('use feesmanagement')
                mycursor.execute('create table fees(Admn_No int(8) not null primary key,Name varchar(30),Phone_No varchar(15),DOB varchar(10), Amount_Paid varchar(10),Date_Payment varchar(20))')
                messagebox.showinfo('Success!', 'Created and Connected to the Database Successfully!', parent=codb)
            except:
                mycursor.execute('use feesmanagement')
               
                messagebox.showinfo('Success!', 'Connected to the Database Successfully!', parent=codb)    
            codb.destroy()

        codb = Toplevel(master=root)
        codb.title("Enter Credentials")
        codb.grab_set()
        codb.resizable(False, False)
        codb.geometry("450x450+800+230")
        codb.config(bg="black")
        ####MYSQL HOST STUFFS####
        
        head = "ZESCA"
        headLabel = Label(codb, text=head, bg="#000000", fg="#eec94c", font=(
            'Elianto', 40, ), )
        headLabel.place(x=26, y=20)
    
        hostvalue = StringVar()
        hostLabel = Label(codb, text="Enter Host: ", font=('Hero', 15 ),
                        fg='#EEC94C',bg='#000000', relief=FLAT, width=15, anchor='n')
        hostLabel.place(x=10, y=130)
        hostEntry = Entry(codb, font=('Hero', 15), textvariable=hostvalue)
        hostEntry.place(x=200, y=130)

        ####MYSQL USER STUFFS##
        uservalue = StringVar()
        userLabel = Label(codb, text="Enter User: ", font=('Hero', 15),
                        fg='#EEC94C',bg='#000000', relief=FLAT, width=15, anchor='n')
        userLabel.place(x=10, y=190)
        userEntry = Entry(codb, font=('Hero', 15), textvariable=uservalue)
        userEntry.place(x=200, y=190)

        ####MYSQL PASSWORD####
        passvalue = StringVar()
        passLabel = Label(codb, text="Enter Password: ", font=(
            'Hero', 15), fg='#EEC94C',bg='#000000', relief=FLAT, width=15,anchor='n')
        passLabel.place(x=10, y=260)
        passEntry = Entry(codb, font=('Hero', 15),
                            textvariable=passvalue,show = '*')
        passEntry.place(x=200, y=260)

        ####SUBMIT BUTTOM####
        submitButton = Button(codb, text="Connect", font=('Hero', 15), bg='#EEC94C', relief=FLAT,
                            width=8, activebackground='red', activeforeground='white', command=connmysql)
        submitButton.place(x=160, y=320)
                


    def addData():
        def addDB():
            idd = idvalue.get()
            name = namevalue.get()
            phone = phonevalue.get()
            dob = dobvalue.get()
            paidamt = paidamtvalue.get()
            amtdate = amtdatevalue.get()
            try:
                ss = 'insert into fees values(%s,%s,%s,%s,%s,%s)'
                mycursor.execute(ss, (idd, name, phone, dob, paidamt, amtdate))
                con.commit()
                ans = messagebox.askyesnocancel('Success!', 'Data Added Successfully!! , Do you want to clear the form?', parent=adddb)
                if (ans == True):
                    idvalue.set('')
                    namevalue.set('')
                    phonevalue.set('')
                    dobvalue.set('')
                    paidamtvalue.set('')
                    amtdatevalue.set('')
            except:
                messagebox.showerror('Error!', 'Admn No already exists , Please try again', parent=adddb)
            sel = 'select * from fees'
            mycursor.execute(sel)
            contents = mycursor.fetchall()
            contenttable.delete(*contenttable.get_children())

            for i in contents:
                values = [i[0], i[1], i[2], i[3], i[4], i[5]]
                contenttable.insert('', END, values=values)

        adddb = Toplevel(master=dataEntryFrame)
        adddb.title("Add Student's Fees Data")
        adddb.config(bg='black')
        adddb.grab_set()
        adddb.resizable(False, False)
        adddb.geometry("540x480+100+100")
        ####DATA STUFFS####

        ### ID DETAILS ###
        idvalue = StringVar()
        idLabel = Label(adddb, text="Enter Admn No: ", font=('Helvetica', 15, 'italic bold'),
                        bg='white', relief=GROOVE, width=20, borderwidth=2, anchor='n')
        idLabel.place(x=10, y=10)
        idEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=idvalue)
        idEntry.place(x=280, y=10)

        ### NAME DETAILS ###
        namevalue = StringVar()
        nameLabel = Label(adddb, text="Enter Name: ", font=('Helvetica', 15, 'italic bold'),
                        bg='white', relief=GROOVE, width=20, borderwidth=2, anchor='n')
        nameLabel.place(x=10, y=70)
        nameEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=namevalue)
        nameEntry.place(x=280, y=70)

        ### PHONE NEUMBER DETAILS ###
        phonevalue = StringVar()
        phoneLabel = Label(adddb, text="Enter Phone No: ", font=('Helvetica', 15, 'italic bold'),
                        bg='white', relief=GROOVE, width=20, borderwidth=2, anchor='n')
        phoneLabel.place(x=10, y=130)
        phoneEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=phonevalue)
        phoneEntry.place(x=280, y=130)

        ### DATE OF BIRTH DETAILS ###
        dobvalue = StringVar()
        dobLabel = Label(adddb, text="Enter DOB: ", font=('Helvetica', 15, 'italic bold'),
                        bg='white', relief=GROOVE, width=20, borderwidth=2, anchor='n')
        dobLabel.place(x=10, y=190)
        dobEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=dobvalue)
        dobEntry.place(x=280, y=190)

        ### BLOOD GROUP DETAILS ###
        paidamtvalue = StringVar()
        paidLabel = Label(adddb, text="Enter Amount Paid: ", font=('Helvetica', 15, 'italic bold'),
                        bg='white', relief=GROOVE, width=20, borderwidth=2, anchor='n')
        paidLabel.place(x=10, y=250)
        paidEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=paidamtvalue)
        paidEntry.place(x=280, y=250)

        ### Payment Date DETAILS ###
        amtdatevalue = StringVar()
        amtdateLabel = Label(adddb, text="Enter Payment Date: ", font=(
            'Helvetica', 15, 'italic bold'), bg='white', relief=GROOVE, width=20, borderwidth=2, anchor='n')
        amtdateLabel.place(x=10, y=310)
        amtdateEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=amtdatevalue)
        amtdateEntry.place(x=280, y=310)

        ### SUBMIT ###
        subButton = Button(adddb, text="Submit", font=('Helvetica', 15, 'italic bold'), bg='white', relief=RIDGE,
                        width=8, borderwidth=5, bd=4, activebackground='red', activeforeground='white', command=addDB)
        subButton.place(x=220, y=380)
        adddb.mainloop()


    def showData():
        try:
            command = 'select * from fees'
            mycursor.execute(command)
            contents = mycursor.fetchall()
            contenttable.delete(*contenttable.get_children())

            for i in contents:
                values = [i[0], i[1], i[2], i[3], i[4], i[5]]
                contenttable.insert('', END, values=values)
        except:
            messagebox.showinfo('Error!','Please Connect to the Database!')

    def searchData():
        def searchsql():
            idd = sidvalue.get()
            name = snamevalue.get()
            phone = sphonevalue.get()
            dob = sdobvalue.get()
            paidamt = spaidamtvalue.get()
            amtdate = samtdatevalue.get()
            
            if (idd != ''):
                command = 'select * from fees where Admn_No = %s'
                mycursor.execute(command,(idd, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    contenttable.insert('', END, values=values)
            
            elif (name != ''):
                command = 'select * from fees where Name = %s'
                mycursor.execute(command, (name, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    contenttable.insert('', END, values=values)

            elif (phone != ''):
                command = 'select * from fees where Phone_No = %s'
                mycursor.execute(command, (phone, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    contenttable.insert('', END, values=values)

            elif (dob != ''):
                command = 'select * from fees where DOB = %s'
                mycursor.execute(command, (dob, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    contenttable.insert('', END, values=values)

            elif (paidamt != ''):
                command = 'select * from fees where Amount_Paid = %s'
                mycursor.execute(command, (paidamt, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    contenttable.insert('', END, values=values)

            elif (amtdate != ''):
                command = 'select * from fees where Date_Payment = %s'
                mycursor.execute(command, (amtdate, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    contenttable.insert('', END, values=values)



        searchdb = Toplevel(master=dataEntryFrame)
        searchdb.title("Search Student's Fees Data")
        searchdb.config(bg='blue')
        searchdb.grab_set()
        searchdb.resizable(False, False)
        searchdb.geometry("540x480+100+100")
        ####DATA STUFFS####

        ### ID DETAILS ###
        sidvalue = StringVar()
        sidLabel = Label(searchdb, text="Search Admn No:", font=(
            'Helvetica', 15, 'italic bold'), bg='grey', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        sidLabel.place(x=10, y=10)
        sidEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sidvalue)
        sidEntry.place(x=280, y=10)

        ### NAME DETAILS ###
        snamevalue = StringVar()
        snameLabel = Label(searchdb, text="Search Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='grey', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        snameLabel.place(x=10, y=70)
        snameEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=snamevalue)
        snameEntry.place(x=280, y=70)

        ### PHONE NEUMBER DETAILS ###
        sphonevalue = StringVar()
        sphoneLabel = Label(searchdb, text="Search Phone No:", font=(
            'Helvetica', 15, 'italic bold'), bg='grey', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        sphoneLabel.place(x=10, y=130)
        sphoneEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sphonevalue)
        sphoneEntry.place(x=280, y=130)

        ### DATE OF BIRTH DETAILS ###
        sdobvalue = StringVar()
        sdobLabel = Label(searchdb, text="Search DOB:", font=(
            'Helvetica', 15, 'italic bold'), bg='grey', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        sdobLabel.place(x=10, y=190)
        sdobEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sdobvalue)
        sdobEntry.place(x=280, y=190)

        ### BLOOD GROUP DETAILS ###
        spaidamtvalue = StringVar()
        spaidamtLabel = Label(searchdb, text="Search by Amount Paid:", font=(
            'Helvetica', 15, 'italic bold'), bg='grey', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        spaidamtLabel.place(x=10, y=250)
        spaidamtEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=spaidamtvalue)
        spaidamtEntry.place(x=280, y=250)

        ### Payment Date DETAILS ###
        samtdatevalue = StringVar()
        samtdateLabel = Label(searchdb, text="Search Payment Date:", font=(
            'Helvetica', 15, 'italic bold'), bg='grey', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        samtdateLabel.place(x=10, y=310)
        samtdateEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=samtdatevalue)
        samtdateEntry.place(x=280, y=310)

        

        ### SUBMIT ###
        ssubButton = Button(searchdb, text="Search", font=('Helvetica', 15, 'italic bold'), bg='grey', relief=RIDGE,
                            width=8, borderwidth=5, bd=4, activebackground='red', activeforeground='white', command=searchsql)
        ssubButton.place(x=220, y=380)
        searchdb.mainloop()
        pass


    def updateData():

        def update():
            idd = uidvalue.get()
            name = unamevalue.get()
            phone = uphonevalue.get()
            dob = udobvalue.get()
            paidamt = upaidamtvalue.get()
            amtdate = uamtdatevalue.get()
            try: 
                command = 'update fees set Name=%s,Phone_No=%s,DOB=%s,Amount_Paid=%s,Date_Payment=%s where Admn_No=%s'
                mycursor.execute(command,(name,phone,dob,paidamt,amtdate,idd, ))
                con.commit()
                messagebox.showinfo('Success!','Updated Successfully!')
                command = 'select * from fees'
                mycursor.execute(command)
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2
                                            ], i[3], i[4], i[5]]
                    contenttable.insert('', END, values=values)
            
                updatedb.destroy()
            
            except:
                messagebox.showinfo('Error!','Please Connect to the Database!')
        
        updatedb = Toplevel(master=dataEntryFrame)
        updatedb.title("Update Student's Fees Data")
        updatedb.config(bg='gold2')
        updatedb.grab_set()
        updatedb.resizable(False, False)
        updatedb.geometry("540x480+100+100")

        ### ID DETAILS ###

        uidvalue = StringVar()
        uidLabel = Label(updatedb, text="Update Admn No:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        uidLabel.place(x=10, y=10)
        uidEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=uidvalue)
        uidEntry.place(x=280, y=10)

        ### NAME DETAILS ###
        unamevalue = StringVar()
        unameLabel = Label(updatedb, text="Update Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        unameLabel.place(x=10, y=70)
        unameEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=unamevalue)
        unameEntry.place(x=280, y=70)

        ### PHONE NEUMBER DETAILS ###
        uphonevalue = StringVar()
        uphoneLabel = Label(updatedb, text="Update Phone No:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        uphoneLabel.place(x=10, y=130)
        uphoneEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=uphonevalue)
        uphoneEntry.place(x=280, y=130)

        ### DATE OF BIRTH DETAILS ###
        udobvalue = StringVar()
        udobLabel = Label(updatedb, text="Update DOB:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        udobLabel.place(x=10, y=190)
        udobEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=udobvalue)
        udobEntry.place(x=280, y=190)

        ### BLOOD GROUP DETAILS ###
        upaidamtvalue = StringVar()
        upaidamtLabel = Label(updatedb, text="Update Amount Paid:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        upaidamtLabel.place(x=10, y=250)
        upaidamtEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=upaidamtvalue)
        upaidamtEntry.place(x=280, y=250)

        ### Payment Date DETAILS ###
        uamtdatevalue = StringVar()
        uamtdateLabel = Label(updatedb, text="Update Payment Date:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=20, borderwidth=4, anchor='n')
        uamtdateLabel.place(x=10, y=310)
        uamtdateEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=uamtdatevalue)
        uamtdateEntry.place(x=280, y=310)

        
        ### SUBMIT ###
        usubButton = Button(updatedb, text="Update", font=('Helvetica', 15, 'italic bold'), bg='cyan',
                            relief=RIDGE, width=8, borderwidth=5, bd=4, activebackground='red', activeforeground='white',command=update)
        usubButton.place(x=220, y=380)
        a = contenttable.focus()
        data = contenttable.item(a)
        b = data['values']
        if len(b) != 0:
            uidvalue.set(b[0])
            unamevalue.set(b[1])
            uphonevalue.set(b[2])
            udobvalue.set(b[3])
            upaidamtvalue.set(b[4])
            uamtdatevalue.set(b[5])

        updatedb.mainloop()

        pass


    def deleteData():
        
        a = contenttable.focus()
        data = contenttable.item(a)
        b = data['values'][0]
        command = 'delete from fees where Admn_No=%s'
        mycursor.execute(command,(b, ))
        con.commit()
        command = 'select * from fees'
        mycursor.execute(command)
        contents = mycursor.fetchall()
        contenttable.delete(*contenttable.get_children())

        for i in contents:
            values = [i[0], i[1], i[2], i[3], i[4], i[5]]
            contenttable.insert('', END, values=values)
        
        messagebox.showinfo('Success!','Deleted Successfully!')

            

    def export():
        a = filedialog.asksaveasfilename()
        b = contenttable.get_children()
        id,name,phone,dob,amountpaid,paymentdate,= [],[],[],[],[],[]
        for i in b:
            contents = contenttable.item(i)
            c = contents['values']
            id.append(c[0]),name.append(c[1]),phone.append(c[2]),dob.append(c[3]),amountpaid.append(c[4]),paymentdate.append(c[5])
        cols = ['Admn No','Name','Phone No','DOB','AMOUNT PAID','DateOfPayment']
        fin = DataFrame(list(zip(id,name,phone,dob,amountpaid,paymentdate)),columns=cols)
        path = a+'.csv'
        fin.to_csv(path,index=False)
        messagebox.showinfo('Success!','Student Data Saved Successfully! {} '.format(path))
    root = Toplevel()
    root.grab_set()
    root.title("FEES MANAGEMENT SYSTEM")
    root.geometry('1174x700+150+2')
    root.config(bg ="#7395AE")
    root.resizable(False,False)

    ### HEADING FRAME ###
    headingFrame = Frame(root, bg = "Black", relief = RIDGE,)
    headingFrame.place(x=0, y=0, width=1174, height=110)

    head = "ZESCA"
    headLabel = Label(headingFrame, text=head, bg="Black", fg="#FFFFFF", font=(
                    'Elianto', 40))
    headLabel.place(x=26, y=20)                

    dataEntryFrame = Frame(root , bg = 'Red' , relief = RIDGE, )
    dataEntryFrame.place(x=0,y=110,width=330,height=620)

    

    
    addDataButton =  Button(dataEntryFrame, text="Add Student", font=('Hero', 20), bg='white', relief=FLAT,
                        width=13, command = addData)
    addDataButton.pack(side=TOP, expand=True)
    showallButton = Button(dataEntryFrame, text="Show All", font=('Hero', 20), bg='white', relief=FLAT,
                        width=13, command=showData)
    showallButton.pack(side=TOP, expand=True)
    searchDataButton = Button(dataEntryFrame, text="Search Student", font=('Hero', 20), bg='white',
                            relief=FLAT, width=13, command=searchData)
    searchDataButton.pack(side=TOP, expand=True)
    updateDataButton = Button(dataEntryFrame, text="Update Student", font=('Hero', 20), bg='white',
                            relief=FLAT, width=13, command=updateData)
    updateDataButton.pack(side=TOP, expand=True)
    deleteDataButton = Button(dataEntryFrame, text="Delete Student", font=('Hero', 20), bg='white',
                            relief=FLAT, width=13, command=deleteData)
    deleteDataButton.pack(side=TOP, expand=True)
    exitButton = Button(dataEntryFrame, text="Export", font=('Hero', 20), bg='white', relief=FLAT,
                        width=13, command=export)
    exitButton.pack(side=TOP, expand=True)


    ####SHOW CONTENT STUFF####
    showFrame = Frame(root, bg='black', relief=FLAT, borderwidth=3)
    showFrame.place(x=330, y=110, width=845, height=590)
    xScrollBar = Scrollbar(showFrame, orient=HORIZONTAL)
    yScrollBar = Scrollbar(showFrame, orient=VERTICAL)
    contenttable = Treeview(showFrame, columns=('Admn No', 'Name', 'Phone No', 'D.O.B', 'Amount Paid',
                                                'Payment Date'), yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

    ### STYLING STUFFS ###
    style = ttk.Style()
    style.configure('Treeview.Heading',font=('times',15,'bold'),foreground='black')
    style.configure('Treeview',font=('times',15,'bold'),background='black',foreground='cyan',rowheight=30)

    xScrollBar.pack(side=BOTTOM, fill=X)
    yScrollBar.pack(side=RIGHT, fill=Y)
    xScrollBar.config(command=contenttable.xview)
    yScrollBar.config(command=contenttable.yview)
    contenttable.heading('Admn No', text='Admn No')
    contenttable.heading('Name', text='Name')
    contenttable.heading('Phone No', text='Phone No')
    contenttable.heading('D.O.B', text='D.O.B')
    contenttable.heading('Amount Paid', text='Amount Paid')
    contenttable.heading('Payment Date', text='Payment Date')
    ### SIZE STUFFS ###
    contenttable.column('Admn No', width=150)
    contenttable.column('Name', width=250)
    contenttable.column('Phone No', width=200)
    contenttable.column('D.O.B', width=150)
    contenttable.column('Amount Paid', width=170)
    contenttable.column('Payment Date', width=250)

    contenttable['show'] = 'headings'
    contenttable.pack(fill=BOTH, expand=1)


    ####HEADING STUFFS####
    txt = "WELCOME TO FEES MANAGEMENT SYSTEM"
    count = 0
    text = ''
    headLabel = Label(root, text=txt, font=('Elianto', 20, 'italic bold'),
                    bg="Black", relief=FLAT, width=45,foreground='white')
    headLabel.place(x=240, y=40)
    colors = ['blue', 'red', 'cyan', 'snow', 'peach puff', 'yellow', 'ivory','black','green','pink','purple']


    def headColor():
        fg = choice(colors)
        headLabel.config(fg=fg)
        headLabel.after(25, headColor)
    headColor()
    ####CONNECT BUTTON####
    connectButton = Button(root, text="Connect to DB", font=('Hero', 15), bg='cyan', relief=FLAT,
                        width=15 ,command=connectDB)
    connectButton.place(x=980, y=0)
    
    root.mainloop()


