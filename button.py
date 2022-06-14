from cgitb import text
import tkinter as tk
import tkinter.ttk as ttk
from typing import Literal

def btn_click():
    print("test")

def insert_frequency(frequency_output_Hz):
    text_box_Hz.delete(0, tk.END)
    text_box_Hz.insert(tk.END,frequency_output_Hz)
    frequency_output = format(frequency_output_Hz / 10**3)
    text_box_KHz.delete(0, tk.END)
    text_box_KHz.insert(tk.END,frequency_output)
    frequency_output = format(frequency_output_Hz / 10**6)
    text_box_MHz.delete(0, tk.END)
    text_box_MHz.insert(tk.END,frequency_output)
    frequency_output = format(frequency_output_Hz / (10**9))
    text_box_GHz.delete(0, tk.END)
    text_box_GHz.insert(tk.END,frequency_output)
    frequency_output = format(frequency_output_Hz / 10**12)
    text_box_THz.delete(0, tk.END)
    text_box_THz.insert(tk.END,frequency_output)

def insert_period(period_output_s):
    text_box_s.delete(0, tk.END)
    text_box_s.insert(tk.END,period_output_s)
    period_output_ms = format(period_output_s * 10**3)
    text_box_ms.delete(0, tk.END)
    text_box_ms.insert(tk.END,period_output_ms)
    period_output_us = format(period_output_s * 10**6)
    text_box_us.delete(0, tk.END)
    text_box_us.insert(tk.END,period_output_us)
    period_output_ns = format(period_output_s * (10**9))
    text_box_ns.delete(0, tk.END)
    text_box_ns.insert(tk.END,period_output_ns)
    period_output_ps = format(period_output_s * 10**12)
    text_box_ps.delete(0, tk.END)
    text_box_ps.insert(tk.END,period_output_ps)

def period_to_frequency():
    selected_period = period_select.get()
    period_input = float(text_box_period.get())
    frequency_output = 1 / period_input
    if selected_period == "s":
        insert_frequency(frequency_output)
    elif selected_period == "ms":
        frequency_output = frequency_output * (10**3)
        insert_frequency(frequency_output) 
    elif selected_period == "us":
        frequency_output = frequency_output * (10**6)
        insert_frequency(frequency_output) 
    elif selected_period == "ns":
        frequency_output = frequency_output * (10**9)
        insert_frequency(frequency_output) 
    elif selected_period == "ps":
        frequency_output = frequency_output * (10**12)
        insert_frequency(frequency_output) 

def frequency_to_period():
    #入力した値の取得
    selected_frequency = frequency_select.get()
    frequency_input = float(text_box_frequency.get())
    period_output = 1 / frequency_input
    if selected_frequency == "Hz":
        insert_period(period_output)
    elif selected_frequency == "KHz":
        period_output = period_output / (10**3)
        insert_period(period_output) 
    elif selected_frequency == "MHz":
        period_output = period_output / (10**6)
        insert_period(period_output) 
    elif selected_frequency == "GHz":
        period_output = period_output / (10**9)
        insert_period(period_output) 
    elif selected_frequency == "THz":
        period_output = period_output / (10**12)
        insert_period(period_output)

#エンターキー入力でボタン押したい
def press_enter():
    period_to_frequency()
    frequency_to_period()


root = tk.Tk()
root.geometry("480x360")
root.title("周期周波数変換")

frame = tk.Frame(root,width=480,heigh=360,padx=10,pady=10)
frame.pack()

root.bind("<Return>", lambda event: press_enter())

input_y = 30
label_period = tk.Label(frame, text = "周期")
label_period.place(x=10,y=input_y)
text_box_period = tk.Entry(frame, width=10)
text_box_period.place(x =50,y=input_y)
lebel_frequency = tk.Label(frame, text = "周波数")
lebel_frequency.place(x=250,y= input_y)
text_box_frequency = tk.Entry(frame, width=10)
text_box_frequency.place(x =300,y=input_y)

