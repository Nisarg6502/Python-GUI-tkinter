import tkinter as tk
from tkinter import messagebox
from turtle import width
from PIL import ImageTk, Image

window = tk.Tk()

# functions


def submit():
    messagebox.showinfo("Form Outcome", "Logged In!")


def close_app():
    window.quit()


# heading image
image1 = Image.open("./Images/health.png")
resize_image1 = image1.resize((100, 30))
render = ImageTk.PhotoImage(resize_image1)

# packing image in a label
img = tk.Label(image=render)
img.image = render
img.pack()

# Frame 1
f1 = tk.Frame(master=window, height=40, bg="#2f2f37", width=100)

l1_f1 = tk.Label(master=f1, bg="#2f2f37", fg="white",
                 text="Tkinter GUI", font=('Arial 25 bold'))
l1_f1.pack(padx=10, pady=25)

# subframe f1.1
sub_f1 = tk.Frame(master=f1, bg="#2f2f37", )
sub_f1_l1 = tk.Label(master=sub_f1, text="User Name",
                     fg="white", bg="#2f2f37", width=15, anchor='w')
sub_f1_ent1 = tk.Entry(master=sub_f1, bg="#2b2f3b", fg="white",
                       highlightthickness=0, width=15)

sub_f1_l1.pack(pady=5)
sub_f1_ent1.pack()

# subframe f1.2
sub_f2 = tk.Frame(master=sub_f1, bg="#2f2f37", width=70)
sub_f2_l1 = tk.Label(master=sub_f2, text="Password",
                     fg="white", bg="#2f2f37", width=15, anchor='w')
sub_f2_ent1 = tk.Entry(master=sub_f2, show="*", fg="white",
                       bg="#2b2f3b", highlightthickness=0, width=15)

sub_f2_l1.pack(pady=5)
sub_f2_ent1.pack()
sub_f2.pack(pady=20)

sub_f1.pack(pady=70)

# subframe f1.3
login = tk.Button(master=f1, fg="white",
                  text="Submit", width=10, background="#197af7", bd=0, relief=tk.GROOVE, highlightthickness=0, command=submit)
login.pack()

exit_app = tk.Button(master=f1, bg="red", fg="white",
                     text="Exit", width=10, highlightthickness=0, command=close_app)
exit_app.pack(pady=10)

# # subframe f3
# sub_f3 = tk.Frame(master=f1, bg="#2f2f37")
# sub_f3_l1 = tk.Label(master=sub_f3, text="Gender", fg="white", bg="#2f2f37")
# sub_f3_r1 = tk.Radiobutton(master=sub_f3, text="Male", fg="white",
#                            bg="#2f2f37", highlightthickness=0, selectcolor="black", value=1)
# sub_f3_r2 = tk.Radiobutton(master=sub_f3, text="Female", fg="white",
#                            bg="#2f2f37", highlightthickness=0, selectcolor="black", value=2)

# sub_f3_l1.pack()
# sub_f3_r1.pack(side=tk.LEFT)
# sub_f3_r2.pack(side=tk.LEFT)
# sub_f3.pack(pady=10, padx=10)


# Frame 2
f2 = tk.Frame(master=window, height=40, bg="#222228", width=100)

# Frame 3
f3 = tk.Frame(master=window, height=40, bg="#222228", width=100)

f1.pack(fill=tk.Y, side=tk.LEFT)
f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
f3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.geometry('800x500')

window.mainloop()
