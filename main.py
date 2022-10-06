from tkinter import *


# ---------Button Click------
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


# ---------Clear Screen------
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("0")


# ---------Sum Up---------
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


# ---------Main()---------
cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

# ---------Display---------
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), fg="white", textvariable=text_Input, bd=30, insertwidth=5,
                   bg="black", justify='right').grid(columnspan=4)

# ---------Clear Button---------
btnClear = Button(cal, padx=143.5, pady=8, bd=4, fg="lightgreen", font=('arial', 16, 'bold'), text="Clear", bg="black",
                  command=btnClearDisplay).grid(row=1, column=0, columnspan=4)

# ---------Button 1st Row---------
btn7 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="7",
              command=lambda: btnClick(7), bg="white").grid(row=2, column=0)
btn8 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="8",
              command=lambda: btnClick(8), bg="white").grid(row=2, column=1)
btn9 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="9",
              command=lambda: btnClick(9), bg="white").grid(row=2, column=2)
Division = Button(cal, padx=24.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="/",
                  command=lambda: btnClick("/"), bg="lightgrey").grid(row=2, column=3)

# ---------Button 2nd Row---------
btn4 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="4",
              command=lambda: btnClick(4), bg="white").grid(row=3, column=0)
btn5 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="5",
              command=lambda: btnClick(5), bg="white").grid(row=3, column=1)
btn6 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="6",
              command=lambda: btnClick(6), bg="white").grid(row=3, column=2)
Multiply = Button(cal, padx=23, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="*",
                  command=lambda: btnClick("*"), bg="lightgrey").grid(row=3, column=3)

# ---------Button 3rd Row---------
btn1 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="1",
              command=lambda: btnClick(1), bg="white").grid(row=4, column=0)
btn2 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="2",
              command=lambda: btnClick(2), bg="white").grid(row=4, column=1)
btn3 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="3",
              command=lambda: btnClick(3), bg="white").grid(row=4, column=2)
Subtraction = Button(cal, padx=24, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="-",
                     command=lambda: btnClick("-"), bg="lightgrey").grid(row=4, column=3)

# ---------Button 4th Row---------
btn0 = Button(cal, padx=23.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="0",
              command=lambda: btnClick(0), bg="white").grid(row=5, column=0)
DOT = Button(cal, padx=25.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text=".",
             command=lambda: btnClick('.'), bg="white").grid(row=5, column=1)
btnEquals = Button(cal, padx=22.5, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="=", bg="orange",
                   command=btnEqualsInput).grid(row=5, column=2)
Addition = Button(cal, padx=21, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), text="+",
                  command=lambda: btnClick("+"), bg="lightgrey").grid(row=5, column=3)

# ---------End of Program---------
cal.mainloop()


#Code By Riyad