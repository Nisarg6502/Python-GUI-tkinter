import tkinter as tk

window = tk.Tk()

#Frame 1
f1 = tk.Frame(master=window, height=40, bg="#171717", width=100)

#Frame 2
f2 = tk.Frame(master=window, height=40, bg="#271717", width=100)

#Frame 3
f3 = tk.Frame(master=window, height=40, bg="#371717", width=100)

f1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
f3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
