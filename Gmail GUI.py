from tkinter import *
from tkinter import scrolledtext,messagebox
import tkinter.font
import smtplib


def sendemail(mailto, msg):

    try:
        # Enter your Email Id in the Single Quotes below
        gmailaddress = ''
        # Enter the Email Id Password in the Single Quotes below
        gmailpassword = ''
        
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, mailto , msg)
        messagebox.showinfo("Email Status", "Mail Sent!")
        mailServer.quit()
        
    except:
        messagebox.showinfo("Email Status", "Unable to send Mail")
        

def clear(txt1, txt2):
    txt1.delete(0, END)
    txt2.delete(1.0, END)



win=Tk()

win.configure(background='#4DD2FF')
win.title("sentiment analysis")
win.geometry('720x580+400+80')

FontOfEntryList=tkinter.font.Font(family="TimesNewRoman",size=20)

lblname=Label(win,text="Sending Email using Python",anchor="center",font=("new roman",35,'bold'),bg='#4DD2FF')
lblname.place(x=40,y=10)

lblemail=Label(win,text="TO :- ",anchor="center",font=("new roman",20),bg='#4DD2FF')
lblemail.place(x=90,y=150)

txt1=Entry(win,font=FontOfEntryList,width=31)
txt1.place(x=160,y=150)


lblmsg=Label(win,text="What is your message?",anchor="center",font=("new roman",20),bg='#4DD2FF')
lblmsg.place(x=90,y=240)

txt2=scrolledtext.ScrolledText(win,font=FontOfEntryList,width='35',height='5')
txt2.place(x=90,y=290)

btnsend=Button(win,text="Send",font=("aerial",16,'bold'),command = lambda: sendemail(txt1.get(), txt2.get('1.0', 'end-1c')))
btnsend.place(x=240,y=500)

btnclr=Button(win,text="Clear",font=("aerial",16,'bold'),command = lambda: clear(txt1, txt2))
btnclr.place(x=440,y=500)


