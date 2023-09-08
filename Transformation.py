import tkinter as tk
from tkinter import ttk

def convert():
    km_input = entry_int.get()
    meter_output = km_input * 1000
    output_string.set(meter_output)

window = tk.Tk()
window.title('Transform')
window.geometry('250x250')

title_lable = ttk.Label(master = window , text = 'Kilometers to meters', font = 'Calibri 20 bold')
title_lable.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable= entry_int)
button = ttk.Button(master= input_frame, text = 'Convert', command=convert )
entry.pack(side = 'left')
button.pack(side = 'left')
input_frame.pack(pady=10)

output_string = tk.StringVar()
output_label = ttk.Label(master = window ,text= 'Output',textvariable= output_string)
output_label.pack(pady=10)


window.mainloop()
