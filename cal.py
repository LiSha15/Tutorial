from tkinter import*

def button_press(num):
    global eq_text
    eq_text=eq_text+str(num)
    eq_label.set(eq_text)

def equal():
    global eq_text

    try:

        total = str(eval(eq_text))

        eq_label.set(total)

        eq_text = total

    except SyntaxError:

        eq_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        eq_label.set("arithmetic error")

        eq_text = ""
    

def clear():
    global eq_text

    eq_label.set("")

    eq_text = ""


window = Tk() #create Tk object
window.title("Calculator") #Window title
window.geometry("500x500") #size of window

eq_text =  ""
eq_label = StringVar()

label = Label(window, textvariable = eq_label,font=('consolas',20),bg="light grey",borderwidth=1,relief="sunken" ,width=20,height=2)
label.pack()

frame= Frame(window)
frame.pack()

#Take label widgets
button1= Button(frame, text=1, height=4, width=9, font= 50,borderwidth=3,relief="solid", command=lambda:button_press(1))
button2 = Button(frame, text=2, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(2))
button3 = Button(frame, text=3, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(3))
button4 = Button(frame, text=4, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(4))
button5 = Button(frame, text=5, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(5))
button6 = Button(frame, text=6, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(6))
button7 = Button(frame, text=7, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(7))
button8 = Button(frame, text=8, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(8))
button9 = Button(frame, text=9, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(9))
button0 = Button(frame, text=0, height=4, width=9, font=50,borderwidth=3,relief="solid",command=lambda: button_press(0))
plus = Button(frame, text='+', height=4, width=9, font=35,bg="light pink",command=lambda: button_press('+'))
minus = Button(frame, text='-', height=4, width=9, font=35,bg="light pink",command=lambda: button_press('-'))
multiply = Button(frame, text='*', height=4, width=9, font=35,bg="light pink",command=lambda: button_press('*'))
divide = Button(frame, text='/', height=4, width=9, font=35,bg="light pink",command=lambda: button_press('/'))
equal = Button(frame, text='=', height=4, width=9, font=35,bg="light pink",command=equal)
decimal = Button(frame, text='.', height=4, width=9, font=50,bg="light pink", command=lambda: button_press('.'))
clear = Button(window, text='CLEAR', height=4, width=30, font=100,command=clear,relief="raised")
clear.pack()

#Place that labels to window
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button0.grid(row=3, column=0)
plus.grid(row=0, column=3)
minus.grid(row=1, column=3)
multiply.grid(row=2, column=3)
divide.grid(row=3, column=3)
equal.grid(row=3, column=2)
decimal.grid(row=3, column=1)

window.mainloop()


