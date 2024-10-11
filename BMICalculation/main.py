from tkinter import *

def calculate():
    w = weight.get()
    h = height.get()
    BMI = float(w) / (float(h)/100)**2



    if (0.0<BMI):
        if(BMI<=18.5):
            resultlabel.config(text="Underweight")
        elif(BMI<=25.0):
            resultlabel.config(text="Normal")
        elif(BMI<=30.0):
           resultlabel.config(text="Overweight")
        else:
            resultlabel.config(text="Obese")
    else:
        resultlabel.config(text="Enter valid numbers")


window = Tk()
window.title("BMI Calculation")
window.minsize(width=350,height=300)

label1=Label(text="Enter your height (cm)",font=('Arial',10,"bold"))
label1.place(x=120,y=10)


height= Entry(width=20)
height.place(x=120,y=45)
height.focus()

label2=Label(text="Enter your weight (kg) ",font=('Arial',10,"bold"))
label2.place(x=120,y=95)

weight=Entry(width=20)
weight.place(x=120,y=125)

button= Button(text="Calculate",command=calculate)
button.place(x=150,y=165)


resultlabel= Label(font=('Arial',12,"bold"))
resultlabel.place(x=85,y=195)

window.mainloop()
