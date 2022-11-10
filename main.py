from cgitb import text
from doctest import master
from re import S
from textwrap import fill
import tkinter as tk
from tkinter import ANCHOR, HORIZONTAL, N, W, messagebox
from tkinter import font
from turtle import color, width
from PIL import ImageTk, Image
from click import command
from tkcalendar import Calendar

window = tk.Tk()

# functions


def Login():
    messagebox.showinfo("Form Outcome", "Logged In!")


def Submit():
    messagebox.showinfo("Data Submitted successfully. Appointment scheduled")


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
                  text="Submit", width=10, background="#197af7", bd=0, relief=tk.GROOVE, highlightthickness=0, command=Login)
login.pack()

exit_app = tk.Button(master=f1, bg="red", fg="white",
                     text="Exit", width=10, highlightthickness=0, command=close_app)
exit_app.pack(pady=10)


# Frame 2
f2 = tk.Frame(master=window, height=40, bg="#222228", width=100)

# submainframe
f2_main = tk.Frame(master=f2, bg="#2f2f37")

# left submainframe
f2_sub_left = tk.Frame(master=f2_main, width=320, bg="#2f2f37")
f2l_1 = tk.Frame(master=f2_sub_left, bg="#464652", width=320)
f2l1_label = tk.Label(master=f2l_1, fg="white",
                      text="With the online facility available, doctor consultations have become easier, and you can get the right health care. Online doctor consultations with 4000+ top medical doctors are available. Enter your details.", bg="#464652", wraplength=300)
f2l1_label.pack(padx=10, pady=10)

f2l_2 = tk.Frame(master=f2_sub_left, bg="#2f2f37")

# radio buttons
f2l2u1 = tk.Frame(master=f2l_2, bg="#2f2f37")
f2l2_label = tk.Label(master=f2l2u1, text="Gender",
                      fg="white", bg="#2f2f37")
f2l2_r1 = tk.Radiobutton(master=f2l2u1, text="Male", fg="white",
                         bg="#2f2f37", highlightthickness=0, selectcolor="black", value=1)
f2l2_r2 = tk.Radiobutton(master=f2l2u1, text="Female", fg="white",
                         bg="#2f2f37", highlightthickness=0, selectcolor="black", value=2)

f2l2_label.pack(side=tk.LEFT, anchor=N, pady=20, padx=10)
f2l2_r1.pack(side=tk.LEFT, anchor=N, pady=20, padx=10)
f2l2_r2.pack(side=tk.LEFT, anchor=N, pady=20, padx=10)

f2l2u1.pack(side=tk.TOP, anchor=W)

# slider
f2l2u2 = tk.Frame(master=f2l_2, bg="#2f2f37")
f2l2_label2 = tk.Label(master=f2l2u2, text="Age (years)",
                       fg="white", bg="#2f2f37")
w1 = tk.Scale(master=f2l2u2, from_=0, to=100, orient=HORIZONTAL,
              bg="#2f2f37", fg="white", highlightthickness=0)
w1.set(18)
f2l2_label2.pack(side=tk.LEFT, anchor=N, pady=20, padx=10)
w1.pack()
f2l2u2.pack(side=tk.TOP, anchor=W)


w2_var = tk.DoubleVar()
f2l2u3 = tk.Frame(master=f2l_2, bg="#2f2f37")
f2l2_label3 = tk.Label(master=f2l2u3, text="Weight (kg)",
                       fg="white", bg="#2f2f37")
w2 = tk.Scale(master=f2l2u3, from_=0, to=200, orient=HORIZONTAL,
              bg="#2f2f37", fg="white", highlightthickness=0, variable=w2_var)
w2.set(50)
f2l2_label3.pack(side=tk.LEFT, anchor=N, pady=20, padx=10)
w2.pack()
f2l2u3.pack(side=tk.TOP, anchor=W)

w3_var = tk.DoubleVar()
f2l2u4 = tk.Frame(master=f2l_2, bg="#2f2f37")
f2l2_label4 = tk.Label(master=f2l2u4, text="Height (cm)",
                       fg="white", bg="#2f2f37")
w3 = tk.Scale(master=f2l2u4, from_=0, to=200, orient=HORIZONTAL,
              bg="#2f2f37", fg="white", highlightthickness=0, variable=w3_var)
