from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()
window.geometry("500x500")
window.title("welcome")

fn=StringVar()
ln=StringVar()
DOB=StringVar()
var=StringVar()
varc1lang=StringVar()
varc2lang=StringVar()
varr1gender=StringVar()
varr2gender=StringVar()

def exit1():
    exit()

def bamble():
    messagebox.showinfo("bam","bamble bam bam")

def printword():
    fname=fn.get()
    lname=ln.get()
    dob=DOB.get()
    varcountry=var.get()
    varlang1= varc1lang.get()
    varlang2 = varc2lang.get()
    vargender=varr1gender.get()
    print(f"name is {fname} {lname}\nDOB is {dob}\ncountry is {varcountry}\nlanguage is {varlang1} {varlang2}\ngender is {vargender}")
    messagebox.showinfo("Success","Successfully logged in")

def window2():
    window2=Tk()
    window2.title="new window bam"
    window2.geometry("350x350")

    def exit2():
        window2.destroy()

    labelw21=Label(window2,text="registration successful",font=("arial",20,"bold"),relief="solid").pack()
    buttonw21=Button(window2,text="exit",font=("arial",16),relief="raised",bg="#663300",fg="white",command=exit2).place(x=250,y=300)

def database():
    fname1=fn.get()
    lname1=ln.get()
    dob1=DOB.get()
    country1=var.get()
    lang1=varc1lang.get()
    lang2 = varc2lang.get()
    gender1=varr1gender.get()

    conn=sqlite3.connect("Form.db")
    with conn:
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Student (name Text,last Text,DOB Text,Country Text,Language Text,Gender Text)')
        cursor.execute('INSERT INTO Student(name,last,DOB,country,language,gender) VALUES(?,?,?,?,?,?)',(fname1,lname1,dob1,country1,lang1,gender1))
        conn.commit()



list=['Nepal','India','USA','England']
droplist=OptionMenu(window,var,*list)
droplist.config(width=30)
droplist.place(x=150,y=235)
var.set("select country")

label1=Label(window,text="form",font=("arial",36,"bold"),bg="#b3d9ff",relief="solid").pack(fill=BOTH,pady=2,padx=2)
button1=Button(window,text="sign up",font=("arial",16),relief="raised",bg="#663300",fg="white",command=database).place(x=60,y=440)
window.bind("<Return>",database)
button2=Button(window,text="quit",font=("arial",16),relief="raised",bg="#663300",fg="white",command=exit1).place(x=180,y=440)
labelfname=Label(window,text="first name",font=("arial",16)).place(x=20,y=80)
entryfname=Entry(window,textvar=fn).place(x=150,y=85)
labellname=Label(window,text="last name",font=("arial",16)).place(x=20,y=130)
entrylname=Entry(window,textvar=ln).place(x=150,y=135)
labelDOB=Label(window,text="DOB",font=("arial",16)).place(x=20,y=180)
entryDOB=Entry(window,textvar=DOB).place(x=150,y=185)
labelcountry=Label(window,text="country",font=("arial",16)).place(x=20,y=230)
labellang=Label(window,text="language",font=("arial",16)).place(x=20,y=280)
c1lang=Checkbutton(window,text="English",variable=varc1lang,onvalue="English" ,offvalue="").place(x=150,y=280)
c1lang=Checkbutton(window,text="Hindi",variable=varc2lang,onvalue="Hindi" ,offvalue="").place(x=250,y=280)
labelgender=Label(window,text="gender",font=("arial",16)).place(x=20,y=330)
r1=Radiobutton(window,text="Male",variable=varr1gender,value="Male").place(x=150,y=330)
r1=Radiobutton(window,text="Female",variable=varr1gender,value="Female").place(x=250,y=330)
button3=Button(window,text="login",font=("arial",16),relief="raised",bg="#663300",fg="white",command=window2).place(x=400,y=440)

menu=Menu(window)
window.config(menu=menu)

submenu1=Menu(menu)
menu.add_cascade(label="options",menu=submenu1)
submenu1.add_command(label="exit",command=exit1)

submenu2=Menu(menu)
subsubmenu1=Menu(submenu1)
menu.add_cascade(label="file",menu=submenu2)
submenu2.add_cascade(label="bam",menu=subsubmenu1)
subsubmenu1.add_command(label="bamble",command=bamble)

window.mainloop()