"""
#radio button
var = tk.IntVar()
rdo_s = tk.Radiobutton(frame,value = 0,variable = var, text= "s")
rdo_s.place(x=150, y=30)
rdo_ms = tk.Radiobutton(frame,value = 1,variable = var,text= "ms")
rdo_ms.place(x=150, y=50)
rdo_us = tk.Radiobutton(frame,value = 2,variable = var,text= "us")
rdo_us.place(x=150, y=70)
rdo_ns = tk.Radiobutton(frame,value = 3,variable = var,text= "ns")
rdo_ns.place(x=150, y=90)
rdo_ps = tk.Radiobutton(frame,value = 4,variable = var,text= "ps")
rdo_ps.place(x=150, y=110)

"""
module_period =("s","ms","us","ns","ps",)
period_select = ttk.Combobox(frame, height=5, width = 4, values=module_period)
period_select.place(x=150,y=30)
module_frequency = ("Hz","KHz","MHz","GHz","THz",)
frequency_select = ttk.Combobox(frame, height=5, width = 4, values=module_frequency)
frequency_select.place(x=400,y=30)

button_y = 70
button_period = tk.Button(frame, text = "周期⇒周波数",width=10, height=1, command=period_to_frequency)
button_period.place(x = 50, y = button_y)
button_frequency = tk.Button(frame, text = "周波数⇒周期",width=10, height=1, command=frequency_to_period)
button_frequency.place(x = 300, y = button_y)

#result
result_frequency_label_x = 120
Hz_y = 150
KHz_y = 180
MHz_y = 210
GHz_y = 240
THz_y = 270
text_box_Hz = tk.Entry(frame, width=10)
text_box_Hz.place(x =50,y=Hz_y)
label_Hz = tk.Label(frame, text = "Hz")
label_Hz.place(x= result_frequency_label_x,y=Hz_y)
text_box_KHz = tk.Entry(frame, width=10)
text_box_KHz.place(x =50,y=KHz_y)
label_KHz = tk.Label(frame, text = "KHz")
label_KHz.place(x= result_frequency_label_x,y=KHz_y)
text_box_MHz = tk.Entry(frame, width=10)
text_box_MHz.place(x =50,y=MHz_y)
label_MHz = tk.Label(frame, text = "MHz")
label_MHz.place(x= result_frequency_label_x,y=MHz_y)
text_box_GHz = tk.Entry(frame, width=10)
text_box_GHz.place(x =50,y=GHz_y)
label_GHz = tk.Label(frame, text = "GHz")
label_GHz.place(x= result_frequency_label_x,y=GHz_y)
text_box_THz = tk.Entry(frame, width=10)
text_box_THz.place(x =50,y=THz_y)
label_THz = tk.Label(frame, text = "THz")
label_THz.place(x= result_frequency_label_x,y=THz_y)

result_period_label_x = 370
text_box_s = tk.Entry(frame, width=10)
text_box_s.place(x =300,y=Hz_y)
label_s = tk.Label(frame, text = "s")
label_s.place(x= result_period_label_x,y=Hz_y)
text_box_ms = tk.Entry(frame, width=10)
text_box_ms.place(x =300,y=KHz_y)
label_ms = tk.Label(frame, text = "ms")
label_ms.place(x= result_period_label_x,y=KHz_y)
text_box_us = tk.Entry(frame, width=10)
text_box_us.place(x =300,y=MHz_y)
label_us = tk.Label(frame, text = "us")
label_us.place(x= result_period_label_x,y=MHz_y)
text_box_ns = tk.Entry(frame, width=10)
text_box_ns.place(x =300,y=GHz_y)
label_ns = tk.Label(frame, text = "ns")
label_ns.place(x= result_period_label_x,y=GHz_y)
text_box_ps = tk.Entry(frame, width=10)
text_box_ps.place(x =300,y=THz_y)
label_ps = tk.Label(frame, text = "ps")
label_ps.place(x= result_period_label_x,y=THz_y)



root.mainloop()
