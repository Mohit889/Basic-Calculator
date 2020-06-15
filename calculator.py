import tkinter
root = tkinter.Tk(screenName=None,  baseName=None,  className="Tk",  useTk=1)
root.title("Basic Calculator")
root.geometry("600x400")
first_number = tkinter.StringVar()
second_number = tkinter.StringVar()
fin_ans = tkinter.StringVar()
ans = None
operator = ""   #string for knowing about the opted opeartor

def set_text(num):
    current = n11.focus_displayof()

    number = str(current.get())
    number_of_digits = len(number)
    current.delete(0,number_of_digits)
    number=number +str(num)
    current.insert(number_of_digits, number)
    #n11.insert(number_of_digits,number)


def set_operator(text):
    global operator
    operator = text

def submit():
    number1=n11.get()
    number2=n22.get()
    global ans
    try:
        first = int(number1)
        second = int(number2)

        global operator
        if operator == "add":
            ans = first + second
        elif operator == "subtract":
            ans = first - second
        elif operator == "multiply":
            ans = first * second
        elif operator == "divide":
            ans = first / second
        else:
            fin_ans.set("Please select an operator")
    except:
        fin_ans.set("Please enter integers only!!")
        first_number.set("")
        second_number.set("")
        #ans= None

    total = str(ans)
    fin_ans.set(total)



n1 = tkinter.Label(root,text="Enter first number")
n2 = tkinter.Label(root,text="Enter second number")
n_ans = tkinter.Label(root,text="Answer:")
n11 = tkinter.Entry(root, textvariable=first_number)
n22 = tkinter.Entry(root, textvariable=second_number)
b1 = tkinter.Button(root,text="1",width=7,command=lambda: (set_text(1)))
b2 = tkinter.Button(root,text="2",width=7,command=lambda: (set_text(2)))
b3 = tkinter.Button(root,text="3",width=7,command=lambda: (set_text(3)))
b4 = tkinter.Button(root,text="4",width=7,command=lambda: (set_text(4)))
b5 = tkinter.Button(root,text="5",width=7,command=lambda: (set_text(5)))
b6 = tkinter.Button(root,text="6",width=7,command=lambda: (set_text(6)))
b7 = tkinter.Button(root,text="7",width=7,command=lambda: (set_text(7)))
b8 = tkinter.Button(root,text="8",width=7,command=lambda: (set_text(8)))
b9 = tkinter.Button(root,text="9",width=7,command=lambda: (set_text(9)))
b0 = tkinter.Button(root,text="0",width=7,command=lambda: (set_text(0)))
n_ans1 = tkinter.Label(root, textvariable=fin_ans)
add = tkinter.Button(root,text="+",width=10,command=lambda: (set_operator("add")))
subtract = tkinter.Button(root,text="-",width=10,command=lambda: (set_operator("subtract")))
multiply = tkinter.Button(root,text="*",width=10,command=lambda: (set_operator("multiply")))
divide = tkinter.Button(root,text="/",width=10,command=lambda: (set_operator("divide")))
s1=tkinter.Button(root,text="Submit",command=submit)
n1.grid(row=0)
n2.grid(row=1)
n11.grid(row=0,column=1)
n22.grid(row=1,column=1)
s1.grid(row=4,column=1)
add.grid(row=2,column=0)
subtract.grid(row=2,column=1)
multiply.grid(row=3,column=0)
divide.grid(row=3,column=1)
n_ans.grid(row=5,column=0)
n_ans1.grid(row=5, column=1)
b1.grid(row=6,column=0)
b2.grid(row=6,column=1)
b3.grid(row=6,column=2)
b4.grid(row=7,column=0)
b5.grid(row=7,column=1)
b6.grid(row=7,column=2)
b7.grid(row=8,column=0)
b8.grid(row=8,column=1)
b9.grid(row=8,column=2)
b0.grid(row=9,column=0)
root.mainloop()
