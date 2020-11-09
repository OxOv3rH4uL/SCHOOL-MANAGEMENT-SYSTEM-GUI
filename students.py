from tkinter import *
from random import choice
from tkinter import Toplevel, ttk, messagebox , filedialog
from tkinter.ttk import Treeview
import mysql.connector as mysql
import PIL
from PIL import ImageTk, Image
from pandas import *

def studentsDB():
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
                return
            try:
                mycursor.execute('create database studentmanagement')
                mycursor.execute('use studentmanagement')
                mycursor.execute('create table students(Admn_No int(8) not null primary key,Name varchar(30),Phone_No varchar(15),DOB varchar(10), Blood_Group varchar(10),Mother_Name varchar(20),Father_Name varchar(20))')
                
                messagebox.showinfo('Success!', 'Created and Connected to the Database Successfully!', parent=codb)
            except:
                mycursor.execute('use studentmanagement')
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
        headLabel = Label(root, text=head, bg="#000000", fg="#eec94c", font=(
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
            bg = bgvalue.get()
            mother = mothervalue.get()
            father = fathervalue.get()
            try:
                ss = 'insert into students values(%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(ss, (idd, name, phone, dob, bg, mother, father, ))
                con.commit()
                ans = messagebox.askyesnocancel(
                    'Success!', 'Data Added Successfully!! , Do you want to clear the form?', parent=adddb)
                if (ans == True):
                    idvalue.set('')
                    namevalue.set('')
                    phonevalue.set('')
                    dobvalue.set('')
                    bgvalue.set('')
                    mothervalue.set('')
                    fathervalue.set('')
            except:
                messagebox.showerror(
                    'Error!', 'Admn No already exists , Please try again', parent=adddb)
            mycursor.execute('select * from students')
            contents = mycursor.fetchall()
            contenttable.delete(*contenttable.get_children())

            for i in contents:
                values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                contenttable.insert('', END, values=values)

        adddb = Toplevel(master=dataEntryFrame)
        adddb.title("Add Student's Data")
        adddb.config(bg='yellow')
        adddb.grab_set()
        adddb.resizable(False, False)
        adddb.geometry("470x470+220+200")
        ####DATA STUFFS####

        ### ID DETAILS ###
        idvalue = StringVar()
        idLabel = Label(adddb, text="Enter Admn No: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        idLabel.place(x=10, y=10)
        idEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=idvalue)
        idEntry.place(x=230, y=10)

        ### NAME DETAILS ###
        namevalue = StringVar()
        nameLabel = Label(adddb, text="Enter Name: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        nameLabel.place(x=10, y=70)
        nameEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=namevalue)
        nameEntry.place(x=230, y=70)

        ### PHONE NEUMBER DETAILS ###
        phonevalue = StringVar()
        phoneLabel = Label(adddb, text="Enter Phone No: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        phoneLabel.place(x=10, y=130)
        phoneEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=phonevalue)
        phoneEntry.place(x=230, y=130)

        ### DATE OF BIRTH DETAILS ###
        dobvalue = StringVar()
        dobLabel = Label(adddb, text="Enter DOB: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        dobLabel.place(x=10, y=190)
        dobEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=dobvalue)
        dobEntry.place(x=230, y=190)

        ### BLOOD GROUP DETAILS ###
        bgvalue = StringVar()
        bgLabel = Label(adddb, text="Enter Blood Group: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        bgLabel.place(x=10, y=250)
        bgEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=bgvalue)
        bgEntry.place(x=230, y=250)

        ### MOTHER NAME DETAILS ###
        mothervalue = StringVar()
        motherLabel = Label(adddb, text="Enter Mother Name: ", font=(
            'Helvetica', 15, 'italic bold'), bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        motherLabel.place(x=10, y=310)
        motherEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=mothervalue)
        motherEntry.place(x=230, y=310)

        ### FATHER NAME DETIALS ###
        fathervalue = StringVar()
        fatherLabel = Label(adddb, text="Enter Father Name: ", font=(
            'Helvetica', 15, 'italic bold'), bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        fatherLabel.place(x=10, y=370)
        fatherEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=fathervalue)
        fatherEntry.place(x=230, y=370)

        ### SUBMIT ###
        subButton = Button(adddb, text="Submit", font=('Helvetica', 15, 'italic bold'), bg='dark violet', relief=RIDGE,
                        width=8, borderwidth=5, bd=4, activebackground='red', activeforeground='white', command=addDB)
        subButton.place(x=180, y=410)
        adddb.mainloop()


    def showData():
        try:
            command = 'select * from students'
            mycursor.execute(command)
            contents = mycursor.fetchall()
            contenttable.delete(*contenttable.get_children())

            for i in contents:
                values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                contenttable.insert('', END, values=values)
        except:
            messagebox.showinfo('Error!','Please Connect to the Database!')

    def searchData():
        def searchsql():
            idd = sidvalue.get()
            name = snamevalue.get()
            phone = sphonevalue.get()
            dob = sdobvalue.get()
            bg = sbgvalue.get()
            mother = smothervalue.get()
            father = sfathervalue.get()
            
            if (idd != ''):
                command = 'select * from students where Admn_No = %s'
                mycursor.execute(command, (idd, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)
            
            elif (name != ''):
                command = 'select * from students where Name = %s'
                mycursor.execute(command, (name, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (phone != ''):
                command = 'select * from students where Phone_No = %s'
                mycursor.execute(command, (phone, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (dob != ''):
                command = 'select * from students where DOB = %s'
                mycursor.execute(command, (dob, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (bg != ''):
                command = 'select * from students where Blood_Group = %s'
                mycursor.execute(command, (bg, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (mother != ''):
                command = 'select * from students where Mother_Name = %s'
                mycursor.execute(command, (mother, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (father != ''):
                command = 'select * from students where Father_Name = %s'
                mycursor.execute(command, (father, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

        searchdb = Toplevel(master=dataEntryFrame)
        searchdb.title("Search Student's Data")
        searchdb.config(bg='maroon2')
        searchdb.grab_set()
        searchdb.resizable(False, False)
        searchdb.geometry("470x470+220+200")
        ####DATA STUFFS####

        ### ID DETAILS ###
        sidvalue = StringVar()
        sidLabel = Label(searchdb, text="Search Admn No:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sidLabel.place(x=10, y=10)
        sidEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sidvalue)
        sidEntry.place(x=230, y=10)

        ### NAME DETAILS ###
        snamevalue = StringVar()
        snameLabel = Label(searchdb, text="Search Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        snameLabel.place(x=10, y=70)
        snameEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=snamevalue)
        snameEntry.place(x=230, y=70)

        ### PHONE NEUMBER DETAILS ###
        sphonevalue = StringVar()
        sphoneLabel = Label(searchdb, text="Search Phone No:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sphoneLabel.place(x=10, y=130)
        sphoneEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sphonevalue)
        sphoneEntry.place(x=230, y=130)

        ### DATE OF BIRTH DETAILS ###
        sdobvalue = StringVar()
        sdobLabel = Label(searchdb, text="Search DOB:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sdobLabel.place(x=10, y=190)
        sdobEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sdobvalue)
        sdobEntry.place(x=230, y=190)

        ### BLOOD GROUP DETAILS ###
        sbgvalue = StringVar()
        sbgLabel = Label(searchdb, text="Search Blood Group:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sbgLabel.place(x=10, y=250)
        sbgEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sbgvalue)
        sbgEntry.place(x=230, y=250)

        ### MOTHER NAME DETAILS ###
        smothervalue = StringVar()
        smotherLabel = Label(searchdb, text="Search Mother Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        smotherLabel.place(x=10, y=310)
        smotherEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=smothervalue)
        smotherEntry.place(x=230, y=310)

        ### FATHER NAME DETIALS ###
        sfathervalue = StringVar()
        sfatherLabel = Label(searchdb, text="Search Father Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sfatherLabel.place(x=10, y=370)
        sfatherEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sfathervalue)
        sfatherEntry.place(x=230, y=370)

        ### SUBMIT ###
        ssubButton = Button(searchdb, text="Search", font=('Helvetica', 15, 'italic bold'), bg='blue2', relief=RIDGE,
                            width=8, borderwidth=5, bd=4, activebackground='red', activeforeground='white', command=searchsql)
        ssubButton.place(x=180, y=410)
        searchdb.mainloop()
        pass


    def updateData():

        def update():
            idd = uidvalue.get()
            name = unamevalue.get()
            phone = uphonevalue.get()
            dob = udobvalue.get()
            bg = ubgvalue.get()
            mother = umothervalue.get()
            father = ufathervalue.get()
            try: 
                command = 'update students set Name=%s,Phone_No=%s,DOB=%s,Blood_Group=%s,Mother_Name=%s,Father_Name=%s where Admn_No=%s'
                mycursor.execute(command,(name,phone,dob,bg,mother,father,idd, ))
                con.commit()
                messagebox.showinfo('Success!','Updated Successfully!')
                command = 'select * from students'
                mycursor.execute(command)
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)
            
                updatedb.destroy()
            
            except:
                messagebox.showinfo('Error!','Please Connect to the Database!')
        
        updatedb = Toplevel(master=dataEntryFrame)
        updatedb.title("Update Student's Data")
        updatedb.config(bg='gold2')
        updatedb.grab_set()
        updatedb.resizable(False, False)
        updatedb.geometry("470x470+220+200")

        ### ID DETAILS ###

        uidvalue = StringVar()
        uidLabel = Label(updatedb, text="Update Admn No:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        uidLabel.place(x=10, y=10)
        uidEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=uidvalue)
        uidEntry.place(x=230, y=10)

        ### NAME DETAILS ###
        unamevalue = StringVar()
        unameLabel = Label(updatedb, text="Update Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        unameLabel.place(x=10, y=70)
        unameEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=unamevalue)
        unameEntry.place(x=230, y=70)

        ### PHONE NEUMBER DETAILS ###
        uphonevalue = StringVar()
        uphoneLabel = Label(updatedb, text="Update Phone No:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        uphoneLabel.place(x=10, y=130)
        uphoneEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=uphonevalue)
        uphoneEntry.place(x=230, y=130)

        ### DATE OF BIRTH DETAILS ###
        udobvalue = StringVar()
        udobLabel = Label(updatedb, text="Update DOB:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        udobLabel.place(x=10, y=190)
        udobEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=udobvalue)
        udobEntry.place(x=230, y=190)

        ### BLOOD GROUP DETAILS ###
        ubgvalue = StringVar()
        ubgLabel = Label(updatedb, text="Update Blood Group:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        ubgLabel.place(x=10, y=250)
        ubgEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=ubgvalue)
        ubgEntry.place(x=230, y=250)

        ### MOTHER NAME DETAILS ###
        umothervalue = StringVar()
        umotherLabel = Label(updatedb, text="Update Mother Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        umotherLabel.place(x=10, y=310)
        umotherEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=umothervalue)
        umotherEntry.place(x=230, y=310)

        ### FATHER NAME DETIALS ###
        ufathervalue = StringVar()
        ufatherLabel = Label(updatedb, text="Update Father Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        ufatherLabel.place(x=10, y=370)
        ufatherEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=ufathervalue)
        ufatherEntry.place(x=230, y=370)

        ### SUBMIT ###
        usubButton = Button(updatedb, text="Update", font=('Helvetica', 15, 'italic bold'), bg='cyan',
                            relief=RIDGE, width=8, borderwidth=5, bd=4, activebackground='red', activeforeground='white',command=update)
        usubButton.place(x=180, y=410)
        a = contenttable.focus()
        data = contenttable.item(a)
        b = data['values']
        if len(b) != 0:
            uidvalue.set(b[0])
            unamevalue.set(b[1])
            uphonevalue.set(b[2])
            udobvalue.set(b[3])
            ubgvalue.set(b[4])
            umothervalue.set(b[5])
            ufathervalue.set(b[6])

        updatedb.mainloop()

        pass


    def deleteData():
        try:
            a = contenttable.focus()
            data = contenttable.item(a)
            b = data['values'][0]
            command = 'delete from students where Admn_No=%s'
            mycursor.execute(command,(b, ))
            con.commit()
            command = 'select * from students'
            mycursor.execute(command)
            contents = mycursor.fetchall()
            contenttable.delete(*contenttable.get_children())

            for i in contents:
                values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                contenttable.insert('', END, values=values)
        
            messagebox.showinfo('Success!','Deleted Successfully!')
        except:
            messagebox.showerror('Error!','No element selected!')

    def export():
        a = filedialog.asksaveasfilename()
        b = contenttable.get_children()
        id,name,phone,dob,bg,mother,father= [],[],[],[],[],[],[]
        for i in b:
            contents = contenttable.item(i)
            c = contents['values']
            id.append(c[0]),name.append(c[1]),phone.append(c[2]),dob.append(c[3]),bg.append(c[4]),mother.append(c[5]),father.append(c[6])
        cols = ['Admn No','Name','Phone No','DOB','Blood Group','Mother Name','Father Name']
        fin = DataFrame(list(zip(id,name,phone,dob,bg,mother,father)),columns=cols)
        path = a+'.csv'
        fin.to_csv(path,index=False)
        messagebox.showinfo('Success!','Student Data Saved Successfully! {} '.format(path))

        

    root = Toplevel()
    root.grab_set_global()
    root.title("STUDENT MANAGEMENT SYSTEM")
    root.geometry('1174x700+150+2')
    root.config(bg ="#7395AE")
    root.resizable(False,False)

    ### HEADING FRAME ###
    headingFrame = Frame(root, bg = "Black", relief = RIDGE,)
    headingFrame.place(x=0, y=0, width=1174, height=110)

    head = "ZESCA"
    headLabel1 = Label(headingFrame, text=head, bg="Black", fg="#FFFFFF", font=(
                    'Elianto', 40))
    headLabel1.place(x=26, y=20)                

    dataEntryFrame = Frame(root , bg = 'lime' , relief = RIDGE, )
    dataEntryFrame.place(x=0,y=110,width=330,height=620)



    #welcomeLabel = Label(dataEntryFrame, text="#_#_#_#_#_COMMANDS_#_#_#_#_#",
    #                     fg='white', bg='black', width=30, font=('Helvetica', 20, 'italic bold'))
    #welcomeLabel.pack(side=TOP, expand=True)
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
    exportButton = Button(dataEntryFrame, text="Export", font=('Hero', 20), bg='white', relief=FLAT,
                        width=13, command=export)
    exportButton.pack(side=TOP, expand=True)


    ####SHOW CONTENT STUFF####
    showFrame = Frame(root, bg='black', relief=FLAT, borderwidth=3)
    showFrame.place(x=330, y=110, width=845, height=590)
    xScrollBar = Scrollbar(showFrame, orient=HORIZONTAL)
    yScrollBar = Scrollbar(showFrame, orient=VERTICAL)
    contenttable = Treeview(showFrame, columns=('Admn No', 'Name', 'Phone No', 'D.O.B', 'Blood Group',
                                                'Mother Name', 'Father Name'), yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

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
    contenttable.heading('Blood Group', text='Blood Group')
    contenttable.heading('Mother Name', text='Mother Name')
    contenttable.heading('Father Name', text='Father Name')
    ### SIZE STUFFS ###
    contenttable.column('Admn No', width=150)
    contenttable.column('Name', width=250)
    contenttable.column('Phone No', width=200)
    contenttable.column('D.O.B', width=150)
    contenttable.column('Blood Group', width=170)
    contenttable.column('Mother Name', width=250)
    contenttable.column('Father Name', width=250)

    contenttable['show'] = 'headings'
    contenttable.pack(fill=BOTH, expand=1)


    ####HEADING STUFFS####
    txt = "WELCOME TO STUDENT MANAGEMENT SYSTEM"
    
    headLabel = Label(root, text=txt, font=('Elianto', 20, 'italic bold'),
                    bg="Black", relief=FLAT, width=45,foreground='yellow')
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



