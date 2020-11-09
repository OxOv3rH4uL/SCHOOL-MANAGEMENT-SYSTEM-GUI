from tkinter import *
from random import choice
from tkinter import Toplevel, ttk, messagebox , filedialog
from tkinter.ttk import Treeview
import mysql.connector as mysql
import PIL
from PIL import ImageTk, Image
from pandas import *


def libraryDB():
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
                mycursor.execute('create database librarymanagement')
                mycursor.execute('use librarymanagement')
                mycursor.execute('create table library(student_id int(8) not null primary key,student_name varchar(30),book_name varchar(30),book_id varchar(10), author_name varchar(30),borrow_date varchar(20),return_date varchar(20))')
                messagebox.showinfo('Success!', 'Created and Connected to the Database Successfully!', parent=codb)
            except:
                mycursor.execute('use librarymanagement')
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
            studentid = idvalue.get()
            studentname = namevalue.get()
            bookname = bnvalue.get()
            bookid = bidvalue.get()
            authorname = authvalue.get()
            borrowdate = bdvalue.get()
            returndate = rdvalue.get()
            try:
                ss = 'insert into library values(%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(ss, (studentid, studentname, bookname, bookid, authorname, borrowdate, returndate))
                con.commit()
                ans = messagebox.askyesnocancel('Success!', 'Data Added Successfully!! , Do you want to clear the form?', parent=adddb)
                if (ans == True):
                    idvalue.set('')
                    namevalue.set('')
                    bnvalue.set('')
                    bidvalue.set('')
                    authvalue.set('')
                    bdvalue.set('')
                    rdvalue.set('')
            except:
                messagebox.showerror('Error!', 'Admn No already exists , Please try again', parent=adddb)
            mycursor.execute('select * from library')
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

        ### Admn No DETAILS ###
        idvalue = StringVar()
        idLabel = Label(adddb, text="Enter Admn No: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        idLabel.place(x=10, y=10)
        idEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=idvalue)
        idEntry.place(x=230, y=10)

        ### Name DETAILS ###
        namevalue = StringVar()
        nameLabel = Label(adddb, text="Enter Name: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        nameLabel.place(x=10, y=70)
        nameEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=namevalue)
        nameEntry.place(x=230, y=70)

        ### Book Name DETAILS ###
        bnvalue = StringVar()
        bnLabel = Label(adddb, text="Enter Book Name: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        bnLabel.place(x=10, y=130)
        bnEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=bnvalue)
        bnEntry.place(x=230, y=130)

        ### Book ID DETAILS ###
        bidvalue = StringVar()
        bidLabel = Label(adddb, text="Enter Book ID: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        bidLabel.place(x=10, y=190)
        bidEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=bidvalue)
        bidEntry.place(x=230, y=190)

        ### Author Name DETAILS ###
        authvalue = StringVar()
        authLabel = Label(adddb, text="Enter Author Name: ", font=('Helvetica', 15, 'italic bold'),
                        bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        authLabel.place(x=10, y=250)
        authEntry = Entry(adddb, font=('Helvetica', 15, 'italic bold'),
                        bd=5, textvariable=authvalue)
        authEntry.place(x=230, y=250)

        ### Borrow Date DETAILS ###
        bdvalue = StringVar()
        bdLabel = Label(adddb, text="Enter Borrow Date: ", font=(
            'Helvetica', 15, 'italic bold'), bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        bdLabel.place(x=10, y=310)
        bdEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=bdvalue)
        bdEntry.place(x=230, y=310)

        ### Return Date DETIALS ###
        rdvalue = StringVar()
        rdLabel = Label(adddb, text="Enter Return Date: ", font=(
            'Helvetica', 15, 'italic bold'), bg='dark violet', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        rdLabel.place(x=10, y=370)
        rdEntry = Entry(adddb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=rdvalue)
        rdEntry.place(x=230, y=370)

        ### SUBMIT ###
        subButton = Button(adddb, text="Submit", font=('Helvetica', 15, 'italic bold'), bg='dark violet', relief=RIDGE,
                        width=8, borderwidth=5, bd=4, activebackground='red', activeforeground='white', command=addDB)
        subButton.place(x=180, y=410)
        adddb.mainloop()


    def showData():
        try:
            command = 'select * from library'
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
            studentid = sidvalue.get()
            studentname = snamevalue.get()
            bookname = sbnvalue.get()
            bookid = sbidvalue.get()
            authorname = sauthvalue.get()
            borrowdate = sbdvalue.get()
            returndate = srnvalue.get()
            
            if (studentid != ''):
                command = 'select * from library where student_id = %s'
                mycursor.execute(command, (studentid, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)
            
            elif (studentname != ''):
                command = 'select * from library where student_name = %s'
                mycursor.execute(command, (studentname, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (bookname != ''):
                command = 'select * from library where book_name = %s'
                mycursor.execute(command, (bookname, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (bookid != ''):
                command = 'select * from library where book_id = %s'
                mycursor.execute(command, (bookid, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (authorname != ''):
                command = 'select * from library where author_name = %s'
                mycursor.execute(command, (authorname, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (borrowdate != ''):
                command = 'select * from library where borrow_date = %s'
                mycursor.execute(command, (borrowdate, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

            elif (returndate != ''):
                command = 'select * from library where return_date = %s'
                mycursor.execute(command, (returndate, ))
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)

        searchdb = Toplevel(master=dataEntryFrame)
        searchdb.title("Search Book's Data")
        searchdb.config(bg='maroon2')
        searchdb.grab_set()
        searchdb.resizable(False, False)
        searchdb.geometry("470x470+220+200")
        ####DATA STUFFS####

        ### Admn No DETAILS ###
        sidvalue = StringVar()
        sidLabel = Label(searchdb, text="Search Admn No:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sidLabel.place(x=10, y=10)
        sidEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sidvalue)
        sidEntry.place(x=230, y=10)

        ### Name DETAILS ###
        snamevalue = StringVar()
        snameLabel = Label(searchdb, text="Search Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        snameLabel.place(x=10, y=70)
        snameEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=snamevalue)
        snameEntry.place(x=230, y=70)

        ### Book Name DETAILS ###
        sbnvalue = StringVar()
        sbnLabel = Label(searchdb, text="Search Book Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sbnLabel.place(x=10, y=130)
        sbnEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sbnvalue)
        sbnEntry.place(x=230, y=130)

        ### Book ID DETAILS ###
        sbidvalue = StringVar()
        sbidLabel = Label(searchdb, text="Search Book ID:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sbidLabel.place(x=10, y=190)
        sbidEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sbidvalue)
        sbidEntry.place(x=230, y=190)

        ### Author Name DETAILS ###
        sauthvalue = StringVar()
        sauthLabel = Label(searchdb, text="Search Author Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sauthLabel.place(x=10, y=250)
        sauthEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sauthvalue)
        sauthEntry.place(x=230, y=250)

        ### Borrow Date DETAILS ###
        sbdvalue = StringVar()
        sbdLabel = Label(searchdb, text="Search Borrow Date:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        sbdLabel.place(x=10, y=310)
        sbdEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=sbdvalue)
        sbdEntry.place(x=230, y=310)

        ### Return Date DETIALS ###
        srnvalue = StringVar()
        srnLabel = Label(searchdb, text="Search Return Date:", font=(
            'Helvetica', 15, 'italic bold'), bg='blue2', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        srnLabel.place(x=10, y=370)
        srnEntry = Entry(searchdb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=srnvalue)
        srnEntry.place(x=230, y=370)

        ### SUBMIT ###
        ssubButton = Button(searchdb, text="Search", font=('Helvetica', 15, 'italic bold'), bg='blue2', relief=RIDGE,
                            width=8, borderwidth=5, bd=4, activebackground='red', activeforeground='white', command=searchsql)
        ssubButton.place(x=180, y=410)
        searchdb.mainloop()
        pass


    def updateData():

        def update():
            studentid = uidvalue.get()
            studentname = unamevalue.get()
            bookname = ubnvalue.get()
            bookid = ubidvalue.get()
            authorname = uauthvalue.get()
            borrowdate = ubdvalue.get()
            returndate = urdvalue.get()
            try: 
                command = 'update library set student_name=%s,book_name=%s,book_id=%s,author_name=%s,borrow_date=%s,return_date=%s where student_id=%s'
                mycursor.execute(command,(studentname,bookname,bookid,authorname,borrowdate,returndate,studentid, ))
                con.commit()
                messagebox.showinfo('Success!','Updated Successfully!')
                updatedb.destroy()

                command = 'select * from library'
                mycursor.execute(command)
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    contenttable.insert('', END, values=values)
            
            
            except:
                messagebox.showinfo('Error!','Please Connect to the Database!')
        
        updatedb = Toplevel(master=dataEntryFrame)
        updatedb.title("Update Library's Data")
        updatedb.config(bg='gold2')
        updatedb.grab_set()
        updatedb.resizable(False, False)
        updatedb.geometry("470x470+220+200")

        ### Admn No DETAILS ###

        uidvalue = StringVar()
        uidLabel = Label(updatedb, text="Update Admn No:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        uidLabel.place(x=10, y=10)
        uidEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=uidvalue)
        uidEntry.place(x=230, y=10)

        ### Name DETAILS ###
        unamevalue = StringVar()
        unameLabel = Label(updatedb, text="Update Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        unameLabel.place(x=10, y=70)
        unameEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=unamevalue)
        unameEntry.place(x=230, y=70)

        ### PHONE NEUMBER DETAILS ###
        ubnvalue = StringVar()
        ubnLabel = Label(updatedb, text="Update Book Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        ubnLabel.place(x=10, y=130)
        ubnEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=ubnvalue)
        ubnEntry.place(x=230, y=130)

        ### DATE OF BIRTH DETAILS ###
        ubidvalue = StringVar()
        ubidLabel = Label(updatedb, text="Update Book ID:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        ubidLabel.place(x=10, y=190)
        ubidEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=ubidvalue)
        ubidEntry.place(x=230, y=190)

        ### BLOOD GROUP DETAILS ###
        uauthvalue = StringVar()
        uauthLabel = Label(updatedb, text="Update Author Name:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        uauthLabel.place(x=10, y=250)
        uauthEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=uauthvalue)
        uauthEntry.place(x=230, y=250)

        ### MOTHER NAME DETAILS ###
        ubdvalue = StringVar()
        ubdLabel = Label(updatedb, text="Update Borrow Date:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        ubdLabel.place(x=10, y=310)
        ubdEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=ubdvalue)
        ubdEntry.place(x=230, y=310)

        ### FATHER NAME DETIALS ###
        urdvalue = StringVar()
        urdLabel = Label(updatedb, text="Update Return Date:", font=(
            'Helvetica', 15, 'italic bold'), bg='cyan', relief=GROOVE, width=17, borderwidth=4, anchor='n')
        urdLabel.place(x=10, y=370)
        urdEntry = Entry(updatedb, font=(
            'Helvetica', 15, 'italic bold'), bd=5, textvariable=urdvalue)
        urdEntry.place(x=230, y=370)

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
            ubnvalue.set(b[2])
            ubidvalue.set(b[3])
            uauthvalue.set(b[4])
            ubdvalue.set(b[5])
            urdvalue.set(b[6])

        updatedb.mainloop()

        pass


    def deleteData():
        
        a = contenttable.focus()
        data = contenttable.item(a)
        b = data['values'][0]
        command = 'delete from library where student_id=%s'
        mycursor.execute(command,(b, ))
        con.commit()
        command = 'select * from library'
        mycursor.execute(command)
        contents = mycursor.fetchall()
        contenttable.delete(*contenttable.get_children())

        for i in contents:
            values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
            contenttable.insert('', END, values=values)
        
        messagebox.showinfo('Success!','Deleted Successfully!')

    def export():
            a = filedialog.asksaveasfilename()
            b = contenttable.get_children()
            id,name,bid,bname,authrname,bordat,retdat= [],[],[],[],[],[],[]
            for i in b:
                contents = contenttable.item(i)
                c = contents['values']
                id.append(c[0]),name.append(c[1]),bid.append(c[2]),bname.append(c[3]),authrname.append(c[4]),bordat.append(c[5]),retdat.append(c[6])
            cols = ['Admn No','Name','Book ID','Book Name','Author Name','Borrow Date','Return Date']
            fin = DataFrame(list(zip(id,name,bid,bname,authrname,bordat,retdat)),columns=cols)
            path = a+'.csv'
            fin.to_csv(path,index=False)
            messagebox.showinfo('Success!','Student Data Saved Successfully! {} '.format(path))
        
            


    root = Toplevel()
    root.title("LIBRARY MANAGEMENT SYSTEM")
    root.geometry('1174x700+150+2')
    root.config(bg ="#7395AE")
    root.resizable(False,False)

    ### HEADING FRAME ###
    headingFrame = Frame(root, bg = "Black", relief = RIDGE,)
    headingFrame.place(x=0, y=0, width=1174, height=110)

    head = "ZESCA"
    headLabel = Label(headingFrame, text=head, fg="#FFFFFF", font=(
                    'Elianto', 40),bg='Black')
    headLabel.place(x=26, y=20)                

    dataEntryFrame = Frame(root , bg = 'Cyan' , relief = RIDGE, )
    dataEntryFrame.place(x=0,y=110,width=330,height=620)

    
    
    addDataButton =  Button(dataEntryFrame, text="Add Book", font=('Hero', 20), bg='white', relief=FLAT,
                        width=13, command = addData)
    addDataButton.pack(side=TOP, expand=True)
    showallButton = Button(dataEntryFrame, text="Show All", font=('Hero', 20), bg='white', relief=FLAT,
                        width=13, command=showData)
    showallButton.pack(side=TOP, expand=True)
    searchDataButton = Button(dataEntryFrame, text="Search Book", font=('Hero', 20), bg='white',
                            relief=FLAT, width=13, command=searchData)
    searchDataButton.pack(side=TOP, expand=True)
    updateDataButton = Button(dataEntryFrame, text="Update Book", font=('Hero', 20), bg='white',
                            relief=FLAT, width=13, command=updateData)
    updateDataButton.pack(side=TOP, expand=True)
    deleteDataButton = Button(dataEntryFrame, text="Delete Book", font=('Hero', 20), bg='white',
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
    contenttable = Treeview(showFrame, columns=('Admn No', 'Name', 'Book Name', 'Book ID', 'Author Name',
                                                'Borrow Date', 'Return Date'), yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

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
    contenttable.heading('Book Name', text='Book Name')
    contenttable.heading('Book ID', text='Book ID')
    contenttable.heading('Author Name', text='Author Name')
    contenttable.heading('Borrow Date', text='Borrow Date')
    contenttable.heading('Return Date', text='Return Date')
    ### SIZE STUFFS ###
    contenttable.column('Admn No', width=150)
    contenttable.column('Name', width=250)
    contenttable.column('Book Name', width=200)
    contenttable.column('Book ID', width=150)
    contenttable.column('Author Name', width=170)
    contenttable.column('Borrow Date', width=250)
    contenttable.column('Return Date', width=250)

    contenttable['show'] = 'headings'
    contenttable.pack(fill=BOTH, expand=2)


    ####HEADING STUFFS####
    txt = "WELCOME TO LIBRARY MANAGEMENT SYSTEM"
    
    headLabel = Label(root, text=txt, font=('Elianto', 20, 'italic bold'),
                    bg="Black", relief=FLAT, width=45,foreground='black')
    headLabel.place(x=240, y=40)
    colors = [ 'snow', 'peach puff', 'yellow', 'ivory','black','green','pink','purple','blue','lime','orange']


    def headColor():
        fg = choice(colors)
        headLabel.config(fg=fg)
        headLabel.after(25, headColor)
    # headSlider()
    headColor()
    ####CONNECT BUTTON####
    connectButton = Button(root, text="Connect to DB", font=('Hero', 15), bg='cyan', relief=FLAT,
                        width=15 ,command=connectDB)
    connectButton.place(x=980, y=0)
    ####TEAM MEMBERS LIST####
    ##                    relief=RIDGE, width=15, borderwidth=5, bd=4, activebackground='red', activeforeground='white')
    #teamButton.place(x=0, y=0)
    root.mainloop()



