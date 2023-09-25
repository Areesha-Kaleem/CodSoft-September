'''Name: Areesha Kaleem
codsoft internship Sep Batch A3'''


import tkinter as tk
from tkinter import *
import PIL.Image, PIL.ImageTk
root = tk.Tk()
tittle = root.title("Simple Calculator")
root_size = root.geometry("570x600+100+200")
colour = root.configure(bg="silver")
icon_image = PIL.Image.open("Calculator_512.webp")
root_icon = PIL.ImageTk.PhotoImage(icon_image)
root.iconphoto(True, root_icon)
result = Label(root,width=25,height=2,bg="Black",fg="White",font=("arial",30))
result.pack()

eq = ""
def show(value):
    global eq
    eq += value
    result.config(text=eq)

def clear():
    global eq
    eq = ""
    result.config(text=eq)

def calculate():
    global eq
    answer = ""
    if eq != "":
        try:
            answer = eval(eq)
        except:
            answer = "Error"
            eq =""
    result.config(text=answer)

clear_button = Button(root,text="Clear",bg="orange",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :clear()).place(x=10,y=100)
div_button = Button(root,text="/",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("/")).place(x=150,y=100)
mod_button = Button(root,text="%",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("%")).place(x=290,y=100)
mul_button = Button(root,text="*",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("*")).place(x=430,y=100)

button7 = Button(root,text="7",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("7")).place(x=10,y=200)
button8 = Button(root,text="8",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("8")).place(x=150,y=200)
button9 = Button(root,text="9",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("9")).place(x=290,y=200)
min_button = Button(root,text="-",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("-")).place(x=430,y=200)

button6 = Button(root,text="6",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("6")).place(x=10,y=300)
button5 = Button(root,text="5",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("5")).place(x=150,y=300)
button4 = Button(root,text="4",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("4")).place(x=290,y=300)
plus_button = Button(root,text="+",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("+")).place(x=430,y=300)

button3 = Button(root,text="3",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("3")).place(x=10,y=400)
button2 = Button(root,text="2",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("2")).place(x=150,y=400)
button1 = Button(root,text="1",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show("1")).place(x=290,y=400)
button0 = Button(root,text="0",bg="silver",fg="black",bd=1,width="11",height="1",font=("arial",30,"bold"),command=lambda :show("0")).place(x=10,y=500)

p_button = Button(root,text=".",bg="silver",fg="black",bd=1,width="5",height="1",font=("arial",30,"bold"),command=lambda :show(".")).place(x=290,y=500)
e_button = Button(root,text="=",bg="orange",fg="black",bd=1,width="5",height="3",font=("arial",30,"bold"),command=lambda :calculate()).place(x=430,y=400)
root.mainloop()
