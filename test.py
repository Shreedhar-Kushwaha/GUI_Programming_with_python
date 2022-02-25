import math
import re
from math import gcd
from tkinter import *
root=Tk()
root.title("Shreedhar")
root.geometry('290x400')
root.wm_minsize(width=290,height=400)
root.wm_maxsize(width=290,height=400)


def next():
    root1 = Tk()
    root1.title("Next Page")
    nb1 = Button(root1, text="sin", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red',command=lambda:press("sin"))
    nb2 = Button(root1, text="cos", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red',command=lambda:press("cos"))
    nb3 = Button(root1, text="tan", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red',command=lambda:press("tan"))
    nb4 = Button(root1, text="Sqrt", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red',command=lambda:press(7))
    nb5 = Button(root1, text="(", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red',command=lambda:press("("))
    nb6 = Button(root1, text=")", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red',command=lambda:press(")"))
    nb7 = Button(root1, text="cot", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red',command=lambda:press(7))
    nb8 = Button(root1, text="Sqr", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red',command=lambda:press(7))
    #nb9 = Button(root1, text="Sqrt", font=('calibri', 14, 'bold'), borderwidth=5, activeforeground='red')


    nb1.place(x=10, y=10, width=60, height=40)
    nb2.place(x=80, y=10, width=60, height=40)
    nb3.place(x=150, y=10, width=60, height=40)
    nb4.place(x=220, y=10, width=60, height=40)
    nb5.place(x=10, y=60, width=60, height=40)
    nb6.place(x=80, y=60, width=60, height=40)
    nb7.place(x=150, y=60, width=60, height=40)
    nb8.place(x=220, y=60, width=60, height=40)
    #nb9.place(x=220, y=110, width=60, height=40)




expression=" "


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def pipress():
    global expression
    expression = expression + str(math.pi)
    equation.set(expression)

def deg():
    global expression
    expression = math.degrees(eval(expression))
    equation.set(expression)
    expression = str(expression)

def rad():
    global expression
    expression = math.radians(eval(expression))
    equation.set(expression)
    expression = str(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression =""
    except:
        equation.set("error")
        expression =" "


def log():
    global expression
    expression = math.log10(eval(expression))
    equation.set(expression)
    expression = str(expression)
    #expression = " "

def ln():
    global expression
    expression = math.log(eval(expression))
    equation.set(expression)
    expression = str(expression)
    #expression = " "


def factorial():
    global expression
    expression = math.factorial(eval(expression))
    equation.set(expression)
    expression = str(expression)
    #expression = " "


def inversepress():
    global expression
    expression = 1/eval(expression)
    equation.set(expression)
    expression = str(expression)
    #expression = " "

def percentpress():
    try:
        global expression
        a,b = [eval(e) for e in re.split('-',expression)]

        per = (a - a*b/100)
        equation.set(str(per))
        expression = " "

    except :
        equation.set("error")
        expression = " "


def lcmpress():
    try:
        global expression
        list = [eval(e) for e in expression.split(',')]
        lcm = list[0]
        for i in list[1:]:
            lcm = int(lcm * i/gcd(lcm,i))
        equation.set(str(lcm))
        expression = " "
    except:
        equation.set("error")
        expression = " "


def clear():
    global expression
    expression= " "
    equation.set(" ")

def cancel():
    global expression
    expression = expression[:-1:]
    equation.set(expression)


f=Frame(root,borderwidth=1,relief='solid',bg='#6C2DC7')
f.place(x=0,y=0,width=290,height=400)

f1=Frame(f,borderwidth=2,relief='solid')
f1.place(x=10,y=10,width=270,height=60)

f2=Frame(f,borderwidth=2,relief="solid",bg="#98AFC7")
f2.place(x=10,y=70,width=270,height=320)

v=IntVar()

equation=StringVar()

b1=Button(f2,text="C",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',bg='red',fg='white',command=clear)
b2=Button(f2,text="Clr",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=cancel)
b3=Button(f2,text="log",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=log)
b4=Button(f2,text="ln",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=ln)
b5=Button(f2,text="NXT",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',bg='#7A5DC7',fg='white',command=next)
b6=Button(f2,text="LCM",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lcmpress)
b7=Button(f2,text="Pi",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=pipress)
b8=Button(f2,text="deg",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',activebackground='#D3D3D3',highlightcolor='red',command=deg)
b9=Button(f2,text="rad",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=rad)
b10=Button(f2,text="X !",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=factorial)
b11=Button(f2,text="7",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(7))
b12=Button(f2,text="8",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(8))
b13=Button(f2,text="9",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(9))
b14=Button(f2,text="/",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press("/"))
b15=Button(f2,text="_",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press("-"))
b16=Button(f2,text="4",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(4))
b17=Button(f2,text="5",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(5))
b18=Button(f2,text="6",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(6))
b19=Button(f2,text="X",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press("*"))
b20=Button(f2,text="+",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press("+"))
b21=Button(f2,text="1",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(1))
b22=Button(f2,text="2",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(2))
b23=Button(f2,text="3",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(3))
b24=Button(f2,text="1/x",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=inversepress)
b25=Button(f2,text="=",font=('calibri',14,'bold'),bg='#228B22',fg='white',borderwidth=5,activeforeground='red',activebackground='#006400',command=equalpress)
b26=Button(f2,text=".",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press("."))
b27=Button(f2,text="0",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(0))
b28=Button(f2,text=",",font=('calibri',14,'bold'),borderwidth=5,activeforeground='red',command=lambda:press(","))



e1=Entry(f1,font=('calibri',25,'bold'),textvariable=equation)
e1.xview()
e1.place(x=0,y=0,width=266,height=60)






b1.place(x=10,y=10,width=40,height=40)
b2.place(x=60,y=10,width=40,height=40)
b3.place(x=110,y=10,width=40,height=40)
b4.place(x=160,y=10,width=40,height=40)
b5.place(x=210,y=10,width=40,height=40)
b6.place(x=10,y=60,width=40,height=40)
b7.place(x=60,y=60,width=40,height=40)
b8.place(x=110,y=60,width=40,height=40)
b9.place(x=160,y=60,width=40,height=40)
b10.place(x=210,y=60,width=40,height=40)
b11.place(x=10,y=110,width=40,height=40)
b12.place(x=60,y=110,width=40,height=40)
b13.place(x=110,y=110,width=40,height=40)
b14.place(x=160,y=110,width=40,height=40)
b15.place(x=210,y=110,width=40,height=40)
b16.place(x=10,y=160,width=40,height=40)
b17.place(x=60,y=160,width=40,height=40)
b18.place(x=110,y=160,width=40,height=40)
b19.place(x=160,y=160,width=40,height=40)
b20.place(x=210,y=160,width=40,height=40)
b21.place(x=10,y=210,width=40,height=40)
b22.place(x=60,y=210,width=40,height=40)
b23.place(x=110,y=210,width=40,height=40)
b24.place(x=160,y=210,width=40,height=40)
b25.place(x=210,y=210,width=40,height=90)
b26.place(x=10,y=260,width=40,height=40)
b27.place(x=60,y=260,width=90,height=40)
b28.place(x=160,y=260,width=40,height=40)





root.mainloop()