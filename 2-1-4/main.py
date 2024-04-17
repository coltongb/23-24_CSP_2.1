#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    print("I got here!")
    if(ent_username.get() == "username" and ent_password.get() == "pass"):
        frame_auth.tkrais()
    else:
        fail_label = tk.Label(frame_login, text="wrong")
        fail_label.pack()

# main window
root = tk.Tk()
root.wm_geometry("500x200")


# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0)
frame_auth = tk.Frame(root)
frame_auth.grid()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
ent_username.pack(padx=200)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)
ent_password.pack(padx=200)

btn_login = tk.Button(frame_login, text='Login')
btn_login.pack()

root.mainloop()