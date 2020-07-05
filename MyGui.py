from tkinter import*
import time 
from datetime import datetime
import csv
import RPi.GPIO as GPIO
import pandas as pd
from pandas import DataFrame


root = Tk()
root.title("ICECAP Impedance Generator")
root.minsize(1100,600)

countNum1 = 0
countNum2 = 0
countNum3 = 0
countNum4 = 0
a = 0
b = 0
c = 0
d = 0


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


GPIO.output(5, 0)
GPIO.output(6, 0)
GPIO.output(17, 0)
GPIO.output(27, 0)



def writeToLog(x):
    csv = open('CycleRunLog.csv', 'a')
    csv.write(x)
    csv.close
        
def refresh():
    sum_list.delete(0,END)
    sum_list.insert(END, "Unit Number           Total Activation Cycle        # of sealers       $$  ")
    data = pd.read_csv('CycleRunLog.csv', sep = "\t", index_col=False, names = ["Unit Name", "Start Time", "Stop Time", "Run Time", "Activation"])
    df = DataFrame(data)
    list = df["Unit Name"]
    listNumber = df["Activation"]
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    
    for i in range(0, len(newlist)):
        numbers = 0
        for j in range(0, len(df)):
            if df["Unit Name"][j] == newlist[i]:
                numbers += df["Activation"][j]
        x = "Unit" + "  " + str(newlist[i]) + "                      " + str(numbers) + "                                   " + str(int(numbers/70))
        sum_list.insert(END, x)
                

        


        


def Enter1():
    global Ulabel1, unit1
    unit1 = e1.get()
    Ulabel1 = Label(root, text = unit1)
    Ulabel1.grid(row = 0, column = 1)
    e1.destroy()
    Button1["text"] = "Start"
    Button1["command"] = Start1
    Clear1['state'] = "active"
    


def Start1():
    global startLabel1, a, start_time1
    start_time1 = datetime.now().replace(microsecond = 0)
    startTime1["text"] = "Start at: " + str(start_time1)
    Button1["text"] = "Stop"
    Button1["command"] = Stop1
    Clear1['state'] = "disabled"
    a = 1
    count1()

        

def Stop1():
    global stopLabel1, a, stop_time1, run_time1, countNum1
    stop_time1 = datetime.now().replace(microsecond = 0)
    stopTime1["text"] = "Stop at: " + str(stop_time1)
    run_time1 = stop_time1 - start_time1
    runTime1["text"] = "RUN TIME: " + str(run_time1)
    Button1["text"] = "Start"
    Button1["command"] = Start1
    Clear1['state'] = "active"
    a = 0
    writeToLog(str(unit1)+ "\t" + str(start_time1) + "\t" + str(stop_time1) + "\t" + str(run_time1) + "\t" + str(countNum1) + "\t" )
    writeToLog(" " + '\n')
    my_listbox.insert(END, unit1 + "         " + str(start_time1) + "     " + str(stop_time1) + "       " + str(run_time1) + "       " + str(countNum1))
    countNum1 = 0
    GPIO.output(5, 0)


def Clear1():
    global e1, a, countNum1
    Ulabel1.destroy()
    e1 = Entry(root, width = 10)
    e1.grid(row = 0, column = 1)
    startTime1["text"] = " "
    stopTime1["text"] = " "
    runTime1["text"] = " "
    Button1["text"] = "Enter"
    Button1["command"] = Enter1
    a = 0
    countNum1 = 0
  

def count1():
    global a, countNum1 
    if a == 1 and countNum1 < 2000:
        countNum1 = countNum1 + 1
        countLabel1["text"] = "Activations: " + str(countNum1)
        GPIO.output(5, 1)
        root.after(20000, count1)
    else:
        Stop1()
    
    
def Enter2():
    global Ulabel2, unit2
    unit2 = e2.get()
    Ulabel2 = Label(root, text = unit2)
    Ulabel2.grid(row = 1, column = 1)
    e2.destroy()
    Button2["text"] = "Start"
    Button2["command"] = Start2
    Clear2['state'] = "active"
    

def Start2():
    global startLabel2, b, start_time2
    start_time2 = datetime.now().replace(microsecond = 0)
    startTime2["text"] = "Start at: " + str(start_time2)
    Button2["text"] = "Stop"
    Button2["command"] = Stop2
    Clear2['state'] = "disabled"
    b = 1
    count2()

        

def Stop2():
    global stopLabel2, b, countNum2
    stop_time2 = datetime.now().replace(microsecond = 0)
    stopTime2["text"] = "Stop at: " + str(stop_time2)
    run_time2 = stop_time2 - start_time2
    runTime2["text"] = "RUN TIME: " + str(run_time2)
    Button2["text"] = "Start"
    Button2["command"] = Start2
    Clear2['state'] = "active"
    b = 0
    writeToLog(str(unit2)+ "\t" + str(start_time2) + "\t" + str(stop_time2) + "\t" + str(run_time2) + "\t" + str(countNum2) + "\t" )
    writeToLog(" " + '\n')
    my_listbox.insert(END, unit2 + "         " + str(start_time2) + "     " + str(stop_time2) + "       " + str(run_time2) + "       " + str(countNum2))
    countNum2 = 0
    GPIO.output(6, 0)


    

