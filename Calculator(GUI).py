from tkinter import *

#################################
###Making the window in Tkinter(size and title)
window=Tk()
text_Input=StringVar()
operator=""
window.resizable(0,0)
window.title("Calculator")
window.configure(background="light blue")
#################################
#functions for the buttons
entry1 = Entry(window,width=11,textvariable=text_Input,borderwidth=5,font=("arial",35,"bold")).grid(row=0,column=0,columnspan=3,padx=5,pady=5,sticky=W)

def btnClick(number):
    global operator
    operator=operator + str(number)
    text_Input.set(operator)

def button_clear():
   global operator
   operator=""
   text_Input.set("")
def Equals():
    global operator
    total=str(eval(operator))
    text_Input.set(total)
    operator=""
#################################

    
#################################
#Labels add a widget that can include text or images and also allowes you to
#################################
##Making the buttons for the numbers


button1=Button(window,text="1",bd=6,width=15,height=8,command= lambda: btnClick(1),bg="powder blue",font=("arial",10,"bold")).grid(row=1,column=0,padx=5,pady=5)
button2=Button(window,text="2",bd=6,width=15,height=8,command= lambda: btnClick(2),bg="powder blue",font=("arial",10,"bold")).grid(row=1,column=1,padx=5,pady=5)
button3=Button(window,text="3",bd=6,width=15,height=8,command= lambda: btnClick(3),bg="powder blue",font=("arial",10,"bold")).grid(row=1,column=2,padx=5,pady=5)
button4=Button(window,text="4",bd=6,width=15,height=8,command= lambda: btnClick(4),bg="powder blue",font=("arial",10,"bold")).grid(row=2,column=0,padx=5,pady=5)
button5=Button(window,text="5",bd=6,width=15,height=8,command= lambda: btnClick(5),bg="powder blue",font=("arial",10,"bold")).grid(row=2,column=1,padx=5,pady=5)
button6=Button(window,text="6",bd=6,width=15,height=8,command= lambda: btnClick(6),bg="powder blue",font=("arial",10,"bold")).grid(row=2,column=2,padx=5,pady=5)
button7=Button(window,text="7",bd=6,width=15,height=8,command= lambda: btnClick(7),bg="powder blue",font=("arial",10,"bold")).grid(row=3,column=0,padx=5,pady=5)
button8=Button(window,text="8",bd=6,width=15,height=8,command= lambda: btnClick(8),bg="powder blue",font=("arial",10,"bold")).grid(row=3,column=1,padx=5,pady=5)
button9=Button(window,text="9",bd=6,width=15,height=8,command= lambda: btnClick(9),bg="powder blue",font=("arial",10,"bold")).grid(row=3,column=2,padx=5,pady=5)
button0=Button(window,text="0",bd=6,width=15,height=8,command= lambda: btnClick(0),bg="powder blue",font=("arial",10,"bold")).grid(row=4,column=2,padx=5,pady=5)
buttonAdd=Button(window,text="+",bd=6,width=8,bg="light green",command= lambda: btnClick("+"),height=8).grid(row=1,column=3,padx=5,pady=5)
buttonSubtract=Button(window,text="-",bd=6,width=8,font=("arial",10,"bold"),bg="light green",command= lambda: btnClick("-"),height=8).grid(row=2,column=3,padx=5,pady=5)
buttonMultiply=Button(window,text="*",width=8,bd=6,font=("arial",10,"bold"),bg="light green",command= lambda: btnClick("*"),height=8).grid(row=3,column=3,padx=5,pady=5)
buttonDivide=Button(window,text="÷",width=8,bd=6,font=("arial",10,"bold"),bg="light green",command= lambda: btnClick("/"),height=8).grid(row=4,column=3,padx=5,pady=5)
buttonEqual=Button(window,text="=",width=33,bd=6,font=("arial",10,"bold"),bg="light green",height=8,command=Equals).grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky=W)
buttonClear=Button(window,text="Clear",width=20,font=("arial",10,"bold"),bg="light green",bd=4,height=8,command=button_clear).grid(row=0,column=2,columnspan=2,padx=5,pady=5,sticky=E)



#Starting the main loop
window.mainloop()

#Created by Harry Cooper
