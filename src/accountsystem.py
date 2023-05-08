from email.mime.text import MIMEText
import smtplib
import sqlite3
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from userHome3 import *


#from buttonWindow import App

AccountSystem = Tk()
AccountSystem.rowconfigure(0, weight=1)
AccountSystem.columnconfigure(0, weight=1)
height = 650
width = 1240
x = (AccountSystem.winfo_screenwidth() // 2) - (width // 2)
y = (AccountSystem.winfo_screenheight() // 4) - (height // 4)
AccountSystem.geometry('{}x{}+{}+{}'.format(width, height, x, y))
AccountSystem.state('zoomed')
AccountSystem.configure(bg="#525561")

AccountSystem.title("MovieMatch")

sign_in = Frame(AccountSystem)
sign_up = Frame(AccountSystem)
genre_choise = Frame(AccountSystem)

for frame in (sign_in, sign_up, genre_choise):
    frame.grid(row=0, column=0, sticky="nsew")


def show_frame(frame):
    frame.tkraise()

# ============Login page==============
# ++++++++++++++++++++++++++++++++++++++++


email = StringVar()
password = StringVar()

# UpdateProfile

EmailStorage = email

# UpdateProfile

sign_in.configure(bg="#525561")

# ================Background Image ====================
Login_backgroundImage = PhotoImage(
    file="image_1.png")
bg_imageLogin = Label(
    sign_in,
    image=Login_backgroundImage,
    bg="#525561"
)
bg_imageLogin.place(x=200, y=70)

# ================ Header Text Left ====================
# Login_headerText_image_left = PhotoImage(
#     file=" headerText_image.png")
Login_headerText_image_left = PhotoImage(
    file="LogoImage3.png")
# E:\Python_Project_Ayush\Final Login and sign up page\Python Tkinter Modern GUI login and sign up form\assets
Login_headerText_image_label1 = Label(
    bg_imageLogin,
    image=Login_headerText_image_left,
    bg="#272A37"
)
Login_headerText_image_label1.place(x=60, y=45)

Login_headerText1 = Label(
    bg_imageLogin,
    text="MovieMatch",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 26 * -1),
    bg="#272A37"
)
Login_headerText1.place(x=150, y=45)


# ================ LOGIN TO ACCOUNT HEADER ====================
loginAccount_header = Label(
    bg_imageLogin,
    text="Login to continue",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
loginAccount_header.place(x=75, y=121)

# ================ NOT A MEMBER TEXT ====================
loginText = Label(
    bg_imageLogin,
    text="Not a member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#272A37"
)
loginText.place(x=75, y=187)

# ================ GO TO SIGN UP ====================
switchSignup = Button(
    bg_imageLogin,
    text="Sign Up",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda: show_frame(sign_up)
)
switchSignup.place(x=220, y=183, width=70, height=35)


# ================ Email Name Section ====================
Login_emailName_image = PhotoImage(
    file="email.png")
Login_emailName_image_Label = Label(
    bg_imageLogin,
    image=Login_emailName_image,
    bg="#272A37"
)
Login_emailName_image_Label.place(x=76, y=242)

Login_emailName_text = Label(
    Login_emailName_image_Label,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_emailName_text.place(x=25, y=0)

Login_emailName_icon = PhotoImage(
    file="email-icon.png")
Login_emailName_icon_Label = Label(
    Login_emailName_image_Label,
    image=Login_emailName_icon,
    bg="#3D404B"
)
Login_emailName_icon_Label.place(x=370, y=15)

Login_emailName_entry = Entry(
    Login_emailName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=email
)
Login_emailName_entry.place(x=8, y=17, width=354, height=27)


# ================ Password Name Section ====================
Login_passwordName_image = PhotoImage(
    file="email.png")
Login_passwordName_image_Label = Label(
    bg_imageLogin,
    image=Login_passwordName_image,
    bg="#272A37"
)
Login_passwordName_image_Label.place(x=80, y=330)

Login_passwordName_text = Label(
    Login_passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_passwordName_text.place(x=25, y=0)

Login_passwordName_icon = PhotoImage(
    file="pass-icon.png")
Login_passwordName_icon_Label = Label(
    Login_passwordName_image_Label,
    image=Login_passwordName_icon,
    bg="#3D404B"
)
Login_passwordName_icon_Label.place(x=370, y=15)

Login_passwordName_entry = Entry(
    Login_passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    fg="#FFFFFF",
    show="*",
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=password
)
Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

# ================hide and see password=============
show_image = ImageTk.PhotoImage(
    file="show.png")

hide_image = ImageTk.PhotoImage(
    file="hide.png")
show_button = Button(bg_imageLogin, image=show_image, relief=FLAT,
                     activebackground="white", borderwidth=0, command=lambda: show(), background="#808080", cursor="hand2")
show_button.place(x=510, y=350)


def show():
    if Login_passwordName_entry.cget('show') == "":
        Login_passwordName_entry.config(show='*')
        show_button.config(image=show_image)
    else:
        Login_passwordName_entry.config(show='')
        show_button.config(image=hide_image)


# =============== Submit Button ====================
Login_button_image_1 = PhotoImage(
    file="button_1.png")
Login_button_1 = Button(
    bg_imageLogin,
    image=Login_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login(),
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
)
Login_button_1.place(x=120, y=445, width=333, height=65)

# ++++++++clear login fields+++++++


def clear_login():
    email.set("")
    password.set("")


# ++++++++Database connection++++
# global otpex
# #otpex = str(num)
# otpex = "11111"


def login():
    conn = sqlite3.connect("AccountSystem1.db")
    cursor = conn.cursor()
    (Login_emailName_entry.get())
    find_user = 'SELECT * FROM AccountDB WHERE EMAIL = ? and Password = ?'
    cursor.execute(
        find_user, [(Login_emailName_entry.get()), (Login_passwordName_entry.get())])
    result = cursor.fetchall()
    (result)
    (type(result))
    if result:
        
        email=Login_emailName_entry.get()
        clear_login()
        AccountSystem.destroy()
        messagebox.showinfo("Success", "Logged in Successfully")
        # calling_userHome2()
        App = QApplication(sys.argv)
        w = mainWindow(str(email))
        sys.exit(App.exec_())
        
        
    else:
        messagebox.showinfo("Failed", "Sorry can't login, please try again")


def calling_userHome2():
    pass


# ================ Forgot Password ====================
forgotPassword = Button(
    bg_imageLogin,
    text="Forgot Password?",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    activebackground="#272A37",
    activeforeground="#ffffff",
    cursor="hand2",
    command=lambda: forgot_password(),
)
forgotPassword.place(x=210, y=400, width=150, height=35)


def forgot_password():

    win = Toplevel()
    window_width = 350
    window_height = 720
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(
        f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Forgot Password')
    win.configure(background='#272A37')
    win.resizable(False, False)

    # ====== Email ====================
    global email_entry3
    email_entry3 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                         bd=0)
    email_entry3.place(x=40, y=80, width=256, height=50)
    email_entry3.config(highlightbackground="#3D404B",
                        highlightcolor="#206DB4")
    email_label3 = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                         font=("yu gothic ui", 11, 'bold'))
    email_label3.place(x=40, y=50)

    global email_entry
    email_verify = StringVar()

    update_pass = Button(win, fg='#f8f8f8', text='Submit', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, command=lambda: change_password(), activebackground="#1D90F5")
    update_pass.place(x=40, y=150, width=256, height=45)

    def exit_win():
        win.destroy()

    def change_password():
        if email_entry3.get() == "":
            messagebox.showerror("Error", "All fileds are required")
            exit_win()
        else:
            conn = sqlite3.connect("AccountSystem1.db")
            cursor = conn.cursor()
            query = 'SELECT * FROM AccountDB WHERE Email = ?'
            cursor.execute(query, [(email_entry3.get())])
            row = cursor.fetchone()

            if row == None:
                messagebox.showinfo("Error", "Email does not exist!")
                exit_win()
            else:
                otp(email_entry3.get())
                gui_rp()

    def gui_rp():  # password resetting continued....
        global new_password_entry
        global email1
        email1 = email_verify.get()
        new_password_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='*', highlightthickness=1,
                                   bd=0)
        new_password_entry.place(x=40, y=250, width=256, height=50)
        new_password_entry.config(
            highlightbackground="#3D404B", highlightcolor="#206DB4")
        new_password_label = Label(win, text='• New Password', fg="#FFFFFF", bg='#272A37',
                                   font=("yu gothic ui", 11, 'bold'))
        new_password_label.place(x=40, y=220)

        global con_new_password_entry
        global p1_verify
        global p1_entry
        global otp_verify
        global otp_entry

        con_new_password_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='*', highlightthickness=1,
                                       bd=0)
        con_new_password_entry.place(x=40, y=350, width=256, height=50)
        con_new_password_entry.config(
            highlightbackground="#3D404B", highlightcolor="#206DB4")
        con_new_password_label = Label(win, text='• Confirm New Password', fg="#FFFFFF", bg='#272A37',
                                       font=("yu gothic ui", 11, 'bold'))
        con_new_password_label.place(x=40, y=320)

        otp_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='*', highlightthickness=1,
                          bd=0)
        otp_entry.place(x=40, y=450, width=256, height=50)
        otp_entry.config(
            highlightbackground="#3D404B", highlightcolor="#206DB4")
        otp_label = Label(win, text='• Enter OTP', fg="#FFFFFF", bg='#272A37',
                          font=("yu gothic ui", 11, 'bold'))
        otp_label.place(x=40, y=420)

        otp_set = Button(win, fg='#f8f8f8', text='Set', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, command=lambda: gui_rp2(), activebackground="#1D90F5")
        otp_set.place(x=40, y=520, width=256, height=45)
        global output_label
        output_label = Label(win, text='', fg="#FFFFFF", bg='#272A37',
                             font=("yu gothic ui", 11, 'bold'))
        output_label.place(x=40, y=590)
        # otp(email_entry3.get())

    def gui_rp2():
        p = new_password_entry.get()
        p1 = con_new_password_entry.get()
        otp1 = otp_entry.get()
        ("get ", otp_entry.get())
        ("otp1 ", otp1)
        ("otpex ", otpex)
        if p == "" or p1 == "" or otp1 == "":
            output_label.config(
                text="All fileds are required")
            ("gui_rp2()")
        elif p == p1 and otp1 == otpex:
            resetpass(email1, p)

        elif p == p1 and otp1 != otpex:
            output_label.config(text="OTP don't match!")
            re_otp_set = Button(win, fg='#f8f8f8', text='Resend OTP', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                                cursor='hand2', relief="flat", bd=0, highlightthickness=0, command=lambda: gui_rp3(), activebackground="#1D90F5")
            re_otp_set.place(x=40, y=660, width=256, height=45)
            otp_entry.delete(0, END)
        elif p != p1 and otp1 == otpex:
            output_label.config(
                text="Passwords don't match...Please enter again")
            con_new_password_entry.delete(0, END)
            new_password_entry.delete(0, END)

    def gui_rp3():
        otp(email_entry3.get())

    def resetpass(mail, newpass):  # to reset password
        conn = sqlite3.connect("AccountSystem1.db")
        cursor = conn.cursor()
        query = 'UPDATE AccountDB SET Password=? WHERE Email=?'
        cursor.execute(
            query, [(new_password_entry.get()), (email_entry3.get())])
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Password changed successfully")
        exit_win()


