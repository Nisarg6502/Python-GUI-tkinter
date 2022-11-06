import tkinter as tk

window = tk.Tk()


# Frame 1
f1 = tk.Frame(master=window, height=40, bg="#171717", width=100)
sub_f1 = tk.Frame(master=f1, bg="#171717", )
sub_f1_l1 = tk.Label(master=sub_f1, text="User Name",
                     fg="white", bg="#171717", width=15)
sub_f1_ent1 = tk.Entry(master=sub_f1, bg="#2b2f3b",
                       highlightthickness=0, width=15)

sub_f1_l1.pack()
sub_f1_ent1.pack()
sub_f1.pack(pady=10, padx=10)

sub_f2 = tk.Frame(master=f1, bg="#171717", width=70)
sub_f2_l1 = tk.Label(master=sub_f2, text="Password",
                     fg="white", bg="#171717", width=15)
sub_f2_ent1 = tk.Entry(master=sub_f2, show="*",
                       bg="#2b2f3b", highlightthickness=0, width=15)

sub_f2_l1.pack()
sub_f2_ent1.pack()
sub_f2.pack(pady=10, padx=10)

sub_f3 = tk.Frame(master=f1, bg="#171717")
sub_f3_l1 = tk.Label(master=sub_f3, text="Gender", fg="white", bg="#171717", )
sub_f3_r1 = tk.Radiobutton(master=sub_f3, text="Male", fg="white",
                           bg="#171717", highlightthickness=0, selectcolor="black", value=1)
sub_f3_r2 = tk.Radiobutton(master=sub_f3, text="Female", fg="white",
                           bg="#171717", highlightthickness=0, selectcolor="black", value=2)

sub_f3_l1.pack()
sub_f3_r1.pack(side=tk.LEFT)
sub_f3_r2.pack(side=tk.LEFT)
sub_f3.pack(pady=10, padx=10)


# Frame 2
f2 = tk.Frame(master=window, height=40, bg="#271717", width=100)

# Frame 3
f3 = tk.Frame(master=window, height=40, bg="#371717", width=100)

f1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
f3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
