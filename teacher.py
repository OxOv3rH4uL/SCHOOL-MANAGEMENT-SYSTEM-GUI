from tkinter import *
from random import choice
from tkinter import Toplevel, ttk, messagebox
from tkinter.ttk import Treeview
import mysql.connector as mysql
import PIL
from PIL import ImageTk, Image
import platform
from tkinter.filedialog import asksaveasfilename
from pandas import *

def teacherDB():
    
        
    
        
        # try:
        #     if con.is_connected():
        # #         print('Connected to MySQL database')

        # except:
        #     messagebox.showerror('No Connection','Please Connect to MySQL for further use')
        #     ConnectSQL()
    
   
    
    # mycursor.execute("create database if not exists teacher")
    # mycursor.execute("use teacher")
    # mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='teacher' AND table_name = 'Teacher'")
    # C = mycursor.fetchall()

    # if C == []:
    #     mycursor.execute("create table Teacher(Teacher_Code varchar(40), Teacher_Name varchar(40), Subject varchar(40), Phone_Number int, DOJ varchar(40), DOB varchar(40), Email varchar(30), Salary int)")
    #     mycursor.execute('alter table teacher modify column Teacher_Code int not null primary key')
        
    # else:
    #     mycursor.execute('use teacher')    
        
    def ThirdWindow():
        
        def ConnectSQL():
            
            global codb
            global con
            
            def connmysql():
                global mycursor
                global con
                
                
                host1 = hostEntry.get()
                user1 = userEntry.get()
                password1 = passEntry.get()
                # print(host1)
                # print(user1)
                # print(password1)
                
            
                
                con = mysql.connect(host=host1, user=user1, passwd=password1)
                mycursor = con.cursor()
                mycursor.execute("create database if not exists teacher")
                mycursor.execute("use teacher")
                mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='teacher' AND table_name = 'Teacher'")
                C = mycursor.fetchall()

                if C == []:
                    mycursor.execute("create table Teacher(Teacher_Code varchar(40), Teacher_Name varchar(40), Subject varchar(40), Phone_Number int, DOJ varchar(40), DOB varchar(40), Email varchar(30), Salary int)")
                    mycursor.execute('alter table teacher modify column Teacher_Code int not null primary key')
                    
                else:
                    mycursor.execute('use teacher')
            
            
                
                #messagebox.showerror('Error!', 'Please Try Again')
                
                codb.destroy()
                
                TreeviewCode()
                

            codb = Toplevel(master=root8)
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
                
            
            codb.mainloop()
                    
        def InsertTable(UsedTab): 

            def InsertAllData(DataInsert):
                
                DataInsert2 = []
                for i in DataInsert:
                    Item = i.get()
                    DataInsert2.append(Item)

                # print(DataInsert2)
                DataQuery = ""
                query1 = "desc %s" % (UsedTab)
                mycursor.execute(query1)
                GetData = mycursor.fetchall()
                DataTypes = []
                
                
                for q in GetData:
                    try:
                        B = q[1].decode('utf-8')
                        DataTypes.append(B)
                    except:
                        B = q[1]
                        DataTypes.append(B)
                    
                DataTypes2 = []
                
                for l in DataTypes:
                    try:
                        C = l.index("(")
                        DataTypes2.append(l[0:C])
                    except ValueError:
                        DataTypes2.append(l)

                # print(DataTypes2)
                N = len(DataTypes)

                Empty = 0
                for i in DataInsert2:
                    if i == '':
                        Empty = 1
                        messagebox.showerror(
                            'Please Enter all Fields', 'Enter all the Input Fields')
                        break

                if Empty != 1:
                    for k in range(N):

                        if DataTypes2[k] == "int":
                            try:
                                int(DataInsert2[k])
                                if k == N-1:
                                    DataQuery = DataQuery + DataInsert2[k]
                                else:
                                    DataQuery = DataQuery + DataInsert2[k] + ","
                            except ValueError:
                                messagebox.showerror('Invalid Field Input',
                                                        'Please enter the corresponding data type',parent=root)
                                continue

                        elif DataTypes2[k] == "float":
                            try:
                                float(DataInsert2[k])
                                if k == N-1:
                                    DataQuery = DataQuery + DataInsert2[k]
                                else:
                                    DataQuery = DataQuery + DataInsert2[k] + ","
                            except ValueError:
                                messagebox.showerror('Invalid Field Input',
                                                        'Please enter the corresponding data type')
                                continue
                        else:
                            if k == N-1:
                                DataQuery = DataQuery + "'" + DataInsert2[k] + "'"
                            else:
                                DataQuery = DataQuery + "'" + \
                                    DataInsert2[k] + "'" + ","
                            continue

                    query = "insert into %s values(%s)" % (UsedTab, DataQuery)
                    # print(query)
                    mycursor.execute(query)
                    con.commit()
                    # print(mycursor.rowcount, "record inserted.")
                    
                    TreeviewCode()
                    root.destroy()
                    
            DataInsert = []
            root = Tk()
            root.config(bg='#000000')
            root.geometry('600x500+200+200')
            # root.resizable(False,False)
            root.title("Insert All Values")

            head = "ENTER DETAILS"
            headLabel = Label(root, text=head, bg="#000000", font=(
                'Hero', 30, ), fg="#eec94c")
            headLabel.place(x=15, y=10,)

            query = "show COLUMNS from %s" % (UsedTab)
            mycursor.execute(query)
            Columns = mycursor.fetchall()
            Col = []
            for i in Columns:
                Col.append(i[0])
            x_coordinate = 290
            y_coordinate = 70
            x_coordinate_2 = 20
            y_coordinate_2 = 70
            for i in range(len(Col)):

                InsertDataLabelText = "Enter %s" % (Col[i])
                InsertDataNameLabel = Label(
                    root, text=InsertDataLabelText, bg="#000000",fg='#eec94c', font=('Hero', 16))
                InsertDataNameLabel.place(x=x_coordinate_2, y=y_coordinate_2)
                InsertDataName = StringVar()
                InsertDataNameEntry = Entry(
                    root, width=28, font=20, textvariable=InsertDataName)
                InsertDataNameEntry.place(x=x_coordinate, y=y_coordinate)
                DataInsert.append(InsertDataNameEntry)
                x_coordinate = x_coordinate
                y_coordinate = y_coordinate + 40
                x_coordinate_2 = x_coordinate_2
                y_coordinate_2 = y_coordinate_2 + 40

            AddDataButton = Button(root, text="Add", fg="#000000",bg='#eec94c',width=8, font=('Hero', 10), command=lambda:InsertAllData(DataInsert))
            AddDataButton.place(x=390, y=20)
            
            
            root.mainloop()
        
        def UpdateData(UsedTab):
            
            def UpdateInfo(NO):
                        
                global No, Y
                No = int(NO.get())

                ParaLabel3.destroy() 
                FieldNoEntry3.destroy()
                NoButton3.destroy()
                
                #ParaLabel = Label(root1, text="Select the Field ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                #ParaLabel.place(x=20, y=60) 

                x_coordinate = 30
                y_coordinate = 70
                x_coordinate2 = 260
                y_coordinate2 = 70
                Fields = []
                Data = []
                Symbol = []
                Symbol2 = []
                
                Para2Label = Label(root1, text="Enter the Values to Update ", bg="#000000", fg="#eec94c", font=('Hero',15))
                Para2Label.place(x=30, y=15)
                
                Para3Label = Label(root1, text="Enter the Row Key ", bg="#000000", fg="#eec94c", font=('Hero', 15), )
                Para3Label.place(x=30, y=250)
                
                for i in range(No):

                    Clicked = StringVar()
                    MyCombo = ttk.Combobox(root1, textvariable=Clicked, font=('Hero',12))
                    MyCombo['values'] = Col
                    MyCombo.current(0)
                    MyCombo.bind("<<ComboboxSelected>>")
                    MyCombo.place(x=x_coordinate, y=y_coordinate)
                    y_coordinate = y_coordinate + 40
                    Fields.append(MyCombo)

                    
                    #Para2Label = Label(root1, text="Enter the Value ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                    #Para2Label.place(x=20, y=60)
                    
                    #DatabaseLabel2 = Label(root1, text="Select Field", bg="#557A95", fg="#FFFFFF", font=(
                    #    'Hero', 20, ), )
                    #DatabaseLabel2.place(x=30, y=20)
                    
                    SearchDataEntry = StringVar()
                    SearchEntry = Entry(root1, font=('Hero',12),  textvariable=SearchDataEntry)
                    SearchEntry.place(x=x_coordinate2, y=y_coordinate2)
                    y_coordinate2 = y_coordinate2 + 40
                    Data.append(SearchEntry)
                
                Clicked = StringVar()
                MyCombo2 = ttk.Combobox(root1, textvariable=Clicked, font=('Hero',12))
                MyCombo2['values'] = Col
                MyCombo2.current(0)
                MyCombo2.bind("<<ComboboxSelected>>")
                MyCombo2.place(x=30,y=300)
                Symbol.append(MyCombo2) 
                
                SearchDataEntry2 = StringVar()
                SearchEntry2 = Entry(root1, font=('Hero',12),  textvariable=SearchDataEntry2)
                SearchEntry2.place(x=30, y=330)
                
                Symbol2.append(SearchEntry2)    

                SearchButton1 = Button(root1, text="Update", bg="#FFFFFF", width=8, font=(
                        "Hero", 14),relief=FLAT, command=lambda:UseClick4(Fields,Data,UsedTab,Col,Symbol,Symbol2))
                SearchButton1.place(x=270, y=300)
                return
            
            def UseClick4(Fields,Data,UsedTab,Col,Symbol,Symbol2):
            
                #global Contents, UsedTab
                Fields2 = []
                Data2 = []
                for i in Fields:
                    j = i.get()
                    Fields2.append(j)
                for k in Data:
                    l = k.get()
                    Data2.append(l)
                # print(Data2)
                # print(Fields2)            
                
                #Label2 = Label(root1, text="Table " + UsedTab + " selected", bg="#7395AE", fg="#FFFFFF", font=(
                #    'Hero', 20, ),)

                query = "show COLUMNS from %s" % (UsedTab)
                mycursor.execute(query)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])

                query1 = "desc %s" % (UsedTab)
                mycursor.execute(query1)
                GetData = mycursor.fetchall()
                DataTypes = []

                for q in GetData:
                    try:
                        B = q[1].decode('utf-8')
                        DataTypes.append(B)
                    except:
                        B = q[1]
                        DataTypes.append(B)
                
                DataTypes2 = []
                for l in DataTypes:
                    try:
                        C = l.index("(")
                        DataTypes2.append(l[0:C])
                    except ValueError:
                        DataTypes2.append(l)

                # print(DataTypes2)
                N = len(Data2)
                
                DataQuery = ""
                Empty = 0
                for i in Data2:
                    if i == '':
                        Empty = 1
                        messagebox.showerror(
                            'Please Enter all Fields', 'Enter all the Input Fields')
                        break
                        
                if Empty != 1:
                    for k in range(N):

                        A = Fields2[k]
                        for f in Col:
                            if f == A:
                                # print(f)
                                Index = Col.index(f)
                                # print(DataTypes2[Index])
                                if DataTypes2[Index] == "int":
                                    try:
                                        int(k)
                                        if k == N-1:
                                            DataQuery = DataQuery + f + "=" + Data2[k]
                                        else:
                                            DataQuery = DataQuery + f + "=" + Data2[k] + ","
                                    except ValueError:
                                        messagebox.showerror('Invalid Field Input',
                                                                'Please enter the corresponding data type')
                                        continue

                                elif DataTypes2[Index] == "float":
                                    try:
                                        float(k)
                                        if k == N-1:
                                            DataQuery = DataQuery + f + "=" + Data2[k]
                                        else:
                                            DataQuery = DataQuery + f + "=" + Data2[k] + ","
                                    except ValueError:
                                        messagebox.showerror('Invalid Field Input',
                                                                'Please enter the corresponding data type')
                                        continue
                                else:
                                    if k == N-1:
                                        DataQuery = DataQuery + f + "='" + Data2[k] +"'"
                                    else:
                                        DataQuery = DataQuery + f + "='" + Data2[k] +"', "
                    
                    S = Symbol[0].get()
                    S1 = Symbol2[0].get()
                    # print(S)
                    # print(S1)
                    
                    if S1.isdigit() == True:
                        query = "update %s set %s where %s = %s " % (UsedTab,DataQuery,S,S1)
                        # print(query)
                        mycursor.execute(query)
                    #Contents = mycursor.fetchall()
                        con.commit()
                    #Label2.place(x=55, y=300)
                        
                        
                    else:
                        query = "update %s set %s where %s = '%s' " % (UsedTab,DataQuery,S,S1)
                        # print(query)
                        mycursor.execute(query)
                    #Contents = mycursor.fetchall()
                        con.commit()
                    #Label2.place(x=55, y=300)
                    root1.destroy()
                    
                    TreeviewCode()
                        
                #SearchTable3(Contents)
                    
                # root2 = Tk()
                # root2.config(bg='#FFFFFF')
                # root2.geometry('845x590+200+200')
            
                # root2.title("Select the Field")
                
                # query1 = "show COLUMNS from %s" % (UsedTab)
                # # print(query1)
                # mycursor.execute(query1)
                # Columns = mycursor.fetchall()
                # Col = []
                # for i in Columns:
                #     Col.append(i[0])

                # showFrame = Frame(root2, bg='black', relief=FLAT, borderwidth=3)
                # showFrame.place(x=0, y=0, width=845, height=590)
                # xScrollBar = Scrollbar(showFrame, orient=HORIZONTAL)
                # yScrollBar = Scrollbar(showFrame, orient=VERTICAL)
                # contenttable = Treeview(showFrame, columns=Col, yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

                # style = ttk.Style()
                # style.configure('Treeview.Heading', font=(
                #                 'Hero', 30, 'bold'), foreground='black')
                # style.configure('Treeview', font=('Hero', 15, 'bold'),
                #                 bg='#7395AE', foreground='black')

                # xScrollBar.pack(side=BOTTOM, fill=X)
                # yScrollBar.pack(side=RIGHT, fill=Y)
                # xScrollBar.config(command=contenttable.xview)
                # yScrollBar.config(command=contenttable.yview)

                for i in Col:
                    contenttable.heading(i, text=i, anchor=CENTER)

                for j in Col:
                    contenttable.column(j, width=230)
                    contenttable['show'] = 'headings'
                    contenttable.pack(fill=BOTH, expand=1)

                command = 'select * from %s' % (UsedTab)
                mycursor.execute(command)
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    value = []
                    for j in range(len(Col)):
                        value.append(i[j])
                    contenttable.insert('', END, values=value)
                
                #root2.mainloop()    
                    
            root1 = Tk()
            root1.config(bg='#000000')
            root1.geometry('500x400+200+200')
            #root.resizable(False,False)
            root1.title("Update")
            
            query = "show COLUMNS from %s" % (UsedTab)
            mycursor.execute(query)
            Columns = mycursor.fetchall()
            Col = []
            for i in Columns:
                Col.append(i[0])

            ParaLabel3 = Label(root1, text="Enter the Number of fields ", bg="#000000", fg="#eec94c", font=('Hero', 20, ), )
            ParaLabel3.place(x=20, y=60)

            FieldNo3 = StringVar()
            FieldNoEntry3 = Entry(root1, width=20, font=('Hero',20), textvariable=FieldNo3)
            FieldNoEntry3.place(x=30, y=150) 

            NoButton3 = Button(root1, text="Next", bg="#eec94c",fg="black", width=8, font=(
                "Hero", 14), relief=FLAT ,command=lambda:UpdateInfo(FieldNoEntry3))
            NoButton3.place(x=30, y=215)  
                    
            root1.mainloop()
            
            return
        
        def DeleteData(UsedTab):
            
            def DeleteInfo(NO):
                        
                global No
                No = int(NO.get())

                ParaLabel3.destroy() 
                FieldNoEntry3.destroy()
                NoButton3.destroy()
                
                #ParaLabel = Label(root1, text="Select the Field ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                #ParaLabel.place(x=20, y=60) 

                x_coordinate = 30
                y_coordinate = 70
                x_coordinate2 = 260
                y_coordinate2 = 70
                Fields = []
                Data = []
                
                Para3Label = Label(root1, text="Enter the Search Parameters for Deletion ", bg="#000000", fg="#eec94c", font=('Hero', 15, ), )
                Para3Label.place(x=30, y=15)
                
                for i in range(No):

                    Clicked = StringVar()
                    MyCombo = ttk.Combobox(root1, textvariable=Clicked, font=('Hero',12))
                    MyCombo['values'] = Col
                    MyCombo.current(0)
                    MyCombo.bind("<<ComboboxSelected>>")
                    MyCombo.place(x=x_coordinate, y=y_coordinate)
                    y_coordinate = y_coordinate + 40
                    Fields.append(MyCombo)
                    
                    #Para2Label = Label(root1, text="Enter the Value ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                    #Para2Label.place(x=20, y=60)
                    
                    #DatabaseLabel2 = Label(root1, text="Select Field", bg="#557A95", fg="#FFFFFF", font=(
                    #    'Hero', 20, ), )
                    #DatabaseLabel2.place(x=30, y=20)
                    
                    SearchDataEntry = StringVar()
                    SearchEntry = Entry(root1, font=('Hero',12),  textvariable=SearchDataEntry)
                    SearchEntry.place(x=x_coordinate2, y=y_coordinate2)
                    y_coordinate2 = y_coordinate2 + 40
                    Data.append(SearchEntry)
                
                SearchButton1 = Button(root1, text="Use", bg="#eec94c",fg="#000000", width=8, font=(
                        "Hero", 14),relief=FLAT, command=lambda:UseClick4(Fields,Data,UsedTab,Col))
                SearchButton1.place(x=220, y=300)
                return
        
            def UseClick4(Fields,Data,UsedTab,Col):
                
                    #global Contents, UsedTab
                    Fields2 = []
                    Data2 = []
                    for i in Fields:
                        j = i.get()
                        Fields2.append(j)
                    for k in Data:
                        l = k.get()
                        Data2.append(l)
                    # print(Data2)
                    # print(Fields2)            
                    
                    #Label2 = Label(root1, text="Table " + UsedTab + " selected", bg="#7395AE", fg="#FFFFFF", font=(
                    #    'Hero', 20, ),)

                    query = "show COLUMNS from %s" % (UsedTab)
                    mycursor.execute(query)
                    Columns = mycursor.fetchall()
                    Col = []
                    for i in Columns:
                        Col.append(i[0])

                    query1 = "desc %s" % (UsedTab)
                    mycursor.execute(query1)
                    GetData = mycursor.fetchall()
                    DataTypes = []

                    for q in GetData:
                        try:
                            B = q[1].decode('utf-8')
                            DataTypes.append(B)
                        except:
                            B = q[1]
                            DataTypes.append(B)
                    DataTypes2 = []
                    
                    for l in DataTypes:
                        try:
                            C = l.index("(")
                            DataTypes2.append(l[0:C])
                        except ValueError:
                            DataTypes2.append(l)

                    # print(DataTypes2)
                    N = len(Data2)
                    
                    DataQuery = ""
                    Empty = 0
                    for i in Data2:
                        if i == '':
                            Empty = 1
                            messagebox.showerror(
                                'Please Enter all Fields', 'Enter all the Input Fields')
                            break
                    
                    
                    
                    if Empty != 1:
                        for k in range(N):

                            A = Fields2[k]
                            for f in Col:
                                if f == A:
                                    # print(f)
                                    Index = Col.index(f)
                                    # print(DataTypes2[Index])
                                    if DataTypes2[Index] == "int":
                                        try:
                                            int(k)
                                            if k == N-1:
                                                DataQuery = DataQuery + f + "=" + Data2[k]
                                            else:
                                                DataQuery = DataQuery + f + "=" + Data2[k] + " and "
                                        except ValueError:
                                            messagebox.showerror('Invalid Field Input',
                                                                    'Please enter the corresponding data type')
                                            continue

                                    elif DataTypes2[Index] == "float":
                                        try:
                                            float(k)
                                            if k == N-1:
                                                DataQuery = DataQuery + f + "=" + Data2[k]
                                            else:
                                                DataQuery = DataQuery + f + "=" + Data2[k] + " and "
                                        except ValueError:
                                            messagebox.showerror('Invalid Field Input',
                                                                    'Please enter the corresponding data type')
                                            continue
                                    else:
                                        if k == N-1:
                                            DataQuery = DataQuery + f + "='" + Data2[k] +"'"
                                        else:
                                            DataQuery = DataQuery + f + "='" + Data2[k] +"' and "
                        
                    
                        query = "delete from %s where %s " % (UsedTab,DataQuery)
                        # print(query)
                        mycursor.execute(query)
                        con.commit()
                        root1.destroy()    
                            
                        
                        TreeviewCode()
        
            root1 = Tk()
            root1.config(bg='#000000')
            root1.geometry('500x400+200+200')
            #root.resizable(False,False)
            root1.title("Delete")

            query = "show COLUMNS from %s" % (UsedTab)
            mycursor.execute(query)
            Columns = mycursor.fetchall()
            Col = []
            for i in Columns:
                Col.append(i[0])

            ParaLabel3 = Label(root1, text="Enter the Number of fields ", bg="#000000", fg="#eec94c", font=('Hero', 20, ), )
            ParaLabel3.place(x=20, y=60)

            FieldNo3 = StringVar()
            FieldNoEntry3 = Entry(root1, width=20, font=('Hero', 20, ), textvariable=FieldNo3)
            FieldNoEntry3.place(x=30, y=150) 

            NoButton3 = Button(root1, text="Next", bg="#eec94c",fg="black", width=8, font=(
                "Hero", 14), command=lambda: DeleteInfo(FieldNoEntry3))
            NoButton3.place(x=30, y=215) 
            
            root1.mainloop() 
            return
        
        def AlterData(UsedTab):
            
            def Add(UsedTab):
                
                def AlterInfo(NO):
                            
                    global No, Y
                    No = int(NO.get())

                    ParaLabel3.destroy() 
                    FieldNoEntry3.destroy()
                    NoButton3.destroy()
                    
                    #ParaLabel = Label(root1, text="Select the Field ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                    #ParaLabel.place(x=20, y=60) 

                    x_coordinate = 260
                    y_coordinate = 70
                    x_coordinate2 = 30
                    y_coordinate2 = 70
                    Fields = []
                    Data = []
                    Symbol = []
                    ChLimit = []
                    
                    for i in range(No):

                        Clicked = StringVar()
                        MyCombo = ttk.Combobox(root2, textvariable=Clicked, font=('Hero',12))
                        MyCombo['values'] = ["int","varchar","float","char"]
                        MyCombo.current(0)
                        MyCombo.bind("<<ComboboxSelected>>")
                        MyCombo.place(x=x_coordinate, y=y_coordinate2)
                        y_coordinate = y_coordinate + 40
                        Fields.append(MyCombo)
                        
                                    
                        #Para2Label = Label(root1, text="Enter the Value ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                        #Para2Label.place(x=20, y=60)
                        
                        #DatabaseLabel2 = Label(root1, text="Select Field", bg="#557A95", fg="#FFFFFF", font=(
                        #    'Hero', 20, ), )
                        #DatabaseLabel2.place(x=30, y=20)
                        
                        SearchDataEntry = StringVar()
                        SearchEntry = Entry(root2, font=('Hero',12),  textvariable=SearchDataEntry)
                        SearchEntry.place(x=x_coordinate2, y=y_coordinate2)
                        
                        Data.append(SearchEntry)
                    
                        SearchDataEntry2 = StringVar()
                        SearchEntry2 = Entry(root2, font=('Hero',12),  textvariable=SearchDataEntry2)
                        SearchEntry2.place(x=x_coordinate2  , y=y_coordinate2+30)
                        ChLimit.append(SearchEntry2)  
                        y_coordinate2 = y_coordinate2 + 70
                        
                    # Clicked = StringVar()
                    # MyCombo2 = ttk.Combobox(root1, textvariable=Clicked, font=('Hero',12))
                    # MyCombo2['values'] = ["add","modify","drop"]
                    # MyCombo2.current(0)
                    # MyCombo2.bind("<<ComboboxSelected>>")
                    # MyCombo2.place(x=30,y=300)
                    # Symbol.append(MyCombo2)
                    
                    SearchButton1 = Button(root2, text="Use", bg="#FFFFFF", width=8, font=(
                            "Hero", 10),relief=FLAT, command=lambda:UseClick4(Fields,Data,UsedTab,Col,ChLimit))
                    SearchButton1.place(x=270, y=300)
 
       
                def UseClick4(Fields,Data,UsedTab,Col,ChLimit):
                    
                    #global Contents, UsedTab
                    Fields2 = []
                    Data2 = []
                    for i in Fields:
                        j = i.get()
                        Fields2.append(j)
                    for k in Data:
                        l = k.get()
                        Data2.append(l)
                    # print(Data2)
                    # print(Fields2)            
                    
                    #Label2 = Label(root1, text="Table " + UsedTab + " selected", bg="#7395AE", fg="#FFFFFF", font=(
                    #    'Hero', 20, ),)

                    query = "show COLUMNS from %s" % (UsedTab)
                    mycursor.execute(query)
                    Columns = mycursor.fetchall()
                    Col = []
                    for i in Columns:
                        Col.append(i[0])

                    query1 = "desc %s" % (UsedTab)
                    mycursor.execute(query1)
                    GetData = mycursor.fetchall()
                    DataTypes = []

                    for q in GetData:
                        try:
                            B = q[1].decode('utf-8')
                            DataTypes.append(B)
                        except:
                            B = q[1]
                            DataTypes.append(B)
                    DataTypes2 = []
                    
                    for l in DataTypes:
                        try:
                            C = l.index("(")
                            DataTypes2.append(l[0:C])
                        except ValueError:
                            DataTypes2.append(l)

                    # print(DataTypes2)
                    N = len(Data2)
                    
                    DataQuery = ""
                    Empty = 0
                    for i in Data2:
                        if i == '':
                            Empty = 1
                            messagebox.showerror(
                                'Please Enter all Fields', 'Enter all the Input Fields')
                            break
                    S = []
                    for r in ChLimit:
                        b = r.get()
                        S.append(b)
                            
                    if Empty != 1:
                        for k in range(N):
                            
                            if k == N-1:
                                DataQuery = DataQuery + " " + Data2[k] + " " + Fields2[k] + "(" + S[k] + ")"                      
                            else:
                                DataQuery = DataQuery + " " + Data2[k] + " " + Fields2[k] + "(" + S[k] + ")" + ", add"
                                            
                        # print(S)
                        
                        
                        query = "alter table %s add %s " % (UsedTab,DataQuery)
                        # print(query)
                        mycursor.execute(query)
                        #Contents = mycursor.fetchall()
                        con.commit()
                        #Label2.place(x=55, y=300)
                            
                        root2.destroy()
                    
                    TreeviewCode()
                
                root2 = Tk()
                root2.config(bg='#000000')
                root2.geometry('500x400+200+200')
                #root.resizable(False,False)
                root2.title("Select the Field")
                
                query = "show COLUMNS from %s" % (UsedTab)
                mycursor.execute(query)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])

                ParaLabel3 = Label(root2, text="Enter the Number of fields ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                ParaLabel3.place(x=20, y=60)

                FieldNo3 = StringVar()
                FieldNoEntry3 = Entry(root2, width=20, font=20, textvariable=FieldNo3)
                FieldNoEntry3.place(x=30, y=150) 
                
                NoButton3 = Button(root2, text="Use", bg="#FFFFFF", width=8, font=(
                "Hero", 10), command=lambda:AlterInfo(FieldNoEntry3))
                NoButton3.place(x=80, y=110)
                
                root2.mainloop()
            
            def Modify(UsedTab):
                
                def UseClick5(Fields,Data,UsedTab,Col,ChLimit):
                    
                    #global Contents, UsedTab
                    Fields2 = []
                    Data2 = []
                    for i in Fields:
                        j = i.get()
                        Fields2.append(j)
                    for k in Data:
                        l = k.get()
                        Data2.append(l)
                    # print(Data2)
                    # print(Fields2)            
                    
                    #Label2 = Label(root1, text="Table " + UsedTab + " selected", bg="#7395AE", fg="#FFFFFF", font=(
                    #    'Hero', 20, ),)

                    query = "show COLUMNS from %s" % (UsedTab)
                    mycursor.execute(query)
                    Columns = mycursor.fetchall()
                    Col = []
                    for i in Columns:
                        Col.append(i[0])

                    query1 = "desc %s" % (UsedTab)
                    mycursor.execute(query1)
                    GetData = mycursor.fetchall()
                    DataTypes = []

                    for q in GetData:
                        try:
                            B = q[1].decode('utf-8')
                            DataTypes.append(B)
                        except:
                            B = q[1]
                            DataTypes.append(B)
                    DataTypes2 = []
                    
                    for l in DataTypes:
                        try:
                            C = l.index("(")
                            DataTypes2.append(l[0:C])
                        except ValueError:
                            DataTypes2.append(l)

                    # print(DataTypes2)
                    N = len(Data2)
                    
                    S = []
                    for r in ChLimit:
                        b =r.get()
                        S.append(b)
                    
                    DataQuery = ""
                    Empty = 0
                    for i in Data2:
                        if i == '':
                            Empty = 1
                            messagebox.showerror(
                                'Please Enter all Fields', 'Enter all the Input Fields')
                            break
                    
                                
                    if Empty != 1:
                        for k in range(N):
                            
                            if k == N-1:
                                DataQuery = DataQuery + " " + Data2[k] + " " + Fields2[k] + "(" + S[k] + ")"                      
                            else:
                                DataQuery = DataQuery + " " + Data2[k] + " " + Fields2[k] + "(" + S[k] + ")" + ", modify"
                                                
                        # print(S)
                        
                        
                        query = "alter table %s modify %s " % (UsedTab,DataQuery)
                        # print(query)
                        mycursor.execute(query)
                        #Contents = mycursor.fetchall()
                        con.commit()
                        #Label2.place(x=55, y=300)
                                
                        root2.destroy()
                        
                        TreeviewCode()
                def ModifyInfo(NO):
                            
                    global No, Y
                    No = int(NO.get())

                    ParaLabel3.destroy() 
                    FieldNoEntry3.destroy()
                    NoButton3.destroy()
                    
                    #ParaLabel = Label(root1, text="Select the Field ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                    #ParaLabel.place(x=20, y=60) 

                    x_coordinate = 260
                    y_coordinate = 70
                    x_coordinate2 = 30
                    y_coordinate2 = 70
                    Fields = []
                    Data = []
                    Symbol = []
                    ChLimit = []
                    
                    for i in range(No):

                        Clicked = StringVar()
                        MyCombo = ttk.Combobox(root2, textvariable=Clicked, font=('Hero',12))
                        MyCombo['values'] = ["int","varchar","float","char"]
                        MyCombo.current(0)
                        MyCombo.bind("<<ComboboxSelected>>")
                        MyCombo.place(x=x_coordinate, y=y_coordinate2)
                        y_coordinate = y_coordinate + 40
                        Fields.append(MyCombo)
                        
                                    
                        #Para2Label = Label(root1, text="Enter the Value ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                        #Para2Label.place(x=20, y=60)
                        
                        #DatabaseLabel2 = Label(root1, text="Select Field", bg="#557A95", fg="#FFFFFF", font=(
                        #    'Hero', 20, ), )
                        #DatabaseLabel2.place(x=30, y=20)
                        Clicked = StringVar()
                        MyCombo2 = ttk.Combobox(root2, textvariable=Clicked, font=('Hero',12))
                        MyCombo2['values'] = Col
                        MyCombo2.current(0)
                        MyCombo2.bind("<<ComboboxSelected>>")
                        MyCombo2.place(x=x_coordinate2, y=y_coordinate2)
                        Data.append(MyCombo2)
                            
                        
                        # SearchDataEntry = StringVar()
                        # SearchEntry = Entry(root2, font=('Hero',12),  textvariable=SearchDataEntry)
                        # SearchEntry.place(x=x_coordinate2, y=y_coordinate2)
                        
                        # Data.append(SearchEntry)
                    
                        SearchDataEntry2 = StringVar()
                        SearchEntry2 = Entry(root2, font=('Hero',12),  textvariable=SearchDataEntry2)
                        SearchEntry2.place(x=x_coordinate2  , y=y_coordinate2+30)
                        ChLimit.append(SearchEntry2)  
                        y_coordinate2 = y_coordinate2 + 70
                        
                    # Clicked = StringVar()
                    # MyCombo2 = ttk.Combobox(root1, textvariable=Clicked, font=('Hero',12))
                    # MyCombo2['values'] = ["add","modify","drop"]
                    # MyCombo2.current(0)
                    # MyCombo2.bind("<<ComboboxSelected>>")
                    # MyCombo2.place(x=30,y=300)
                    # Symbol.append(MyCombo2)
                    
                    SearchButton1 = Button(root2, text="Use", bg="#FFFFFF", width=8, font=(
                            "Hero", 10),relief=FLAT, command=lambda:UseClick5(Fields,Data,UsedTab,Col,ChLimit))
                    SearchButton1.place(x=270, y=300)
                
                root2 = Tk()
                root2.config(bg='#557A95')
                root2.geometry('500x400+200+200')
                #root.resizable(False,False)
                root2.title("Select the Field")
                
                query = "show COLUMNS from %s" % (UsedTab)
                mycursor.execute(query)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])

                ParaLabel3 = Label(root2, text="Enter the Number of fields ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                ParaLabel3.place(x=20, y=60)

                FieldNo3 = StringVar()
                FieldNoEntry3 = Entry(root2, width=20, font=20, textvariable=FieldNo3)
                FieldNoEntry3.place(x=30, y=150) 
                
                NoButton3 = Button(root2, text="Use", bg="#FFFFFF", width=8, font=(
                "Hero", 10), command=lambda:ModifyInfo(FieldNoEntry3))
                NoButton3.place(x=80, y=110)
                
                root2.mainloop()
                    
                return
            
            def Drop(UsedTab):
                
                def UseClick6(UsedTab,ColumnEntry):
                    
                    Column = ColumnEntry[0].get()
                    query = "alter table %s drop column %s" % (UsedTab,Column)
                    # print(query)
                    mycursor.execute(query)
                    #Contents = mycursor.fetchall()
                    con.commit()
                    #Label2.place(x=55, y=300)
                            
                    root2.destroy()
                    
                    TreeviewCode()   
                                 
                    return
                
                DelCol = []
                root2 = Tk()
                root2.config(bg='#557A95')
                root2.geometry('500x400+200+200')
                #root.resizable(False,False)
                root2.title("Select the Field")
                
                query = "show COLUMNS from %s" % (UsedTab)
                mycursor.execute(query)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])
                    
                ParaLabel3 = Label(root2, text="Select the Column ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                ParaLabel3.place(x=20, y=60)

                Clicked = StringVar()
                MyCombo3 = ttk.Combobox(root2, textvariable=Clicked, font=('Hero',12))
                MyCombo3['values'] = Col
                MyCombo3.current(0)
                MyCombo3.bind("<<ComboboxSelected>>")
                MyCombo3.place(x=30, y=150)
                DelCol.append(MyCombo3) 
                
                NoButton3 = Button(root2, text="Use", bg="#FFFFFF", width=8, font=(
                "Hero", 10), command=lambda:UseClick6(UsedTab,DelCol))
                NoButton3.place(x=80, y=110)   
                    
                root2.mainloop()    
                
                return 
            
            def SetPrimaryKey(UsedTab):
                
                def UseClick7(UsedTab,ColumnEntry):
                    
                    query = "select constraint_name from information_schema.table_constraints where table_name = '%s' and constraint_name = 'PRIMARY'" % (UsedTab)
                    mycursor.execute(query)
                    Data = mycursor.fetchall()
                    
                    if Data != []:
                        messagebox.showerror('Multiple Primary keys',
                                                        'Primary key already exists',parent=root2)
                        root2.destroy()
                    
                    else:
                        Column = ColumnEntry[0].get()
                        query = "alter table %s add primary key(%s)" % (UsedTab,Column)
                        # print(query)
                        mycursor.execute(query)
                        #Contents = mycursor.fetchall()
                        con.commit()
                        #Label2.place(x=55, y=300)
                                
                        root2.destroy()
                    
                PrimaryCol = []
                root2 = Tk()
                root2.config(bg='#557A95')
                root2.geometry('500x400+200+200')
                #root.resizable(False,False)
                root2.title("Select the Field")
                
                query = "show COLUMNS from %s" % (UsedTab)
                mycursor.execute(query)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])
                    
                ParaLabel3 = Label(root2, text="Select the Column ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                ParaLabel3.place(x=20, y=60)

                Clicked = StringVar()
                MyCombo3 = ttk.Combobox(root2, textvariable=Clicked, font=('Hero',12))
                MyCombo3['values'] = Col
                MyCombo3.current(0)
                MyCombo3.bind("<<ComboboxSelected>>")
                MyCombo3.place(x=30, y=150)
                PrimaryCol.append(MyCombo3) 
                
                NoButton3 = Button(root2, text="Use", bg="#FFFFFF", width=8, font=(
                "Hero", 10), command=lambda:UseClick7(UsedTab,PrimaryCol))
                NoButton3.place(x=80, y=110)   
                    
                root2.mainloop()           
                
            root1 = Tk()
            root1.config(bg='#000000')
            root1.geometry('500x500+200+200')
            #root.resizable(False,False)
            root1.title("Alter Contents")
            
            AlterLabel3 = Label(root1, text="Alter", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
            AlterLabel3.place(x=20, y=60)
            
            
            Search1Button = Button(root1, text="Add", bg="#FFFFFF", width=26,relief= FLAT, font=("Hero",19),command=lambda:Add(UsedTab))
            Search1Button.place(x=50, y=80)

            Search2Button = Button(root1, text="Modify", bg="#FFFFFF", width=26, relief=FLAT,font=("Hero",19), command=lambda:Modify(UsedTab))
            Search2Button.place(x=50, y=160)

            Search3Button = Button(root1, text="Drop", bg="#FFFFFF", width=26, relief=FLAT, font=("Hero",19), command=lambda:Drop(UsedTab))
            Search3Button.place(x=50, y=240) 
            
            Search4Button = Button(root1, text="Set Primary Key", bg="#FFFFFF", width=26, relief=FLAT, font=("Hero",19), command=lambda:SetPrimaryKey(UsedTab))
            Search4Button.place(x=50, y=320)    
                
            root1.mainloop()
            
            
        def TreeviewCode():
            
            query = "show COLUMNS from %s" % (UsedTab)
            mycursor.execute(query)
            Columns = mycursor.fetchall()
            Col = []
            for i in Columns:
                Col.append(i[0])
                
            showFrame = Frame(root8, bg='black', relief=FLAT, borderwidth=3)
            showFrame.place(x=330, y=110, width=845, height=590)
            xScrollBar = Scrollbar(showFrame, orient=HORIZONTAL)
            yScrollBar = Scrollbar(showFrame, orient=VERTICAL)
            contenttable = Treeview(showFrame, columns=Col, yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

            style = ttk.Style()
            style.configure('Treeview.Heading', font=('Hero', 20), foreground='black')
            style.configure('Treeview', font=('Hero', 15),
                            bg='#7395AE', foreground='black')

            xScrollBar.pack(side=BOTTOM, fill=X)
            yScrollBar.pack(side=RIGHT, fill=Y)
            xScrollBar.config(command=contenttable.xview)
            yScrollBar.config(command=contenttable.yview)

            for i in Col:
                contenttable.heading(i, text=i, anchor=CENTER)

            for j in Col:
                contenttable.column(j, width=150)
            contenttable['show'] = 'headings'
            contenttable.pack(fill=BOTH, expand=1)

            command = 'select * from %s' % (UsedTab)
            mycursor.execute(command)
            contents = mycursor.fetchall()
            contenttable.delete(*contenttable.get_children())

            for i in contents:
                value = []
                for j in range(len(Col)):
                    value.append(i[j])
                contenttable.insert('', END, values=value)
            return contenttable
            
        def ExportData(UsedTab):
            
            if con.is_connected():
                
                global contenttable
                
                query = "show COLUMNS from %s" % (UsedTab)
                mycursor.execute(query)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])
                    
                showFrame = Frame(root8, bg='black', relief=FLAT, borderwidth=3)
                showFrame.place(x=330, y=110, width=845, height=590)
                xScrollBar = Scrollbar(showFrame, orient=HORIZONTAL)
                yScrollBar = Scrollbar(showFrame, orient=VERTICAL)
                contenttable = Treeview(showFrame, columns=Col, yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

                style = ttk.Style()
                style.configure('Treeview.Heading', font=('Hero', 20), foreground='black')
                style.configure('Treeview', font=('Hero', 15),
                                bg='#7395AE', foreground='black')

                xScrollBar.pack(side=BOTTOM, fill=X)
                yScrollBar.pack(side=RIGHT, fill=Y)
                xScrollBar.config(command=contenttable.xview)
                yScrollBar.config(command=contenttable.yview)

                for i in Col:
                    contenttable.heading(i, text=i, anchor=CENTER)

                for j in Col:
                    contenttable.column(j, width=150)
                contenttable['show'] = 'headings'
                contenttable.pack(fill=BOTH, expand=1)

                command = 'select * from %s' % (UsedTab)
                mycursor.execute(command)
                contents = mycursor.fetchall()
                contenttable.delete(*contenttable.get_children())

                for i in contents:
                    value = []
                    for j in range(len(Col)):
                        value.append(i[j])
                    contenttable.insert('', END, values=value)
                
            
            
            query = "show COLUMNS from %s" % (UsedTab)
            # print(query)
            mycursor.execute(query)
            Columns = mycursor.fetchall()
            Col = []
            for i in Columns:
                Col.append(i[0])
            # print(Col)

            root8.withdraw()
            a = asksaveasfilename()
            root8.call('wm', 'attributes', '.', '-topmost', True)
            b = contenttable.get_children()
            # print(b)
            
            Cols = []
            # for j in Col:
            #     j = []
            #     Cols.append(j)
                
            for i in b:
                contents = contenttable.item(i)
                # print(contents)
                c = contents['values']
                # print(c)
                Cols.append(c)
            # print(Cols)

            List = []
            for f in Cols:
                List.append(f)

            ZippedList = tuple(List)
            # print(ZippedList)
            # print(zip(ZippedList))    
            fin = DataFrame(List, columns=Col)
            path = a+'.csv'
            fin.to_csv(path,index=False)
            messagebox.showinfo('Success!','Student Data Saved Successfully! {} '.format(path))
        
        
        
        root8 = Tk()
        root8.title("Zesca")
        root8.geometry('1174x700+200+50')
        root8.config(bg="#000000")
        root8.resizable(False, False)
        
        
        
        UsedTab = "Teacher"
        
        headingFrame2 = Frame(root8, bg="#eec94c", relief=RIDGE,)
        headingFrame2.place(x=0, y=0, width=1174, height=110)

        head = "ZESCA"
        headLabel = Label(headingFrame2, text=head, bg="#eec94c", fg="#000000", font=(
            'Elianto', 40, ), )
        headLabel.place(x=26, y=20)

        dataEntryFrame = Frame(root8, bg='#5D5C61', relief=RIDGE, )
        dataEntryFrame.place(x=0, y=110, width=330, height=620)
        
        UsingTableName1 = "Table: "
        TableHeader1 = Label(dataEntryFrame, text=UsingTableName1, bg="#5D5C61", fg="#FFFFFF", font=(
            'Hero', 20, ))
        TableHeader1.place(x=22, y=20)

        UsingTableName2 = UsedTab
        TableHeader2 = Label(dataEntryFrame, text=UsingTableName2, bg="#5D5C61", fg="#FFFFFF", font=(
            'Hero', 20, ))
        TableHeader2.place(x=22, y=60)    
            
        InsertDataButton = Button(root8, text="Insert Data", bg="#FFFFFF", width=15,relief= FLAT, font=("Hero",19), command=lambda:InsertTable(UsedTab))
        InsertDataButton.place(x=47, y=220)
        
        SearchDataButton = Button(root8, text="Search Data", bg="#FFFFFF", width=15,relief= FLAT, font=("Hero",19), command=lambda:SearchData(UsedTab))
        SearchDataButton.place(x=47, y=290)
        
        UpdateDataButton = Button(root8, text="Update Data", bg="#FFFFFF", width=15,relief= FLAT, font=("Hero",19), command=lambda:UpdateData(UsedTab))
        UpdateDataButton.place(x=47, y=360)
        
        DeleteDataButton = Button(root8, text="Delete Data", bg="#FFFFFF", width=15,relief= FLAT, font=("Hero",19), command=lambda:DeleteData(UsedTab))
        DeleteDataButton.place(x=47, y=430)
        
        AlterDataButton = Button(root8, text="Alter Data", bg="#FFFFFF", width=15,relief= FLAT, font=("Hero",19), command=lambda:AlterData(UsedTab))
        AlterDataButton.place(x=47, y=500)

        ExportDataButton = Button(root8, text="Export Data", bg="#FFFFFF", width=15,relief= FLAT, font=("Hero",19), command=lambda:ExportData(UsedTab))
        ExportDataButton.place(x=47, y=570)
        
        connectButton = Button(root8, text="Connect to DB", font=('Hero', 15), bg='black', fg ="#eec94c", relief=FLAT,
                        width=15 ,command=ConnectSQL)
        connectButton.place(x=950, y=30)
        
        
                        
        root8.mainloop()
        
    def SearchData(UsedTab):
        
        def Search1(UsedTab):
            
            root1 = Tk()
            root1.config(bg='#557A95')
            root1.geometry('500x400+200+200')
            # root.resizable(False,False)
            root1.title("Select the Field")
            
            def SearchTable1(Contents):
                
                root2 = Tk()
                root2.config(bg='#FFFFFF')
                root2.geometry('845x590+200+200')
            
                root2.title("Select the Field")
                
                query1 = "show COLUMNS from %s" % (UsedTab)
                # print(query1)
                mycursor.execute(query1)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])

                showFrame = Frame(root2, bg='black', relief=FLAT, borderwidth=3)
                showFrame.place(x=0, y=0, width=845, height=590)
                xScrollBar = Scrollbar(showFrame, orient=HORIZONTAL)
                yScrollBar = Scrollbar(showFrame, orient=VERTICAL)
                contenttable = Treeview(showFrame, columns=Col, yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

                style = ttk.Style()
                style.configure('Treeview.Heading', font=(
                                'Hero',20), foreground='black')
                style.configure('Treeview', font=('Hero', 15),
                                bg='#7395AE', foreground='black')

                xScrollBar.pack(side=BOTTOM, fill=X)
                yScrollBar.pack(side=RIGHT, fill=Y)
                xScrollBar.config(command=contenttable.xview)
                yScrollBar.config(command=contenttable.yview)

                for i in Col:
                    contenttable.heading(i, text=i, anchor=CENTER)

                for j in Col:
                    contenttable.column(j, width=230)
                    contenttable['show'] = 'headings'
                    contenttable.pack(fill=BOTH, expand=1)

                #command = 'select * from %s' % (UsedTab)
                # mycursor.execute(command)
                #contents = mycursor.fetchall()
                #contenttable.delete(*contenttable.get_children())

                for i in Contents:
                    value = []
                    for j in range(len(Col)):
                        value.append(i[j])
                    contenttable.insert('', END, values=value)
                
                root2.mainloop()    
            
            def ComboClick1(object):
                
                global Please
                Please = MyCombo.get()
                # print(Please)
                return Please    
                
            def UseClick(SearchDataEntry, UsedTab):

                #global Contents, UsedTab
                
                Check = ComboClick1(object)
                # print(Check)
                            
                Value = SearchDataEntry.get()
                
                #Label2 = Label(root1, text="Table " + UsedTab + " selected", bg="#7395AE", fg="#FFFFFF", font=(
                #    'Hero', 20, ),)
                query = "select * from %s where %s ='%s' " % (UsedTab,Check,Value)
                # print(query)
                mycursor.execute(query)
                Contents = mycursor.fetchall()

                #Label2.place(x=55, y=300)
                root1.destroy()
                
                SearchTable1(Contents)
                        
            query = "show COLUMNS from %s" % (UsedTab)
            mycursor.execute(query)
            Columns = mycursor.fetchall()
            Col = []
            for i in Columns:
                Col.append(i[0])
                
            ParaLabel = Label(root1, text="Select the Field ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
            ParaLabel.place(x=20, y=60)    

            Clicked = StringVar()
            
            MyCombo = ttk.Combobox(root1, textvariable=Clicked)
            MyCombo['values'] = Col
            MyCombo.current(0)
            MyCombo.bind("<<ComboboxSelected>>", ComboClick1)
            MyCombo.place(x=280, y=30)
            
            Para2Label = Label(root1, text="Enter the Value ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
            Para2Label.place(x=20, y=60)
            
            DatabaseLabel2 = Label(root1, text="Select Table", bg="#557A95", fg="#FFFFFF", font=(
                'Hero', 20, ), )
            DatabaseLabel2.place(x=30, y=20)
            
            SearchDataEntry = StringVar()
            SearchEntry = Entry(root1, width=20, font=20, textvariable=SearchDataEntry)
            SearchEntry.place(x=30, y=150)

            SearchButton1 = Button(root1, text="Use", bg="#FFFFFF", width=8, font=(
                "Hero", 10), command=lambda: UseClick(SearchEntry,UsedTab))
            SearchButton1.place(x=80, y=110)

        def Search2(UsedTab):
            
            root1 = Tk()
            root1.config(bg='#557A95')
            root1.geometry('500x400+200+200')
            # root.resizable(False,False)
            root1.title("Select the Field")

            def FieldNo(NO):
                
                
                global No, Y
                No = int(NO.get())

                ParaLabel1.destroy() 
                FieldNoEntry.destroy()
                NoButton1.destroy()
                
                #ParaLabel = Label(root1, text="Select the Field ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                #ParaLabel.place(x=20, y=60) 

                x_coordinate = 30
                y_coordinate = 40
                x_coordinate2 = 260
                y_coordinate2 = 40
                Fields = []
                Data = []
                for i in range(No):

                    Clicked = StringVar()
                    MyCombo = ttk.Combobox(root1, textvariable=Clicked, font=('Hero',12))
                    MyCombo['values'] = Col
                    MyCombo.current(0)
                    MyCombo.bind("<<ComboboxSelected>>")
                    MyCombo.place(x=x_coordinate, y=y_coordinate)
                    y_coordinate = y_coordinate + 40
                    Fields.append(MyCombo)

                    
                    #Para2Label = Label(root1, text="Enter the Value ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                    #Para2Label.place(x=20, y=60)
                    
                    #DatabaseLabel2 = Label(root1, text="Select Field", bg="#557A95", fg="#FFFFFF", font=(
                    #    'Hero', 20, ), )
                    #DatabaseLabel2.place(x=30, y=20)
                    
                    SearchDataEntry = StringVar()
                    SearchEntry = Entry(root1, font=('Hero',12),  textvariable=SearchDataEntry)
                    SearchEntry.place(x=x_coordinate2, y=y_coordinate2)
                    y_coordinate2 = y_coordinate2 + 40
                    Data.append(SearchEntry)

                SearchButton1 = Button(root1, text="Use", bg="#FFFFFF", width=8, font=(
                        "Hero", 10), command=lambda: UseClick1(Fields,Data,UsedTab,Col))
                SearchButton1.place(x=170, y=300)
                return
            
            def SearchTable2(Contents):

                root2 = Tk()
                root2.config(bg='#FFFFFF')
                root2.geometry('845x590+200+200')
            
                root2.title("Select the Field")
                
                query1 = "show COLUMNS from %s" % (UsedTab)
                # print(query1)
                mycursor.execute(query1)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])

                showFrame = Frame(root2, bg='black', relief=FLAT, borderwidth=3)
                showFrame.place(x=0, y=0, width=845, height=590)
                xScrollBar = Scrollbar(showFrame, orient=HORIZONTAL)
                yScrollBar = Scrollbar(showFrame, orient=VERTICAL)
                contenttable = Treeview(showFrame, columns=Col, yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

                style = ttk.Style()
                style.configure('Treeview.Heading', font=(
                                'Hero', 20), foreground='black')
                style.configure('Treeview', font=('Hero', 15),
                                bg='#7395AE', foreground='black')

                xScrollBar.pack(side=BOTTOM, fill=X)
                yScrollBar.pack(side=RIGHT, fill=Y)
                xScrollBar.config(command=contenttable.xview)
                yScrollBar.config(command=contenttable.yview)

                for i in Col:
                    contenttable.heading(i, text=i, anchor=CENTER)

                for j in Col:
                    contenttable.column(j, width=150)
                    contenttable['show'] = 'headings'
                    contenttable.pack(fill=BOTH, expand=1)

                #command = 'select * from %s' % (UsedTab)
                # mycursor.execute(command)
                #contents = mycursor.fetchall()
                #contenttable.delete(*contenttable.get_children())

                for i in Contents:
                    value = []
                    for j in range(len(Col)):
                        value.append(i[j])
                    contenttable.insert('', END, values=value)
                
                root2.mainloop()    
            
            def UseClick1(Fields, Data, UsedTab, Col):

                #global Contents, UsedTab
                Fields2 = []
                Data2 = []
                for i in Fields:
                    j = i.get()
                    Fields2.append(j)
                for k in Data:
                    l = k.get()
                    Data2.append(l)
                # print(Data2)
                # print(Fields2)            
                
                #Label2 = Label(root1, text="Table " + UsedTab + " selected", bg="#7395AE", fg="#FFFFFF", font=(
                #    'Hero', 20, ),)

                query = "show COLUMNS from %s" % (UsedTab)
                mycursor.execute(query)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])

                query1 = "desc %s" % (UsedTab)
                mycursor.execute(query1)
                GetData = mycursor.fetchall()
                DataTypes = []

                for i in GetData:
                    B = i[1].decode('utf-8')
                    DataTypes.append(B)
                DataTypes2 = []
                
                for l in DataTypes:
                    try:
                        C = l.index("(")
                        DataTypes2.append(l[0:C])
                    except ValueError:
                        DataTypes2.append(l)

                # print(DataTypes2)
                N = len(Data2)
                
                DataQuery = ""
                Empty = 0
                for i in Data2:
                    if i == '':
                        Empty = 1
                        messagebox.showerror(
                            'Please Enter all Fields', 'Enter all the Input Fields')
                        break

                if Empty != 1:
                    for k in range(N):

                        A = Fields2[k]
                        for f in Col:
                            if f == A:
                                # print(f)
                                Index = Col.index(f)
                                # print(DataTypes2[Index])
                                if DataTypes2[Index] == "int":
                                    try:
                                        int(k)
                                        if k == N-1:
                                            DataQuery = DataQuery + f + "=" + Data2[k]
                                        else:
                                            DataQuery = DataQuery + f + "=" + Data2[k] + "and"
                                    except ValueError:
                                        messagebox.showerror('Invalid Field Input',
                                                                'Please enter the corresponding data type')
                                        continue

                                elif DataTypes2[Index] == "float":
                                    try:
                                        float(k)
                                        if k == N-1:
                                            DataQuery = DataQuery + f + "=" + Data2[k]
                                        else:
                                            DataQuery = DataQuery + f + "=" + Data2[k] + "and"
                                    except ValueError:
                                        messagebox.showerror('Invalid Field Input',
                                                                'Please enter the corresponding data type')
                                        continue
                                else:
                                    if k == N-1:
                                        DataQuery = DataQuery + f + "='" + Data2[k] +"'"
                                    else:
                                        DataQuery = DataQuery + f + "='" + Data2[k] +"' and "
                
                query = "select * from %s where %s " % (UsedTab,DataQuery)
                
                # print(query)
                mycursor.execute(query)
                Contents = mycursor.fetchall()

                #Label2.place(x=55, y=300)
                root1.destroy()
                
                SearchTable2(Contents)
            
            
            query = "show COLUMNS from %s" % (UsedTab)
            mycursor.execute(query)
            Columns = mycursor.fetchall()
            Col = []
            for i in Columns:
                Col.append(i[0])

            ParaLabel1 = Label(root1, text="Enter the Number of fields ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
            ParaLabel1.place(x=20, y=60)

            FieldNoEntry = StringVar()
            FieldNoEntry = Entry(root1, width=20, font=20, textvariable=FieldNoEntry)
            FieldNoEntry.place(x=30, y=150) 

            NoButton1 = Button(root1, text="Use", bg="#FFFFFF", width=8, font=(
                "Hero", 10), command=lambda: FieldNo(FieldNoEntry))
            NoButton1.place(x=80, y=110)  

        def Search3(UsedTab):
            
            root1 = Tk()
            root1.config(bg='#557A95')
            root1.geometry('500x400+200+200')
            # root.resizable(False,False)
            root1.title("Select the Field")
            
            def FieldNo2(NO):
                    
                global No, Y
                No = int(NO.get())

                ParaLabel2.destroy() 
                FieldNoEntry2.destroy()
                NoButton2.destroy()
                
                #ParaLabel = Label(root1, text="Select the Field ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                #ParaLabel.place(x=20, y=60) 

                x_coordinate = 30
                y_coordinate = 70
                x_coordinate2 = 260
                y_coordinate2 = 70
                Fields = []
                Data = []
                Symbol = []
                for i in range(No):

                    Clicked = StringVar()
                    MyCombo = ttk.Combobox(root1, textvariable=Clicked, font=('Hero',12))
                    MyCombo['values'] = Col
                    MyCombo.current(0)
                    MyCombo.bind("<<ComboboxSelected>>")
                    MyCombo.place(x=x_coordinate, y=y_coordinate)
                    y_coordinate = y_coordinate + 40
                    Fields.append(MyCombo)

                    
                    #Para2Label = Label(root1, text="Enter the Value ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
                    #Para2Label.place(x=20, y=60)
                    
                    #DatabaseLabel2 = Label(root1, text="Select Field", bg="#557A95", fg="#FFFFFF", font=(
                    #    'Hero', 20, ), )
                    #DatabaseLabel2.place(x=30, y=20)
                    
                    SearchDataEntry = StringVar()
                    SearchEntry = Entry(root1, font=('Hero',12),  textvariable=SearchDataEntry)
                    SearchEntry.place(x=x_coordinate2, y=y_coordinate2)
                    y_coordinate2 = y_coordinate2 + 40
                    Data.append(SearchEntry)
                
                Clicked = StringVar()
                MyCombo2 = ttk.Combobox(root1, textvariable=Clicked, font=('Hero',12))
                MyCombo2['values'] = ["<",">","!=","<=",">="]
                MyCombo2.current(0)
                MyCombo2.bind("<<ComboboxSelected>>")
                MyCombo2.place(x=30,y=300)
                Symbol.append(MyCombo2)    

                SearchButton1 = Button(root1, text="Use", bg="#FFFFFF", width=8, font=(
                        "Hero", 10),relief=FLAT, command=lambda: UseClick1(Fields,Data,UsedTab,Col,Symbol))
                SearchButton1.place(x=270, y=300)
                return
            
            def SearchTable2(Contents):
        
                root2 = Tk()
                root2.config(bg='#FFFFFF')
                root2.geometry('845x590+200+200')
            
                root2.title("Select the Field")
                
                query1 = "show COLUMNS from %s" % (UsedTab)
                # print(query1)
                mycursor.execute(query1)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])

                showFrame = Frame(root2, bg='black', relief=FLAT, borderwidth=3)
                showFrame.place(x=0, y=0, width=845, height=590)
                xScrollBar = Scrollbar(showFrame, orient=HORIZONTAL)
                yScrollBar = Scrollbar(showFrame, orient=VERTICAL)
                contenttable = Treeview(showFrame, columns=Col, yscrollcommand=yScrollBar.set, xscrollcommand=xScrollBar.set)

                style = ttk.Style()
                style.configure('Treeview.Heading', font=(
                                'Hero', 20), foreground='black')
                style.configure('Treeview', font=('Hero', 15),
                                bg='#7395AE', foreground='black')

                xScrollBar.pack(side=BOTTOM, fill=X)
                yScrollBar.pack(side=RIGHT, fill=Y)
                xScrollBar.config(command=contenttable.xview)
                yScrollBar.config(command=contenttable.yview)

                for i in Col:
                    contenttable.heading(i, text=i, anchor=CENTER)

                for j in Col:
                    contenttable.column(j, width=150)
                    contenttable['show'] = 'headings'
                    contenttable.pack(fill=BOTH, expand=1)

                #command = 'select * from %s' % (UsedTab)
                # mycursor.execute(command)
                #contents = mycursor.fetchall()
                #contenttable.delete(*contenttable.get_children())

                for i in Contents:
                    value = []
                    for j in range(len(Col)):
                        value.append(i[j])
                    contenttable.insert('', END, values=value)
                
                root2.mainloop()    
            
            def UseClick1(Fields, Data, UsedTab, Col, Symbol):

                #global Contents, UsedTab
                Fields2 = []
                Data2 = []
                for i in Fields:
                    j = i.get()
                    Fields2.append(j)
                for k in Data:
                    l = k.get()
                    Data2.append(l)
                # print(Data2)
                # print(Fields2)            
                
                #Label2 = Label(root1, text="Table " + UsedTab + " selected", bg="#7395AE", fg="#FFFFFF", font=(
                #    'Hero', 20, ),)

                query = "show COLUMNS from %s" % (UsedTab)
                mycursor.execute(query)
                Columns = mycursor.fetchall()
                Col = []
                for i in Columns:
                    Col.append(i[0])

                query1 = "desc %s" % (UsedTab)
                mycursor.execute(query1)
                GetData = mycursor.fetchall()
                DataTypes = []

                for i in GetData:
                    B = i[1].decode('utf-8')
                    DataTypes.append(B)
                DataTypes2 = []
                
                for l in DataTypes:
                    try:
                        C = l.index("(")
                        DataTypes2.append(l[0:C])
                    except ValueError:
                        DataTypes2.append(l)

                # print(DataTypes2)
                N = len(Data2)
                # print(Fields2)
                # print(Data2)
                
                DataQuery = ""
                Empty = 0
                for i in Data2:
                    if i == '':
                        Empty = 1
                        messagebox.showerror(
                            'Please Enter all Fields', 'Enter all the Input Fields')
                        break
                SymbolValue = Symbol[0].get()
                if Empty != 1:
                    for k in range(N):

                        A = Fields2[k]
                        for f in Col:
                            if f == A:
                                Index = Col.index(f)
                        
                                if DataTypes2[Index] == "int":
                                    try:
                                        int(k)
                                        if k == N-1:
                                            DataQuery = DataQuery + str(f) + SymbolValue + str(Data2[k])
                                        else:
                                            DataQuery = DataQuery + str(f) + SymbolValue + str(Data2[k]) + "and"
                                    except ValueError:
                                        messagebox.showerror('Invalid Field Input',
                                                                'Please enter the corresponding data type')
                                        continue
                                
                                    
                
                query = "select * from %s where %s " % (UsedTab,DataQuery)
                
                # print(query)
                mycursor.execute(query)
                Contents = mycursor.fetchall()

                #Label2.place(x=55, y=300)
                root1.destroy()
                
                SearchTable2(Contents)    
                
            
            query = "show COLUMNS from %s" % (UsedTab)
            mycursor.execute(query)
            Columns = mycursor.fetchall()
            Col = []
            for i in Columns:
                Col.append(i[0])

            ParaLabel2 = Label(root1, text="Enter the Number of fields ", bg="#557A95", fg="#FFFFFF", font=('Hero', 20, ), )
            ParaLabel2.place(x=20, y=60)

            FieldNoEntry = StringVar()
            FieldNoEntry2 = Entry(root1, width=20, font=20, textvariable=FieldNoEntry)
            FieldNoEntry2.place(x=30, y=150) 

            NoButton2 = Button(root1, text="Use", bg="#FFFFFF", width=8, font=(
                "Hero", 10), command=lambda: FieldNo2(FieldNoEntry2))
            NoButton2.place(x=80, y=110)  
            
            return       
            
        root = Tk()
        root.config(bg='#000000')
        root.geometry('500x400+200+200')
        # root.resizable(False,False)
        root.title("Table Contents")

        head = "Search"
        headLabel = Label(root, text=head, bg="#000000", font=('Hero', 30, ), fg="#eec94c")
        headLabel.place(x=15, y=9)
        
        Search1Button = Button(root, text="Search by Single Field", bg="#FFFFFF", width=26,relief= FLAT, font=("Hero",19),command=lambda:Search1(UsedTab))
        Search1Button.place(x=50, y=80)

        Search2Button = Button(root, text="Search by Multiple Fields", bg="#FFFFFF", width=26, relief=FLAT,font=("Hero",19), command=lambda:Search2(UsedTab))
        Search2Button.place(x=50, y=160)

        Search3Button = Button(root, text="Search by Comparing Values", bg="#FFFFFF", width=26, relief=FLAT, font=("Hero",19), command=lambda:Search3(UsedTab))
        Search3Button.place(x=50, y=240)
    
        root.mainloop()    
        
    #ConnectSQL()    
    ThirdWindow()
    