def Clear2():
    global e2, b, countNum2
    Ulabel2.destroy()
    e2 = Entry(root, width = 10)
    e2.grid(row = 1, column = 1)
    startTime2["text"] = " "
    stopTime2["text"] = " "
    runTime2["text"] = " "
    Button2["text"] = "Enter"
    Button2["command"] = Enter2
    b = 0
    countNum2 = 0
  
    
def count2():
    global b, countNum2, start
    if b == 1 and countNum2 < 2000:
        countNum2 = countNum2 + 1
        countLabel2["text"] = "Activations: " + str(countNum2)
        GPIO.output(6, 1)
        root.after(20000, count2)
    else:
        Stop2()
            


def Enter3():
    global Ulabel3, unit3
    unit3 = e3.get()
    Ulabel3 = Label(root, text = unit3)
    Ulabel3.grid(row = 2, column = 1)
    e3.destroy()
    Button3["text"] = "Start"
    Button3["command"] = Start3
    Clear3['state'] = "active"



def Start3():
    global startLabel3, c, start_time3
    start_time3 = datetime.now().replace(microsecond = 0)
    startTime3["text"] = "Start at: " + str(start_time3)
    Button3["text"] = "Stop"
    Button3["command"] = Stop3
    Clear3['state'] = "disabled"
    c = 1
    count3()

        

def Stop3():
    global stopLabel3, c, countNum3
    stop_time3 = datetime.now().replace(microsecond = 0)
    stopTime3["text"] = "Stop at: " + str(stop_time3)
    run_time3 = stop_time3 - start_time3
    runTime3["text"] = "RUN TIME: " + str(run_time3)
    Button3["text"] = "Start"
    Button3["command"] = Start3
    Clear3['state'] = "active"
    c = 0
    writeToLog(str(unit3) + "\t" + str(start_time3) + "\t" + str(stop_time3) + "\t" + str(run_time3) + "\t" + str(countNum3) + "\t" )
    writeToLog(" " + '\n')
    my_listbox.insert(END, unit3 + "         " + str(start_time3) + "     " + str(stop_time3) + "       " + str(run_time3) + "       " + str(countNum3))
    countNum3 = 0
    GPIO.output(17, 0)
    

def Clear3():
    global e3, c, countNum3
    Ulabel3.destroy()
    e3 = Entry(root, width = 10)
    e3.grid(row = 2, column = 1)
    startTime3["text"] = " "
    stopTime3["text"] = " "
    runTime3["text"] = " "
    Button3["text"] = "Enter"
    Button3["command"] = Enter3
    c = 0
    countNum3 = 0
  
    
def count3():
    global c, countNum3
    if c == 1 and countNum3 < 2000:
        countNum3 = countNum3 + 1
        countLabel3["text"] = "Activations: " + str(countNum3)
        GPIO.output(17, 1)
        root.after(20000, count3)
    else:
        Stop3()


def Enter4():
    global Ulabel4, unit4
    unit4 = e4.get()
    Ulabel4 = Label(root, text = unit4)
    Ulabel4.grid(row = 3, column = 1)
    e4.destroy()
    Button4["text"] = "Start"
    Button4["command"] = Start4
    Clear4['state'] = "active"



def Start4():
    global startLabel4, d, start_time4
    start_time4 = datetime.now().replace(microsecond = 0)
    startTime4["text"] = "Start at: " + str(start_time4)
    Button4["text"] = "Stop"
    Button4["command"] = Stop4
    Clear4['state'] = "disabled"
    d = 1
    count4()
        

def Stop4():
    global stopLabel4, d, countNum4
    stop_time4 = datetime.now().replace(microsecond = 0)
    stopTime4["text"] = "Stop at: " + str(stop_time4)
    run_time4 = stop_time4 - start_time4
    runTime4["text"] = "RUN TIME: " + str(run_time4)
    Button4["text"] = "Start"
    Button4["command"] = Start4
    Clear4['state'] = "active"
    d = 0
    writeToLog(str(unit4) + "\t" + str(start_time4) + "\t" + str(stop_time4) + "\t" + str(run_time4) + "\t" + str(countNum4)+ "\t" )
    writeToLog(" " + '\n')
    my_listbox.insert(END, unit4 + "         " + str(start_time4) + "     " + str(stop_time4) + "       " + str(run_time4) + "       " + str(countNum4))
    countNum4 = 0
    GPIO.output(27, 0)
    