w3.set(150)
f2l2_label4.pack(side=tk.LEFT, anchor=N, pady=20, padx=10)
w3.pack()
f2l2u4.pack(side=tk.TOP, anchor=W)


def BMI(weight, height):
    height_m = height / 100.0
    bmi = weight / (height_m**2)
    return round(bmi, 3)


def Check_BMI(bmi):
    return f"Your BMI is {bmi}"

#command=BMI(w2_var.get(), w3_var.get()),


bmi_var = BMI(w2_var.get(), w3_var.get())

f2l2u5 = tk.Frame(master=f2l_2, bg="#2f2f37")
f2l2_label5 = tk.Label(master=f2l2u5, text=f"Body Mass Index (BMI): {Check_BMI(bmi_var)}",
                       fg="white", bg="#2f2f37")
f2l2_button1 = tk.Button(master=f2l2u5, text="Check", command=BMI(w2_var.get(), w3_var.get()),
                         bg="orange", fg="white", highlightthickness=0)
f2l2_label5.pack(side=tk.LEFT, anchor=N, pady=10, padx=10)
f2l2_button1.pack()
f2l2u5.pack(side=tk.TOP, anchor=W)


f2l_1.pack(fill=tk.X, side=tk.TOP, anchor=N)
f2l_2.pack(fill=tk.BOTH, side=tk.TOP, expand=True, anchor=N)


f2_sub_left.pack(side=tk.LEFT, fill=tk.BOTH, padx=20, pady=20, anchor=N)


# right submainframe
f2_sub_right = tk.Frame(master=f2_main, bg="#2f2f37")
f2r = tk.Frame(master=f2_sub_right, bg="#2f2f37")

f2r_1 = tk.Frame(master=f2r, bg="#2f2f37")
f2r1_l = tk.Label(master=f2r_1, text="Language for App",
                  fg="white", bg="#2f2f37")
f2r1_l.pack(padx=25, pady=10)
f2r_1.pack(side=tk.TOP, anchor=W)

f2r_2 = tk.Frame(master=f2r, bg="#2f2f37")
lang_options = ["English", "Hindi", "Marathi", "Kannada", "German"]
lang_menu = tk.StringVar()
lang_menu.set("Select Language")
drop_lang = tk.OptionMenu(f2r_2, lang_menu, *lang_options)
drop_lang.pack()
f2r_2.pack(side=tk.TOP)

f2space = tk.Frame(master=f2r, bg="#2f2f37")
f2space.pack(pady=10)

f2r_3 = tk.Frame(master=f2r, bg="#2f2f37")
f2r2_l = tk.Label(master=f2r_3, text="Doctor Type", bg="#2f2f37", fg="white")
f2r2_l.pack(padx=29, pady=10)
f2r_3.pack(side=tk.TOP, anchor=W)

f2r_4 = tk.Frame(master=f2r, bg="#2f2f37")
doc_options = ["Cardiologist", "Dermatologist",
               "Neurologist", "Ob/GYN", "Opthalmologist", "Oncologist", "Pediatrician"]
doc_menu = tk.StringVar()
doc_menu.set("Select Doctor")
drop_doc = tk.OptionMenu(f2r_4, doc_menu, *doc_options)
drop_doc.pack()
f2r_4.pack()

f2space_2 = tk.Frame(master=f2r, bg="#2f2f37")
f2space_2.pack(pady=10)

f2r_5 = tk.Frame(master=f2r, bg="#2f2f37")
# Add Calendar
cal = Calendar(f2r_5, selectmode='day',
               year=2020, month=5,
               day=22)
cal.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
get_date = tk.Button(f2r_5, text="Get Date",
                     command=grad_date).pack(pady=20)

date = tk.Label(f2r_5, text="Date: ")
date.pack(pady=20)
f2r_5.pack(side=tk.BOTTOM)

f2r_6 = tk.Frame(master=f2r, bg="#2f2f37")
Submit = tk.Button(master=f2r_6, fg="white",
                   text="Submit", width=10, background="#197af7", bd=0, relief=tk.GROOVE, highlightthickness=0, command=Submit)
Submit.pack()
f2r_6.pack(side=tk.BOTTOM)


f2r.pack(fill=tk.BOTH, pady=20)
f2_sub_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
f2_main.pack(fill=tk.BOTH, pady=20, padx=20, expand=True)

f1.pack(fill=tk.Y, side=tk.LEFT)
f2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.geometry('850x500')
window.mainloop()