def otp(email_):  # to generate otp
    import random
    num = random.randint(10000, 99999)
    text = str(num) + \
        ' is your OTP for email verification of MovieMatch.'
    subject = "Email Verification"

    #body = "This is the body of the text message"

    sender = "moviesmailing@gmail.com"

    # ["sanketdalvi362@gmail.com", "ayushrajpro@gmail.com"]
    recipients = email_

    password = "kepeacjuarbhlofv"
    global otpex
    otpex = str(num)
    mail(subject, text, sender, recipients, password)


# ========code for mail =========
# =================================
# ===================================


def mail(subject, body, sender, recipients, password):

    msg = MIMEText(body)

    msg['Subject'] = subject

    msg['From'] = sender

    msg['To'] = ', '.join(recipients)

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    smtp_server.login(sender, password)

    smtp_server.sendmail(sender, recipients, msg.as_string())

    smtp_server.quit()


# ============Register page==============
# ++++++++++++++++++++++++++++++++++++++++


# Signup textvariables
FirstName = StringVar()
LastName = StringVar()
Email = StringVar()
Password = StringVar()
ConfirmPassword = StringVar()
otp_entryy = StringVar()


sign_up.configure(bg="#525561")

# ================Background Image ====================
backgroundImage = PhotoImage(
    file="image_1.png")
