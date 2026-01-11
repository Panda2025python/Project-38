import tkinter as tk
from datetime import date
def calculate_age():
    try:
        y = int(year_entry.get())
        m = int(month_entry.get())
        d = int(day_entry.get())
        today = date.today()
        age = today.year - y - ((today.month, today.day) < (m, d))
        result_label.config(text=str(age))
    except:
        result_label.config(text="Invalid")
root = tk.Tk()
root.title("Age Calculator")
tk.Label(root, text="Year").grid(row=0, column=0)
tk.Label(root, text="Month").grid(row=1, column=0)
tk.Label(root, text="Day").grid(row=2, column=0)
year_entry = tk.Entry(root)
month_entry = tk.Entry(root)
day_entry = tk.Entry(root)
year_entry.grid(row=0, column=1)
month_entry.grid(row=1, column=1)
day_entry.grid(row=2, column=1)
tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=3, column=0, columnspan=2)
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)
root.mainloop()