def Clear4():
    global e4, d, countNum4
    Ulabel4.destroy()
    e4 = Entry(root, width = 10)
    e4.grid(row = 3, column = 1)
    startTime4["text"] = " "
    stopTime4["text"] = " "
    runTime4["text"] = " "
    Button4["text"] = "Enter"
    Button4["command"] = Enter4
    d = 0
    countNum4 = 0
  
    
def count4():
    global d, countNum4
    if d == 1 and countNum4 < 2000:
        countNum4 = countNum4 + 1
        countLabel4["text"] = "Activations: " + str(countNum4)
        root.after(20000, count4)
        GPIO.output(27, 1)
    else:
        Stop4()




Genertaor1 = Label(root, text = "Generator 1: ").grid(row = 0, column = 0)
e1 = Entry(root, width = 10)
e1.grid(row = 0, column = 1)
Button1 = Button(root, text = "Enter", padx = 10, command = Enter1, state = "active")
Button1.grid(row = 0, column = 2)
Clear1 = Button(root, text = "Clear", padx = 10, command = Clear1, state = "disabled")
Clear1.grid(row = 0, column = 3)
countLabel1 = Label(root, text = "Activations: 0", fg = "blue")
countLabel1.grid(row = 0, column = 4)
runTime1 = Label(root, text = "RUN TIME: 0", fg = "black")
runTime1.grid(row = 0, column = 5)
startTime1 = Label(root, text = "Start at: ", fg = "green")
startTime1.grid(row = 0, column = 6)
stopTime1 = Label(root, text = "Stop at: ", fg = "red")
stopTime1.grid(row = 0, column = 7)


Genertaor2 = Label(root, text = "Generator 2: ").grid(row = 1, column = 0)
e2 = Entry(root, width = 10)
e2.grid(row = 1, column = 1)
Button2 = Button(root, text = "Enter", padx = 10, command = Enter2, state = "active")
Button2.grid(row = 1, column = 2)
Clear2 = Button(root, text = "Clear", padx = 10, command = Clear2, state = "disabled")
Clear2.grid(row = 1, column = 3)
countLabel2 = Label(root, text = "Activations: 0", fg = "blue")
countLabel2.grid(row = 1, column = 4)
runTime2 = Label(root, text = "RUN TIME: 0", fg = "black")
runTime2.grid(row = 1, column = 5)
startTime2 = Label(root, text = "Start at: ", fg = "green")
startTime2.grid(row = 1, column = 6)
stopTime2 = Label(root, text = "Stop at: ", fg = "red")
stopTime2.grid(row = 1, column = 7)



Genertaor3 = Label(root, text = "Generator 3: ").grid(row = 2, column = 0)
e3 = Entry(root, width = 10)
e3.grid(row = 2, column = 1)
Button3 = Button(root, text = "Enter", padx = 10, command = Enter3, state = "active")
Button3.grid(row = 2, column = 2)
Clear3 = Button(root, text = "Clear", padx = 10, command = Clear3, state = "disabled")
Clear3.grid(row = 2, column = 3)
countLabel3 = Label(root, text = "Activations: 0", fg = "blue")
countLabel3.grid(row = 2, column = 4)
runTime3 = Label(root, text = "RUN TIME: 0", fg = "black")
runTime3.grid(row = 2, column = 5)
startTime3 = Label(root, text = "Start at: ", fg = "green")
startTime3.grid(row = 2, column = 6)
stopTime3 = Label(root, text = "Stop at: ", fg = "red")
stopTime3.grid(row = 2, column = 7)



Genertaor4 = Label(root, text = "Generator 4: ").grid(row = 3, column = 0)
e4 = Entry(root, width = 10)
e4.grid(row = 3, column = 1)
Button4 = Button(root, text = "Enter", padx = 10, command = Enter4, state = "active")
Button4.grid(row = 3, column = 2)
Clear4 = Button(root, text = "Clear", padx = 10, command = Clear4, state = "disabled")
Clear4.grid(row = 3, column = 3)
countLabel4 = Label(root, text = "Activations: 0", fg = "blue")
countLabel4.grid(row = 3, column = 4)
runTime4 = Label(root, text = "RUN TIME: 0", fg = "black")
runTime4.grid(row = 3, column = 5)
startTime4 = Label(root, text = "Start at: ", fg = "green")
startTime4.grid(row = 3, column = 6)
stopTime4 = Label(root, text = "Stop at: ", fg = "red")
stopTime4.grid(row = 3, column = 7)

my_listbox = Listbox(root, width = 70, height = 25)
my_listbox.place(x = 0, y = 160)
my_listbox.insert(END, "Unit Number" + "            " + "Start Time" + "               " + "Stop Time" + "                     " + "Run time" + "         " + "Activation")

sum_list = Listbox(root, width = 48, height = 10)
sum_list.place(x = 650, y = 160)
sum_list.insert(END, "Unit Number           Total Activation Cycle        # of sealers       $$  ")

refreshButton = Button(root, text = "Refresh", padx = 10, command = refresh, state = "active")
refreshButton.grid(row = 4, column = 15)

root.mainloop()