bg_image = Label(
    sign_up,
    image=backgroundImage,
    bg="#525561"
)
bg_image.place(x=200, y=70)

# ================ Header Text Left ====================
headerText_image_left = PhotoImage(
    file="headerText_image.png")
headerText_image_label1 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#272A37"
)
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(
    bg_image,
    text="MovieMatch",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
headerText1.place(x=110, y=45)


# ================ CREATE ACCOUNT HEADER ====================
createAccount_header = Label(
    bg_image,
    text="Create new account",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
createAccount_header.place(x=75, y=121)

# ================ ALREADY HAVE AN ACCOUNT TEXT ====================
text = Label(
    bg_image,
    text="Already a member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#272A37"
)
text.place(x=75, y=187)

# ================ GO TO LOGIN ====================
switchLogin = Button(
    bg_image,
    text="Sign in",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda: show_frame(sign_in)
)
switchLogin.place(x=230, y=183, width=50, height=35)

# ================ First Name Section ====================
firstName_image = PhotoImage(
    file="input_img.png")
firstName_image_Label = Label(
    bg_image,
    image=firstName_image,
    bg="#272A37"
)
firstName_image_Label.place(x=80, y=242)

firstName_text = Label(
    firstName_image_Label,
    text="First name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B",
)
firstName_text.place(x=25, y=0)

firstName_icon = PhotoImage(
    file="name_icon.png")
firstName_icon_Label = Label(
    firstName_image_Label,
    image=firstName_icon,
    bg="#3D404B"
)
firstName_icon_Label.place(x=159, y=15)

firstName_entry = Entry(
    firstName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=FirstName
)
firstName_entry.place(x=8, y=17, width=140, height=27)


# ================ Last Name Section ====================
lastName_image = PhotoImage(
    file="input_img.png")
lastName_image_Label = Label(
    bg_image,
    image=lastName_image,
    bg="#272A37"
)
lastName_image_Label.place(x=293, y=242)

lastName_text = Label(
    lastName_image_Label,
    text="Last name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
lastName_text.place(x=25, y=0)

lastName_icon = PhotoImage(
    file="name_icon.png")
lastName_icon_Label = Label(
    lastName_image_Label,
    image=lastName_icon,
    bg="#3D404B"
)
lastName_icon_Label.place(x=159, y=15)

lastName_entry = Entry(
    lastName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=LastName
)
lastName_entry.place(x=8, y=17, width=140, height=27)

# ================ Email Name Section ====================
emailName_image = PhotoImage(
    file="email.png")
emailName_image_Label = Label(
    bg_image,
    image=emailName_image,
    bg="#272A37"
)
emailName_image_Label.place(x=80, y=311)

emailName_text = Label(
    emailName_image_Label,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
emailName_text.place(x=25, y=0)

emailName_icon = PhotoImage(
    file="email-icon.png")
emailName_icon_Label = Label(
    emailName_image_Label,
    image=emailName_icon,
    bg="#3D404B"
)
emailName_icon_Label.place(x=370, y=15)

emailName_entry = Entry(
    emailName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=Email
)
emailName_entry.place(x=8, y=17, width=354, height=27)


# ================ Password Name Section ====================
passwordName_image = PhotoImage(
    file="input_img.png")
passwordName_image_Label = Label(
    bg_image,
    image=passwordName_image,
    bg="#272A37"
)
passwordName_image_Label.place(x=80, y=380)

passwordName_text = Label(
    passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
passwordName_text.place(x=25, y=0)

passwordName_icon = PhotoImage(
    file="pass-icon.png")
passwordName_icon_Label = Label(
    passwordName_image_Label,
    image=passwordName_icon,
    bg="#3D404B"
)
passwordName_icon_Label.place(x=159, y=15)

passwordName_entry = Entry(
    passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=Password
)
passwordName_entry.place(x=8, y=17, width=140, height=27)


# ================ Confirm Password Name Section ====================
confirm_passwordName_image = PhotoImage(
    file="input_img.png")
confirm_passwordName_image_Label = Label(
    bg_image,
    image=confirm_passwordName_image,
    bg="#272A37"
)
confirm_passwordName_image_Label.place(x=293, y=380)

confirm_passwordName_text = Label(
    confirm_passwordName_image_Label,
    text="Confirm Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
confirm_passwordName_text.place(x=25, y=0)

confirm_passwordName_icon = PhotoImage(
    file="pass-icon.png")
confirm_passwordName_icon_Label = Label(
    confirm_passwordName_image_Label,
    image=confirm_passwordName_icon,
    bg="#3D404B"
)
confirm_passwordName_icon_Label.place(x=159, y=15)

confirm_passwordName_entry = Entry(
    confirm_passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=ConfirmPassword
)
confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

# =============== Submit Button ====================
submit_buttonImage = PhotoImage(
    file="button_1.png")
submit_button = Button(
    bg_image,
    image=submit_buttonImage,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#272A37",
    command=lambda: signup(),
    cursor="hand2",
)
submit_button .place(x=130, y=460, width=333, height=65)


def clear():
    global Saving_Email
    Saving_Email = Email
    global Saving_Email2
    Saving_Email2 = emailName_entry.get()
    LastName.set("")
    FirstName.set("")
    Password.set("")
    ConfirmPassword.set("")
    Email.set("")

# +++============database connection for signUp


def signup():
    if firstName_entry.get() == "" or lastName_entry.get() == "" or passwordName_entry.get() == "" or emailName_entry.get() == "" or confirm_passwordName_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif passwordName_entry.get() != confirm_passwordName_entry.get():
        messagebox.showerror(
            "Error", "Password and confirm Password didn't match")
    else:
        (firstName_entry.get())
        (lastName_entry.get())
        (FirstName)
        try:
            conn = sqlite3.connect("AccountSystem1.db")
            cursor = conn.cursor()
            query = 'SELECT * FROM AccountDB WHERE Email = ?'
            cursor.execute(query, [(emailName_entry.get())])
            row = cursor.fetchone()

            if row != None:
                messagebox.showinfo("Error", "Email already exist!")
            else:
                otp_check_sign_up()
        except Exception as es:
            (es)
            messagebox.showerror("Error", "Something went wrong try again")


def otp_check_sign_up():

    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(
        f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Mail Verification')
    win.configure(background='#272A37')
    win.resizable(False, False)
    otp(emailName_entry.get())
    # ====== Email ====================
    global otp_entry4
    otp_entry4 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                       bd=0, textvariable=otp_entryy)
    otp_entry4.place(x=40, y=80, width=256, height=50)
    otp_entry4.config(highlightbackground="#3D404B",
                      highlightcolor="#206DB4")
    email_label4 = Label(win, text='• OTP', fg="#FFFFFF", bg='#272A37',
                         font=("yu gothic ui", 11, 'bold'))
    email_label4.place(x=40, y=50)

    update_pass = Button(win, fg='#f8f8f8', text='Submit', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, command=lambda: true_convert(), activebackground="#1D90F5")
    update_pass.place(x=40, y=150, width=256, height=45)

    def exit_win():
        win.destroy()

    def true_convert():
        (otpex)
        ("hi")
        (otp_entry4.get())
        ("why")
        (otp_entryy)
        if otp_entry4.get() == otpex:
            ("true_convert")
            global a
            a = True
            finally_creating()
        else:
            ("otp doesnot matchhh")
#

    def finally_creating():
        ("finally_creating")
        (a)
        if(a):
            try:
                connection = sqlite3.connect("AccountSystem1.db")
                cur = connection.cursor()
                cur.execute("INSERT INTO AccountDB(FirstName, LastName ,EMAIL , Password) VALUES(?,?,?,?)", (
                    firstName_entry.get(), lastName_entry.get(), emailName_entry.get(), passwordName_entry.get()))
                connection.commit()
                connection.close()
                clear()
                messagebox.showinfo(
                    "Success", "New account created successfully")
                exit_win()
                show_frame(genre_choise)

            except Exception as es:
                messagebox.showerror("Error", "Something went wrong try again")
        else:
            ("howww")
            ("else of finally_converting")
            otp_entry4.delete(0, END)


#================genre selection=======#
# =======================================
genre_choise.configure(bg="#525561")

# ================Background Image ====================
genre_backgroundImage = PhotoImage(
    file="image_1.png")
genre_bg_image = Label(
    genre_choise,
    image=genre_backgroundImage,
    bg="#525561"
)
genre_bg_image.place(x=200, y=70)

# ================ Header Text Left ====================
genre_headerText_image_left = PhotoImage(
    file="headerText_image.png")
genre_headerText_image_label1 = Label(
    genre_bg_image,
    image=genre_headerText_image_left,
    bg="#272A37"
)
genre_headerText_image_label1.place(x=60, y=45)

genre_headerText1 = Label(
    genre_bg_image,
    text="MovieMatch",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
genre_headerText1.place(x=110, y=45)

# =================
genre_header = Label(
    genre_bg_image,
    text="Choose Your Three Favourite Genres ",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
genre_header.place(x=75, y=121)

#dropBox code#
############
############

genre_checkbox_image = PhotoImage(
    file="input_img.png")
option_menu1_image_Label1 = Label(
    genre_bg_image,
    image=genre_checkbox_image,
    bg="#272A37"
)
option_menu1_image_Label2 = Label(
    genre_bg_image,
    image=genre_checkbox_image,
    bg="#272A37"
)
option_menu1_image_Label3 = Label(
    genre_bg_image,
    image=genre_checkbox_image,
    bg="#272A37"
)
option_menu1_image_Label1.place(x=60, y=190)
option_menu1_image_Label2.place(x=285, y=190)
option_menu1_image_Label3.place(x=510, y=190)
genres = ("Comedy", "Drama", "Action", "Adventure", "Romance",
          "Science Fiction", "Thriller", "Horror", "Fantasy", "Animation")
genre_select_var1 = StringVar()
genre_select_var2 = StringVar()
genre_select_var3 = StringVar()


def option_changed():
    genre_select_var1.get()
    genre_select_var2.get()
    genre_select_var3.get()


option_menu1 = ttk.OptionMenu(
    option_menu1_image_Label1,
    genre_select_var1,
    genres[0],
    *genres,
    style='my.TMenubutton')
option_menu2 = ttk.OptionMenu(
    option_menu1_image_Label2,
    genre_select_var2,
    genres[0],
    *genres,
    style='my.TMenubutton')
s = ttk.Style()
option_menu3 = ttk.OptionMenu(
    option_menu1_image_Label3,
    genre_select_var3,
    genres[0],
    *genres,
    style='my.TMenubutton')
s.configure('my.TMenubutton', foreground="#FFFFFF",
            background="#3D404B", bg="red", font=('Arial', 20, 'bold'))

option_menu1.place(x=35, y=7)
option_menu2.place(x=35, y=7)
option_menu3.place(x=35, y=7)

genre_submit_buttonImage = PhotoImage(
    file="button_1.png")
submit_button = Button(
    genre_bg_image,
    image=genre_submit_buttonImage,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#272A37",
    command=lambda: genre_data_entry(),
    cursor="hand2",
)
submit_button.place(x=140, y=400, width=333, height=65)


def genre_data_entry():
    ("genre_data_entry")
    if((genre_select_var1.get() != genre_select_var2.get()) and (genre_select_var2.get() != genre_select_var3.get()) and (genre_select_var1.get() != genre_select_var3.get())):
        try:
            connection = sqlite3.connect("AccountSystem1.db")
            cur = connection.cursor()
            ("inn")
            cur.execute("""UPDATE AccountDB SET Genre1 = ?, Genre2 = ?, Genre3 = ? WHERE EMAIL = ? """, (
                genre_select_var1.get(), genre_select_var2.get(), genre_select_var3.get(), Saving_Email2))
            ("here")
            connection.commit()
            connection.close()
            messagebox.showinfo(
                "Success", "Genre saved successfully")

        except Exception as es:
            (es)
            messagebox.showerror("Error", "Something went wrong try again")
    else:
        messagebox.showerror("Error", "Please select unique genre")
        ("else of genre_data_entry")


##############
###############
###################


show_frame(sign_in)


AccountSystem.resizable(0, 0)
AccountSystem.mainloop()