# def ConnectSQL():
    
#     global codb
    
#     def connmysql():
        
#         global mycursor
#         global con
        
        
#         host = hostvalue.get()
#         user = uservalue.get()
#         password = passvalue.get()
#         try:
#             con = mysql.connect(host=host, user=user, passwd=password)
#             mycursor = con.cursor()
#             mycursor.execute("create database if not exists teacher")
#             mycursor.execute("use teacher")
#             mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='teacher' AND table_name = 'Teacher'")
#             C = mycursor.fetchall()

#             if C == []:
#                 mycursor.execute("create table Teacher(Teacher_Code varchar(40), Teacher_Name varchar(40), Subject varchar(40), Phone_Number int, DOJ varchar(40), DOB varchar(40), Email varchar(30), Salary int)")
#                 mycursor.execute('alter table teacher modify column Teacher_Code int not null primary key')
                
#             else:
#                 mycursor.execute('use teacher')
            
#         except:
            
#             messagebox.showerror('Error!', 'Please Try Again')
#             return
        
#         codb.destroy()
         
           
#     ConnectSQL()       

#     codb = Tk()
#     codb.title("Enter Credentials")
#     codb.grab_set()
#     codb.resizable(False, False)
#     codb.geometry("450x450+800+230")
#     codb.config(bg="black")
#     ####MYSQL HOST STUFFS####
    
