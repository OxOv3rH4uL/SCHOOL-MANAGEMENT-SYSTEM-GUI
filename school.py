from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import mysql.connector as mysql
import PIL.Image
from students import *
from fees import *
from library import *
from teacher import *



rootMain = Tk()
rootMain.title("SCHOOL MANAGEMENT SYSTEM")
rootMain.geometry('1174x700+200+50')
rootMain.config(bg ="#7395AE")
rootMain.resizable(False,False)

rootMain.attributes('-topmost',False)



headingFrame = Frame(rootMain, bg = "#04C4EF", relief = RIDGE,)

head = "ZESCA"
headLabel = Label(rootMain, text=head, bg="#04C4EF", fg="#FFFFFF", font=(
                'Elianto', 40, ), )
headLabel.place(x=26, y=20)                


BG = PIL.Image.open("back.jpg")
BG = BG.resize((1174,700),PIL.Image.ANTIALIAS)
BGImage = ImageTk.PhotoImage(BG)

BGImageLabel = Label(image=BGImage, bg="#5D5C61")
BGImageLabel.place(x=0, y=0)

head = "ZESCA"
headLabel = Label(rootMain, text=head, bg="#000000", fg="#FFFFFF", font=(
                'Elianto', 60, ), )
headLabel.place(x=47, y=20)   

## DATABASES BUTTON

TeacherDBButton = Button(rootMain, text="Teacher", bg="#FFFFFF", width=15,relief= FLAT, font=("Hero",19), command=teacherDB)
TeacherDBButton.place(x=47, y=385)

LibraryDBButton = Button(rootMain, text="Library", bg="#FFFFFF", width=15, relief=FLAT,font=("Hero",19), command=libraryDB)
LibraryDBButton.place(x=300, y=385)

StudentDBButton = Button(rootMain, text="Student", bg="#FFFFFF", width=15, relief=FLAT, font=("Hero",19), command=studentsDB)
StudentDBButton.place(x=47, y=450)

FeesDBButton = Button(rootMain, text="Fees", bg="#FFFFFF", width=15, relief=FLAT, font=("Hero",19), command=feesDB)
FeesDBButton.place(x=300, y=450)




rootMain.mainloop()



