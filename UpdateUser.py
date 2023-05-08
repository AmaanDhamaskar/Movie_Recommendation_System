from email.mime.text import MIMEText
import smtplib
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


def Update_User_Page(username):
    Emailll=username
    window = Tk()

    height = 650
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.state('zoomed')

    window.configure(bg="#525561")

    #[(1, 'Ayush', 'Rajpurohit', 'ayushrajpro@gmail.com', 'Password', 'Genre 3', 'Genre 5', 'Genre 7')]
# 'ayushrajpro@gmail.com'
    def somename(Emailll):
        print(type(Emailll))
        conn = sqlite3.connect("AccountSystem1.db")
        cursor = conn.cursor()
        # print(Login_emailName_entry.get())
        find_user = 'SELECT * FROM AccountDB WHERE EMAIL = ? '
        cursor.execute(
            find_user, [Emailll])
        global result
        result = cursor.fetchall()
        print(result[0][3])

    somename(Emailll)

    FirstName = StringVar()
    FirstName.set(result[0][1])
    LastName = StringVar()
    LastName.set(result[0][2])
    Date_of_birth = StringVar()
    Date_of_birth.set(result[0][8])

    # ================Background Image ====================
    backgroundImage = PhotoImage(
        file="image_1.png")
    Up_bg_image = Label(
        window,
        image=backgroundImage,
        bg="#525561"
    )
    Up_bg_image.place(x=200, y=70)

    # ================ Header Text Left ====================
    headerText_image_left = PhotoImage(
        file="headerText_image.png")
    Up_headerText_image_label1 = Label(
        Up_bg_image,
        image=headerText_image_left,
        bg="#272A37"
    )
    Up_headerText_image_label1.place(x=60, y=45)

    headerText1 = Label(
        Up_bg_image,
        text=result[0][3],  # usermail
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    headerText1.place(x=110, y=45)

    Up_createAccount_header = Label(
        Up_bg_image,
        text="Personal Details",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 28 * -1),
        bg="#272A37"
    )
    Up_createAccount_header.place(x=75, y=121)

    def makingchange():
        firstName_entry.config(state='normal')
        lastName_entry.config(state='normal')
        cal.config(state='normal')
        Up_passwordName_entry.config(state='normal')
        option_menu1['state'] = 'normal'
        option_menu2['state'] = 'normal'
        option_menu3['state'] = 'normal'
        #switchLogin['text'] = 'Save'
        print(Date_of_birth.get(), "hi")
        print(switchLogin['text'])
        if switchLogin['text'] == 'Save':
            print(switchLogin['text'], "in if")
            Up_user()
            #switchLogin['command'] = Up_user
        else:
            print(switchLogin['text'], "in else")
            switchLogin['text'] = 'Save'

    switchLogin = Button(
        Up_bg_image,
        text="Edit",
        fg="#206DB4",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37",
        bd=0,
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff",
        command=makingchange
    )
    switchLogin.place(x=300, y=125, width=50, height=35)

    firstName_image = PhotoImage(
        file="input_img.png")
    firstName_image_Label = Label(
        Up_bg_image,
        image=firstName_image,
        bg="#272A37"
    )
    firstName_image_Label.place(x=80, y=200)

    firstName_text = Label(
        firstName_image_Label,
        text="First name",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
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

    Up_firstName_text = Label(
        firstName_image_Label,
        text=result[0][1],
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 17 * -1),
        bg="#3D404B"
    )
    Up_firstName_text.place(x=8, y=17, width=140, height=27)

    firstName_entry = Entry(
        firstName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
        disabledbackground="#3D404B",
        readonlybackground="#3D404B",
        textvariable=FirstName,
        state='disabled'
    )
    firstName_entry.place(x=8, y=17, width=140, height=27)

    # ===========lastname
    lastName_image = PhotoImage(
        file="input_img.png")
    lastName_image_Label = Label(
        Up_bg_image,
        image=lastName_image,
        bg="#272A37"
    )
    lastName_image_Label.place(x=293, y=200)

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
        textvariable=LastName,
        disabledbackground="#3D404B",
        state='disabled'
    )
    lastName_entry.place(x=8, y=17, width=140, height=27)

    # =============dateOfBirth
    Dob_image = PhotoImage(
        file="input_img.png")
    Dob_image_Label = Label(
        Up_bg_image,
        image=Dob_image,
        bg="#272A37"
    )
    Dob_image_Label.place(x=80, y=270)

    Dob_text = Label(
        Dob_image_Label,
        text="Date of Birth",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    Dob_text.place(x=25, y=0)

    dob_icon = PhotoImage(
        file="email-icon.png")
    dob_icon_Label = Label(
        Dob_image_Label,
        image=dob_icon,
        bg="#3D404B"
    )
    dob_icon_Label.place(x=159, y=15)

    # Dob_icon = PhotoImage(
    #     file="email-icon.png")
    # Dob_icon_Label = Label(
    #     Dob_image_Label,
    #     image=Dob_icon,
    #     bg="#3D404B"
    # )
    # Dob_icon_Label.place(x=370, y=15)
    # "#3D404B"
    cal = DateEntry(Dob_image_Label,
                    width=12,
                    bd=0,
                    # bg="red",
                    highlightthickness=0,
                    year=2019,
                    month=6,
                    day=22,
                    font=("yu gothic ui SemiBold", 16 * -1),
                    textvariable=Date_of_birth,
                    background="blue",
                    foreground="white",
                    # headersbackground="yellow",
                    # headerforeground="green",
                    # bordercolor="green",
                    # selectbackground="orange",
                    # tooltipbackground="orange",
                    # tooltipforeground="orange",
                    date_pattern='dd/mm/y',
                    disabledselectbackground="#3D404B",
                    state="disabled",
                    borderwidth=2
                    )

    # Dob_entry = Entry(
    #     Dob_image_Label,
    #     bd=0,
    #     bg="#3D404B",
    #     highlightthickness=0,
    #     font=("yu gothic ui SemiBold", 16 * -1),
    #     textvariable=Date_of_birth,
    #     disabledbackground="#3D404B",
    #     state='disabled'
    # )
    cal.place(x=20, y=19, width=110, height=27)

    # ========password

    Up_Password = StringVar()
    Up_Password.set(result[0][4])

    Up_passwordName_image = PhotoImage(
        file="input_img.png")
    Up_passwordName_image_Label = Label(
        Up_bg_image,
        image=Up_passwordName_image,
        bg="#272A37"
    )
    Up_passwordName_image_Label.place(x=293, y=270)

    Up_passwordName_text = Label(
        Up_passwordName_image_Label,
        text="Confirm Password",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    Up_passwordName_text.place(x=25, y=0)

    Up_passwordName_icon = PhotoImage(
        file="pass-icon.png")
    Up_passwordName_icon_Label = Label(
        Up_passwordName_image_Label,
        image=Up_passwordName_icon,
        bg="#3D404B"
    )
    Up_passwordName_icon_Label.place(x=159, y=15)

    Up_passwordName_entry = Entry(
        Up_passwordName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
        textvariable=Up_Password,
        disabledbackground="#3D404B",
        state='disabled'
    )
    Up_passwordName_entry.place(x=8, y=17, width=140, height=27)

    # =============genre

    genre_checkbox_image = PhotoImage(
        file="input_img.png")
    option_menu1_image_Label1 = Label(
        Up_bg_image,
        image=genre_checkbox_image,
        bg="#272A37"
    )
    option_menu1_image_Label2 = Label(
        Up_bg_image,
        image=genre_checkbox_image,
        bg="#272A37"
    )
    option_menu1_image_Label3 = Label(
        Up_bg_image,
        image=genre_checkbox_image,
        bg="#272A37"
    )
    option_menu1_image_Label1.place(x=80, y=340)
    option_menu1_image_Label2.place(x=305, y=340)
    option_menu1_image_Label3.place(x=530, y=340)
    genres = ("Comedy", "Drama", "Action", "Adventure", "Romance",
          "Science Fiction", "Thriller", "Horror", "Fantasy", "Animation")
    genre_select_var1 = StringVar()
    genre_select_var2 = StringVar()
    genre_select_var3 = StringVar()
    # genre_select_var1.set(result[0][5])
    # genre_select_var2.set(result[0][6])
    # genre_select_var3.set(result[0][7])
    tempVar1 = result[0][5]
    tempVar2 = result[0][6]
    tempVar3 = result[0][7]

    def option_changed():
        genre_select_var1.get()
        genre_select_var2.get()
        genre_select_var3.get()

    option_menu1 = ttk.OptionMenu(
        option_menu1_image_Label1,
        genre_select_var1,
        tempVar1,
        *genres,
        style='my.TMenubutton')
    option_menu2 = ttk.OptionMenu(
        option_menu1_image_Label2,
        genre_select_var2,
        tempVar2,
        *genres,
        style='my.TMenubutton')
    s = ttk.Style()
    option_menu3 = ttk.OptionMenu(
        option_menu1_image_Label3,
        genre_select_var3,
        tempVar3,
        *genres,
        style='my.TMenubutton'
    )
    s.configure('my.TMenubutton', foreground="black",
                background="#3D404B", bg="red", font=('Arial', 20, 'bold'))
    option_menu1.state([DISABLED])
    option_menu2.state([DISABLED])
    option_menu3.state([DISABLED])
    option_menu1.place(x=35, y=7)
    option_menu2.place(x=35, y=7)
    option_menu3.place(x=35, y=7)

    # =========genre

    # =============submit

    # saving changes
    ######################
    ####################

    def Up_user():
        if firstName_entry.get() == "" or lastName_entry.get() == "" or Up_passwordName_entry.get() == "" or Date_of_birth.get() == "00/00/0000":
            messagebox.showerror("Error", "All fields are required!")
        elif(genre_select_var1.get() == genre_select_var2.get()) and (genre_select_var2.get() == genre_select_var3.get()) and (genre_select_var1.get() == genre_select_var3.get()):
            messagebox.showerror("Error", "Please select unique genre")
        else:
            try:
                otp_check_sign_up()
            except Exception as es:
                print(es)
                messagebox.showerror("Error", "Something went wrong try again")

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

    def mail(subject, body, sender, recipients, password):

        msg = MIMEText(body)

        msg['Subject'] = subject

        msg['From'] = sender

        msg['To'] = ', '.join(recipients)

        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        smtp_server.login(sender, password)

        smtp_server.sendmail(sender, recipients, msg.as_string())

        smtp_server.quit()

    Up_otp_entryy = StringVar()

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
        otp(Emailll)
        # ====== Email ====================
        global otp_entry4
        otp_entry4 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                           bd=0, textvariable=Up_otp_entryy)
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
            print(otpex)
            print("hi")
            print(otp_entry4.get())
            print("why")
            print(Up_otp_entryy)
            if otp_entry4.get() == otpex:
                print("true_convert")
                global a
                a = True
                finally_creating()
            else:
                print("otp doesnot matchhh")
    #

        def finally_creating():
            print("finally_creating")
            print(a)
            if(a):
                try:
                    connection = sqlite3.connect("AccountSystem1.db")
                    cur = connection.cursor()
                    print("befor execute")
                    print(firstName_entry.get(), lastName_entry.get(), Up_passwordName_entry.get(), genre_select_var1.get(
                    ), genre_select_var2.get(), genre_select_var3.get(), Date_of_birth.get(), Emailll)
                    #print(Date_of_birth.get(), " ", Emailll)
                    # cur.execute("INSERT INTO AccountDB(FirstName, LastName , Password, Genre 1, Genre 2, Genre 3, DOB ) VALUES(?,?,?,?,?,?,?)", (
                    #     firstName_entry.get(), lastName_entry.get(), Up_passwordName_entry.get(), passwordName_entry.get()))
                    cur.execute("""UPDATE AccountDB SET FirstName = ?, LastName = ? , Password = ?, Genre1 = ?, Genre2 = ?, Genre3 = ?, DOB = ? WHERE EMAIL = ? """, (
                        firstName_entry.get(), lastName_entry.get(), Up_passwordName_entry.get(), genre_select_var1.get(), genre_select_var2.get(), genre_select_var3.get(), Date_of_birth.get(), Emailll))
                    print("After execute")
                    connection.commit()
                    connection.close()
                    # clear()
                    messagebox.showinfo(
                        "Success", "Updates done successfully")
                    exit_win()
                    firstName_entry.config(state='disabled')
                    lastName_entry.config(state='disabled')
                    cal.config(state='disabled')
                    Up_passwordName_entry.config(state='disabled')
                    option_menu1['state'] = 'disabled'
                    option_menu2['state'] = 'disabled'
                    option_menu3['state'] = 'disabled'
                    switchLogin['text'] = 'Edit'
                    # show_frame(genre_choise)

                except Exception as es:
                    messagebox.showerror(
                        "Error", "Something went wrong try again of finallycon")
            else:
                print("howww")
                print("else of finally_converting")
                otp_entry4.delete(0, END)

    ###################
    # 3
    ####################
    window.resizable(False, False)
    window.mainloop()

    # naming()