#     head = "ZESCA"
#     headLabel = Label(codb, text=head, bg="#000000", fg="#eec94c", font=(
#         'Elianto', 40, ), )
#     headLabel.place(x=26, y=20)
   
#     hostvalue = StringVar()
#     hostLabel = Label(codb, text="Enter Host: ", font=('Hero', 15 ),
#                     fg='#EEC94C',bg='#000000', relief=FLAT, width=15, anchor='n')
#     hostLabel.place(x=10, y=130)
#     hostEntry = Entry(codb, font=('Hero', 15), textvariable=hostvalue)
#     hostEntry.place(x=200, y=130)

#     ####MYSQL USER STUFFS##
#     uservalue = StringVar()
#     userLabel = Label(codb, text="Enter User: ", font=('Hero', 15),
#                     fg='#EEC94C',bg='#000000', relief=FLAT, width=15, anchor='n')
#     userLabel.place(x=10, y=190)
#     userEntry = Entry(codb, font=('Hero', 15), textvariable=uservalue)
#     userEntry.place(x=200, y=190)

#     ####MYSQL PASSWORD####
#     passvalue = StringVar()
#     passLabel = Label(codb, text="Enter Password: ", font=(
#         'Hero', 15), fg='#EEC94C',bg='#000000', relief=FLAT, width=15,anchor='n')
#     passLabel.place(x=10, y=260)
#     passEntry = Entry(codb, font=('Hero', 15),
#                         textvariable=passvalue,show = '*')
#     passEntry.place(x=200, y=260)

#     ####SUBMIT BUTTOM####
#     submitButton = Button(codb, text="Connect", font=('Hero', 15), bg='#EEC94C', relief=FLAT,
#                         width=8, activebackground='red', activeforeground='white', command=connmysql)
#     submitButton.place(x=160, y=320)
    
    
    
#     codb.mainloop()
    
#     try:
#         if con.is_connected():
# #             print('Connected to MySQL database')

#     except:
#         messagebox.showerror('No Connection','Please Connect to MySQL for further use')
#         ConnectSQL()

