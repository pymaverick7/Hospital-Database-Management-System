from PIL import ImageTk, Image
import customtkinter
from customtkinter import CTkFont
from tkinter import messagebox
from tkcalendar import Calendar
import mysql.connector
import random
import string
from tkinter import ttk


# Window Settings
window = customtkinter.CTk()
window.geometry("1580x980")
window.title("Zoe Hospital Database System")
window.iconbitmap("pic.ico")
#window.state('zoomed')
window.attributes("-fullscreen",True)
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")

# Connection to Database
my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Maverick7%",
    database="HospitalDB"
)
my_cursor = my_connect.cursor()

# Set Custom Fonts
font = CTkFont(
    family="Montserrat",
    size=16,
    weight="bold"
)
font_title = CTkFont(
    family="Monserrat",
    size=30,
    weight="bold"
)

# Set Background
my_bg = ImageTk.PhotoImage(Image.open("a1.png"))
lbl = customtkinter.CTkLabel(window, image=my_bg, text="")
lbl.place(x=0, y=0, relwidth=1, relheight=1)

# Set frame for Buttons
frame = customtkinter.CTkFrame(window, width=1580, height=500, bg_color="#29b491", fg_color="#29b491")
frame.pack(side="bottom")


# Functions


# Register Patients Function
def reg_patients():
    # window.withdraw()
    reg_top = customtkinter.CTkToplevel(window)
    reg_top.geometry("700x750")
    reg_top.title("Register New Patients")
    reg_top.iconbitmap("pic.ico")

    my_bg = ImageTk.PhotoImage(Image.open("window.png"))
    lbl = customtkinter.CTkLabel(reg_top, image=my_bg, text="")
    lbl.place(x=0, y=0, relwidth=1, relheight=1)

    def submit_pat():
        n = list(string.digits)
        random.shuffle(n)
        random.shuffle(n)
        password = ["PID"]
        for i in range(5):
            password.append(random.choice(n))
        h = "".join(password)
        fname = entry_fname.get()
        mname = entry_mname.get()
        lname = entry_lname.get()
        day = Combo_day.get()
        month = combo_month.get()
        year = entry_year.get()
        age = entry_age.get()
        email = entry_email.get()
        number = entry_num.get()
        idcard = combo_id.get()
        idnum = entry_idnum.get()
        residence = entry_resi.get()
        gender = combo_gender.get()
        blood = combo_blood.get()
        height = entry_height.get()
        sql = "insert into Patients(PID,First_Name, Middle_Name, Last_Name, Day, Month, Year, Age, Email, Phone_Number, " \
              "ID_Card, ID_Number, Residence, Gender, Blood, Height) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        val = (
            h, fname, mname, lname, day, month, year, age, email, number, idcard, idnum, residence, gender, blood,
            height)
        my_cursor.execute(sql, val)
        my_connect.commit()
        messagebox.showinfo("Patients ID Number", f"Your Patient ID is {h}")
        messagebox.showinfo("Register Health Staff", "Details Successfully Recorded!")
        fname = entry_fname.delete(0, "end")
        mname = entry_mname.delete(0, "end")
        lname = entry_lname.delete(0, "end")
        year = entry_year.delete(0, "end")
        age = entry_age.delete(0, "end")
        email = entry_email.delete(0, "end")
        number = entry_num.delete(0, "end")
        idnum = entry_idnum.delete(0, "end")
        residence = entry_resi.delete(0, "end")
        height = entry_height.delete(0, "end")
        # window.mainloop()

    frame = customtkinter.CTkFrame(reg_top, width=700, height=700, bg_color="#29b491", fg_color="#29b491")
    frame.pack(side="bottom")

    # Registration frame window
    label_top = customtkinter.CTkLabel(frame, text="Register New Patients", font=font_title)
    label_top.grid(row=0, column=0, columnspan=3, pady=10)

    # Labels and Entries for name
    label_fname = customtkinter.CTkLabel(frame, text="First Name", font=font)
    label_fname.grid(row=1, column=0, padx=50, pady=5)
    entry_fname = customtkinter.CTkEntry(frame, width=150)
    entry_fname.grid(row=2, column=0)

    label_mname = customtkinter.CTkLabel(frame, text="Middle Name", font=font)
    label_mname.grid(row=1, column=1, padx=50, pady=5)
    entry_mname = customtkinter.CTkEntry(frame, width=150)
    entry_mname.grid(row=2, column=1)

    label_lname = customtkinter.CTkLabel(frame, text="Last Name", font=font)
    label_lname.grid(row=1, column=2, padx=50, pady=5)
    entry_lname = customtkinter.CTkEntry(frame, width=150)
    entry_lname.grid(row=2, column=2)

    # Labels and Entries for Date of Birth
    label_dob = customtkinter.CTkLabel(frame, text="Date of Birth", font=font)
    label_dob.grid(row=3, column=0, columnspan=3, pady=10)

    label_day = customtkinter.CTkLabel(frame, text="Day", font=font)
    label_day.grid(row=4, column=0)
    Combo_day = customtkinter.CTkCombobox(frame,
                                          values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                                                  "14",
                                                  "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                                                  "26",
                                                  "27", "28", "29", "30", "31"])
    Combo_day.grid(row=5, column=0, pady=10)

    label_month = customtkinter.CTkLabel(frame, text="Month", font=font)
    label_month.grid(row=4, column=1)
    combo_month = customtkinter.CTkCombobox(frame,
                                            values=["January", "February", "March", "April", "May", "June", "July",
                                                    "August", "September", "October", "November", "December"])
    combo_month.grid(row=5, column=1, pady=10)

    label_year = customtkinter.CTkLabel(frame, text="Year", font=font)
    label_year.grid(row=4, column=2)
    entry_year = customtkinter.CTkEntry(frame, width=150)
    entry_year.grid(row=5, column=2, pady=10)

    label_age = customtkinter.CTkLabel(frame, text="Age", font=font)
    label_age.grid(row=6, column=0)
    entry_age = customtkinter.CTkEntry(frame, width=150)
    entry_age.grid(row=7, column=0, pady=10)

    label_email = customtkinter.CTkLabel(frame, text="Email", font=font)
    label_email.grid(row=6, column=1, pady=10)
    entry_email = customtkinter.CTkEntry(frame, width=150)
    entry_email.grid(row=7, column=1, pady=10)

    label_num = customtkinter.CTkLabel(frame, text="Phone Number", font=font)
    label_num.grid(row=6, column=2, pady=10)
    entry_num = customtkinter.CTkEntry(frame, width=150)
    entry_num.grid(row=7, column=2, pady=10)

    label_id = customtkinter.CTkLabel(frame, text="ID Card Type", font=font)
    label_id.grid(row=8, column=0, pady=10)
    combo_id = customtkinter.CTkCombobox(frame, values=["Ghana Card", "Passport", "Voters ID", "Institution ID",
                                                        "Drivers' License"])
    combo_id.grid(row=9, column=0, pady=10)

    label_idnum = customtkinter.CTkLabel(frame, text="ID Number", font=font)
    label_idnum.grid(row=8, column=1, pady=10)
    entry_idnum = customtkinter.CTkEntry(frame, width=150)
    entry_idnum.grid(row=9, column=1, pady=10)

    label_resi = customtkinter.CTkLabel(frame, text="Place of Residence", font=font)
    label_resi.grid(row=8, column=2, pady=10)
    entry_resi = customtkinter.CTkEntry(frame, width=150)
    entry_resi.grid(row=9, column=2, pady=10)

    label_gender = customtkinter.CTkLabel(frame, text="Gender", font=font)
    label_gender.grid(row=10, column=0, pady=10)
    combo_gender = customtkinter.CTkCombobox(frame, values=["Male", "Female", "Others"])
    combo_gender.grid(row=11, column=0, pady=10)

    label_blood = customtkinter.CTkLabel(frame, text="Blood Group", font=font)
    label_blood.grid(row=10, column=1, pady=10)
    combo_blood = customtkinter.CTkCombobox(frame, values=["A", "B", "AB", "O"])
    combo_blood.grid(row=11, column=1, pady=10)

    label_height = customtkinter.CTkLabel(frame, text="Height", font=font)
    label_height.grid(row=10, column=2, pady=10)
    entry_height = customtkinter.CTkEntry(frame, width=150)
    entry_height.grid(row=11, column=2, pady=10)

    btn_register = customtkinter.CTkButton(frame, text="Register", width=200, height=55, font=font_title,
                                           command=submit_pat)
    btn_register.grid(row=12, column=0, columnspan=3, pady=30)


# Register Health Staff
def reg_health():
    reg_h_staff = customtkinter.CTkToplevel(window)
    reg_h_staff.geometry("700x750")
    reg_h_staff.title("Register Health Staff")
    reg_h_staff.iconbitmap("pic.ico")

    my_bg = ImageTk.PhotoImage(Image.open("window.png"))
    lbl = customtkinter.CTkLabel(reg_h_staff, image=my_bg, text="")
    lbl.place(x=0, y=0, relwidth=1, relheight=1)

    def submit_health():
        n = list(string.digits)
        random.shuffle(n)
        random.shuffle(n)
        password = ["HID"]
        for i in range(5):
            password.append(random.choice(n))
        h = "".join(password)

        fname = entry_fname.get()
        mname = entry_mname.get()
        lname = entry_lname.get()
        day = Combo_day.get()
        month = combo_month.get()
        year = entry_year.get()
        age = entry_age.get()
        email = entry_email.get()
        number = entry_num.get()
        idcard = combo_id.get()
        idnum = entry_idnum.get()
        residence = entry_resi.get()
        gender = combo_gender.get()
        cate = combo_cate.get()
        height = entry_height.get()
        sql = "insert into H_Staff(HID,First_Name, Middle_name, Last_name, Day, Month, Year, Age, Email, Phone_Number,ID_Card, ID_Number, Residence, Gender,Cate, Height) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        val = (
            h, fname, mname, lname, day, month, year, age, email, number, idcard, idnum, residence, gender, cate,
            height)
        my_cursor.execute(sql, val)
        my_connect.commit()
        messagebox.showinfo("Health Staff ID Number", f"Your Health Staff ID is {h}")
        messagebox.showinfo("Register Health Staff", "Details Successfully Recorded!")
        fname = entry_fname.delete(0, "end")
        mname = entry_mname.delete(0, "end")
        lname = entry_lname.delete(0, "end")
        year = entry_year.delete(0, "end")
        age = entry_age.delete(0, "end")
        email = entry_email.delete(0, "end")
        number = entry_num.delete(0, "end")
        idnum = entry_idnum.delete(0, "end")
        residence = entry_resi.delete(0, "end")
        height = entry_height.delete(0, "end")

    frame_2 = customtkinter.CTkFrame(reg_h_staff, width=700, height=700, bg_color="#29b491", fg_color="#29b491")
    frame_2.pack(side="bottom")

    # Registration frame window
    label_top = customtkinter.CTkLabel(frame_2, text="Register New Health-Staff", font=font_title)
    label_top.grid(row=0, column=0, columnspan=3, pady=10)
    # Labels and Entries for name
    label_fname = customtkinter.CTkLabel(frame_2, text="First Name", font=font)
    label_fname.grid(row=1, column=0, padx=50, pady=5)
    entry_fname = customtkinter.CTkEntry(frame_2, width=150)
    entry_fname.grid(row=2, column=0)

    label_mname = customtkinter.CTkLabel(frame_2, text="Middle Name", font=font)
    label_mname.grid(row=1, column=1, padx=50, pady=5)
    entry_mname = customtkinter.CTkEntry(frame_2, width=150)
    entry_mname.grid(row=2, column=1)

    label_lname = customtkinter.CTkLabel(frame_2, text="Last Name", font=font)
    label_lname.grid(row=1, column=2, padx=50, pady=5)
    entry_lname = customtkinter.CTkEntry(frame_2, width=150)
    entry_lname.grid(row=2, column=2)

    # Labels and Entries for Date of Birth
    label_dob = customtkinter.CTkLabel(frame_2, text="Date of Birth", font=font)
    label_dob.grid(row=3, column=0, columnspan=3, pady=10)

    label_day = customtkinter.CTkLabel(frame_2, text="Day", font=font)
    label_day.grid(row=4, column=0)
    Combo_day = customtkinter.CTkCombobox(frame_2,
                                          values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                                                  "14",
                                                  "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                                                  "26",
                                                  "27", "28", "29", "30", "31"])
    Combo_day.grid(row=5, column=0, pady=10)

    label_month = customtkinter.CTkLabel(frame_2, text="Month", font=font)
    label_month.grid(row=4, column=1)
    combo_month = customtkinter.CTkCombobox(frame_2,
                                            values=["January", "February", "March", "April", "May", "June", "July",
                                                    "August", "September", "October", "November", "December"])
    combo_month.grid(row=5, column=1, pady=10)

    label_year = customtkinter.CTkLabel(frame_2, text="Year", font=font)
    label_year.grid(row=4, column=2)
    entry_year = customtkinter.CTkEntry(frame_2, width=150)
    entry_year.grid(row=5, column=2, pady=10)

    label_age = customtkinter.CTkLabel(frame_2, text="Age", font=font)
    label_age.grid(row=6, column=0)
    entry_age = customtkinter.CTkEntry(frame_2, width=150)
    entry_age.grid(row=7, column=0, pady=10)

    label_email = customtkinter.CTkLabel(frame_2, text="Email", font=font)
    label_email.grid(row=6, column=1, pady=10)
    entry_email = customtkinter.CTkEntry(frame_2, width=150)
    entry_email.grid(row=7, column=1, pady=10)

    label_num = customtkinter.CTkLabel(frame_2, text="Phone Number", font=font)
    label_num.grid(row=6, column=2, pady=10)
    entry_num = customtkinter.CTkEntry(frame_2, width=150)
    entry_num.grid(row=7, column=2, pady=10)

    label_id = customtkinter.CTkLabel(frame_2, text="ID Card Type", font=font)
    label_id.grid(row=8, column=0, pady=10)
    combo_id = customtkinter.CTkCombobox(frame_2, values=["Ghana Card", "Passport", "Voters ID", "Institution ID",
                                                          "Drivers' License"])
    combo_id.grid(row=9, column=0, pady=10)

    label_idnum = customtkinter.CTkLabel(frame_2, text="ID Number", font=font)
    label_idnum.grid(row=8, column=1, pady=10)
    entry_idnum = customtkinter.CTkEntry(frame_2, width=150)
    entry_idnum.grid(row=9, column=1, pady=10)

    label_resi = customtkinter.CTkLabel(frame_2, text="Place of Residence", font=font)
    label_resi.grid(row=8, column=2, pady=10)
    entry_resi = customtkinter.CTkEntry(frame_2, width=150)
    entry_resi.grid(row=9, column=2, pady=10)

    label_gender = customtkinter.CTkLabel(frame_2, text="Gender", font=font)
    label_gender.grid(row=10, column=0, pady=10)
    combo_gender = customtkinter.CTkCombobox(frame_2, values=["Male", "Female", "Others"])
    combo_gender.grid(row=11, column=0, pady=10)

    label_blood = customtkinter.CTkLabel(frame_2, text="Health Category", font=font)
    label_blood.grid(row=10, column=1, pady=10)
    combo_cate = customtkinter.CTkCombobox(frame_2, values=["Attending Physician", "Specialist", "Nurse", "Physician "
                                                                                                          "Assistant",
                                                            "Therapist", "Pharmacist", "Dietitian"])
    combo_cate.grid(row=11, column=1, pady=10)

    label_height = customtkinter.CTkLabel(frame_2, text="Height", font=font)
    label_height.grid(row=10, column=2, pady=10)
    entry_height = customtkinter.CTkEntry(frame_2, width=150)
    entry_height.grid(row=11, column=2, pady=10)

    btn_register = customtkinter.CTkButton(frame_2, text="Register", width=200, height=55, font=font_title,
                                           command=submit_health)
    btn_register.grid(row=12, column=0, columnspan=3, pady=30)


# Register Non-Health Staff
def reg_nonhealth():
    reg_non_h_staff = customtkinter.CTkToplevel(window)
    reg_non_h_staff.geometry("700x750")
    reg_non_h_staff.title("Register Health Staff")
    reg_non_h_staff.iconbitmap("pic.ico")

    my_bg = ImageTk.PhotoImage(Image.open("window.png"))
    lbl = customtkinter.CTkLabel(reg_non_h_staff, image=my_bg, text="")
    lbl.place(x=0, y=0, relwidth=1, relheight=1)

    def submit_nonhealth():
        n = list(string.digits)
        random.shuffle(n)
        random.shuffle(n)
        password = ["NHID"]
        for i in range(5):
            password.append(random.choice(n))
        h = "".join(password)

        fname = entry_fname.get()
        mname = entry_mname.get()
        lname = entry_lname.get()
        day = Combo_day.get()
        month = combo_month.get()
        year = entry_year.get()
        age = entry_age.get()
        email = entry_email.get()
        number = entry_num.get()
        idcard = combo_id.get()
        idnum = entry_idnum.get()
        residence = entry_resi.get()
        gender = combo_gender.get()
        cate = entry_cate.get()
        height = entry_height.get()
        sql = "insert into NonH_Staff(NHID,First_Name, Middle_name, Last_name, Day, Month, Year, Age, Email, " \
              "Phone_Number,ID_Card, ID_Number, Residence, Gender,NonH_Cate, Height) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s) "
        val = (
            h, fname, mname, lname, day, month, year, age, email, number, idcard, idnum, residence, gender, cate,
            height)
        my_cursor.execute(sql, val)
        my_connect.commit()
        messagebox.showinfo("Non-Health Staff ID Number", f"Your Non-Health Staff ID is {h}")
        messagebox.showinfo("Register Non-Health Staff", "Details Successfully Recorded!")
        fname = entry_fname.delete(0, "end")
        mname = entry_mname.delete(0, "end")
        lname = entry_lname.delete(0, "end")
        year = entry_year.delete(0, "end")
        age = entry_age.delete(0, "end")
        email = entry_email.delete(0, "end")
        number = entry_num.delete(0, "end")
        idnum = entry_idnum.delete(0, "end")
        residence = entry_resi.delete(0, "end")
        cate = entry_cate.delete(0, "end")
        height = entry_height.delete(0, "end")

    # creating the frames
    frame_2 = customtkinter.CTkFrame(reg_non_h_staff, width=700, height=700, bg_color="#29b491", fg_color="#29b491")
    frame_2.pack(side="bottom")

    # Registration frame window
    label_top = customtkinter.CTkLabel(frame_2, text="Register New Non-Health Staff", font=font_title)
    label_top.grid(row=0, column=0, columnspan=3, pady=10)
    # Labels and Entries for name
    label_fname = customtkinter.CTkLabel(frame_2, text="First Name", font=font)
    label_fname.grid(row=1, column=0, padx=50, pady=5)
    entry_fname = customtkinter.CTkEntry(frame_2, width=150)
    entry_fname.grid(row=2, column=0)

    label_mname = customtkinter.CTkLabel(frame_2, text="Middle Name", font=font)
    label_mname.grid(row=1, column=1, padx=50, pady=5)
    entry_mname = customtkinter.CTkEntry(frame_2, width=150)
    entry_mname.grid(row=2, column=1)

    label_lname = customtkinter.CTkLabel(frame_2, text="Last Name", font=font)
    label_lname.grid(row=1, column=2, padx=50, pady=5)
    entry_lname = customtkinter.CTkEntry(frame_2, width=150)
    entry_lname.grid(row=2, column=2)

    # Labels and Entries for Date of Birth
    label_dob = customtkinter.CTkLabel(frame_2, text="Date of Birth", font=font)
    label_dob.grid(row=3, column=0, columnspan=3, pady=10)

    label_day = customtkinter.CTkLabel(frame_2, text="Day", font=font)
    label_day.grid(row=4, column=0)
    Combo_day = customtkinter.CTkCombobox(frame_2,
                                          values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                                                  "14",
                                                  "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                                                  "26",
                                                  "27", "28", "29", "30", "31"])
    Combo_day.grid(row=5, column=0, pady=10)

    label_month = customtkinter.CTkLabel(frame_2, text="Month", font=font)
    label_month.grid(row=4, column=1)
    combo_month = customtkinter.CTkCombobox(frame_2,
                                            values=["January", "February", "March", "April", "May", "June", "July",
                                                    "August", "September", "October", "November", "December"])
    combo_month.grid(row=5, column=1, pady=10)

    label_year = customtkinter.CTkLabel(frame_2, text="Year", font=font)
    label_year.grid(row=4, column=2)
    entry_year = customtkinter.CTkEntry(frame_2, width=150)
    entry_year.grid(row=5, column=2, pady=10)

    label_age = customtkinter.CTkLabel(frame_2, text="Age", font=font)
    label_age.grid(row=6, column=0)
    entry_age = customtkinter.CTkEntry(frame_2, width=150)
    entry_age.grid(row=7, column=0, pady=10)

    label_email = customtkinter.CTkLabel(frame_2, text="Email", font=font)
    label_email.grid(row=6, column=1, pady=10)
    entry_email = customtkinter.CTkEntry(frame_2, width=150)
    entry_email.grid(row=7, column=1, pady=10)

    label_num = customtkinter.CTkLabel(frame_2, text="Phone Number", font=font)
    label_num.grid(row=6, column=2, pady=10)
    entry_num = customtkinter.CTkEntry(frame_2, width=150)
    entry_num.grid(row=7, column=2, pady=10)

    label_id = customtkinter.CTkLabel(frame_2, text="ID Card Type", font=font)
    label_id.grid(row=8, column=0, pady=10)
    combo_id = customtkinter.CTkCombobox(frame_2, values=["Ghana Card", "Passport", "Voters ID", "Institution ID",
                                                          "Drivers' License"])
    combo_id.grid(row=9, column=0, pady=10)

    label_idnum = customtkinter.CTkLabel(frame_2, text="ID Number", font=font)
    label_idnum.grid(row=8, column=1, pady=10)
    entry_idnum = customtkinter.CTkEntry(frame_2, width=150)
    entry_idnum.grid(row=9, column=1, pady=10)

    label_resi = customtkinter.CTkLabel(frame_2, text="Place of Residence", font=font)
    label_resi.grid(row=8, column=2, pady=10)
    entry_resi = customtkinter.CTkEntry(frame_2, width=150)
    entry_resi.grid(row=9, column=2, pady=10)

    label_gender = customtkinter.CTkLabel(frame_2, text="Gender", font=font)
    label_gender.grid(row=10, column=0, pady=10)
    combo_gender = customtkinter.CTkCombobox(frame_2, values=["Male", "Female", "Others"])
    combo_gender.grid(row=11, column=0, pady=10)

    label_blood = customtkinter.CTkLabel(frame_2, text="Work Category", font=font)
    label_blood.grid(row=10, column=1, pady=10)
    entry_cate = customtkinter.CTkEntry(frame_2, width=150)
    entry_cate.grid(row=11, column=1, pady=10)

    label_height = customtkinter.CTkLabel(frame_2, text="Height", font=font)
    label_height.grid(row=10, column=2, pady=10)
    entry_height = customtkinter.CTkEntry(frame_2, width=150)
    entry_height.grid(row=11, column=2, pady=10)

    btn_register = customtkinter.CTkButton(frame_2, text="Register", width=200, height=55, font=font_title,
                                           command=submit_nonhealth)
    btn_register.grid(row=12, column=0, columnspan=3, pady=30)


# Search Details
def searcd():
    search = customtkinter.CTkToplevel(window)
    search.geometry("850x797")
    search.title("Search and View Record")
    search.iconbitmap("pic.ico")

    my_bg = ImageTk.PhotoImage(Image.open("op.png"))
    lbl = customtkinter.CTkLabel(search, image=my_bg, text="")
    lbl.place(x=0, y=0, relwidth=1, relheight=1)

    def record1():
        root = customtkinter.CTkToplevel(search)
        root.title("All Patient Records")
        root.iconbitmap("pic.ico")
        root.geometry("800x500")
        root.configure(fg_color="#29b491")

        mycursor = my_connect.cursor()
        d = ttk.Treeview(root)

        d["columns"] = ("Patient ID", "First Name", "Middle Name", "Last Name", "Age", "Phone Number")

        # Format Columns
        d.column("#0", width=0)
        d.column("Patient ID", width=80)
        d.column("First Name", width=120)
        d.column("Middle Name", width=120)
        d.column("Last Name", width=120)
        d.column("Age", width=80)
        d.column("Phone Number", width=120)

        # Create Headings
        d.heading("#0", text="")
        d.heading("Patient ID", text="Patient ID")
        d.heading("First Name", text="First Name")
        d.heading("Middle Name", text="Middle Name")
        d.heading("Last Name", text="Last Name")
        d.heading("Age", text="Age")
        d.heading("Phone Number", text="Phone Number")

        # add data
        sql = "SELECT PID,First_Name, Middle_name, Last_name,Age,Phone_Number FROM Patients"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        count = 0

        for x in myresult:
            d.insert(parent="", index="end", iid=count, text="", values=(x[0], x[1], x[2], x[3], x[4], x[5],))
            count += 1

        d.pack(pady=20)

    def record2():
        root = customtkinter.CTkToplevel(search)
        root.title("All Health Staff Records")
        root.iconbitmap("pic.ico")
        root.geometry("800x500")
        root.configure(fg_color="#29b491")

        mycursor = my_connect.cursor()
        d = ttk.Treeview(root)

        d["columns"] = ("Health Staff ID", "First Name", "Middle Name", "Last Name", "Age", "Phone Number","Health Category")

        # Format Columns
        d.column("#0", width=0)
        d.column("Health Staff ID", width=80)
        d.column("First Name", width=120)
        d.column("Middle Name", width=120)
        d.column("Last Name", width=120)
        d.column("Age", width=80)
        d.column("Phone Number", width=120)
        d.column("Health Category", width=120)

        # Create Headings
        d.heading("#0", text="")
        d.heading("Health Staff ID", text="Health Staff ID")
        d.heading("First Name", text="First Name")
        d.heading("Middle Name", text="Middle Name")
        d.heading("Last Name", text="Last Name")
        d.heading("Age", text="Age")
        d.heading("Phone Number", text="Phone Number")
        d.heading("Health Category", text="Health Category")

        # add data
        sql = f"SELECT HID,First_Name, Middle_name, Last_name,Age,Phone_Number,Cate FROM H_Staff"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        count = 0

        for x in myresult:
            d.insert(parent="", index="end", iid=count, text="", values=(x[0], x[1], x[2], x[3], x[4], x[5],x[6]))
            count += 1

        d.pack(pady=20)

    def record3():
        root = customtkinter.CTkToplevel(search)
        root.title("All Non-Health Staff Records")
        root.iconbitmap("pic.ico")
        root.geometry("800x500")
        root.configure(fg_color="#29b491")

        mycursor = my_connect.cursor()
        d = ttk.Treeview(root)

        d["columns"] = (
        "Non-Health Staff ID", "First Name", "Middle Name", "Last Name", "Age", "Phone Number", "Non-Health Cat")

        # Format Columns
        d.column("#0", width=0)
        d.column("Non-Health Staff ID", width=80)
        d.column("First Name", width=120)
        d.column("Middle Name", width=120)
        d.column("Last Name", width=120)
        d.column("Age", width=80)
        d.column("Phone Number", width=120)
        d.column("Non-Health Cat", width=120)

        # Create Headings
        d.heading("#0", text="")
        d.heading("Non-Health Staff ID", text="Non-Health Staff ID")
        d.heading("First Name", text="First Name")
        d.heading("Middle Name", text="Middle Name")
        d.heading("Last Name", text="Last Name")
        d.heading("Age", text="Age")
        d.heading("Phone Number", text="Phone Number")
        d.heading("Non-Health Cat", text="Non-Health Cat")

        # add data
        sql = f"SELECT NHID,First_Name, Middle_name, Last_name,Age,Phone_Number,NonH_Cate FROM NonH_Staff"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        count = 0

        for x in myresult:
            d.insert(parent="", index="end", iid=count, text="", values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
            count += 1

        d.pack(pady=20)

    def search1():
        pid = entry_searchlname.get()
        sql = f"SELECT PID,First_Name, Middle_name, Last_name,Age,Phone_Number FROM Patients where PID = '{pid}'"
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()
        if not myresult:
            messagebox.showerror("Search Patient", "Record Not Found!")


        else:
            for x in myresult:
                messagebox.showinfo("Search Patients",
                                    f"PID: {x[0]} \n First name: {x[1]} \n Middle name: {x[2]} \n Last name: {x[3]} \n Age: {x[4]} \n Phone Number: {x[5]}")

        searcd()

    def search2():
        hid = entry_search_hlname.get()
        sql = f"SELECT HID,First_Name, Middle_name, Last_name,Age,Phone_Number,Cate FROM H_Staff where HID = '{hid}'"
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()
        if not myresult:
            messagebox.showerror("Search Health Staff Record", "Record Not Found!")


        else:
            for x in myresult:
                messagebox.showinfo("Search Patients",
                                    f"HID:{x[0]} \n First name: {x[1]} \n Middle name: {x[2]} \n Last name: {x[3]} \n Age: {x[4]} \n Phone Number{x[5]} \n Health Category: {x[6]}")
        searcd()

    def search3():
        nhid = entry_search_nhlname.get()
        sql = f"SELECT NHID,first_name,middle_name,last_name,age,phone_number,NonH_Cate FROM NonH_Staff where NHID = '{nhid}'"
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()
        if not myresult:
            messagebox.showerror("Search Non-Health Staff Record", "Record Not Found!")


        else:
            for x in myresult:
                messagebox.showinfo("Search Non-Health Staff Record",
                                    f"NHID: {x[0]} \n First name: {x[1]} \n Middle name: {x[2]} \n Last name: {x[3]} \n Age: {x[4]} \n Phone Number: {x[5]} \n Work Category: {x[6]}")

        searcd()

    frame_2 = customtkinter.CTkFrame(search, width=700, height=700, bg_color="#29b491", fg_color="#29b491")
    frame_2.pack(side="left")

    # Registration frame window
    label_top = customtkinter.CTkLabel(frame_2, text="Search Patient Record With ID", font=font_title)
    label_top.grid(row=0, column=0, columnspan=8, pady=10, padx=40)
    label_searchlname = customtkinter.CTkLabel(frame_2, text="PID", font=font)
    label_searchlname.grid(row=1, column=0, padx=40, pady=10)
    entry_searchlname = customtkinter.CTkEntry(frame_2, width=300)
    entry_searchlname.grid(row=1, column=1, padx=40, pady=10)
    btn_searchname = customtkinter.CTkButton(frame_2, text="SEARCH", width=160, height=40, command=search1)
    btn_searchname.grid(row=3, column=1, padx=10, pady=10)
    viewp = customtkinter.CTkButton(frame_2, text="View all Patient Records", font=font, width=160, height=40,
                                    command=record1)
    viewp.grid(row=3, column=2, padx=10, pady=10)

    label_top = customtkinter.CTkLabel(frame_2, text="Search Health Staff With ID", font=font_title)
    label_top.grid(row=4, column=0, columnspan=3, pady=10)
    label_search_hlname = customtkinter.CTkLabel(frame_2, text="HID", font=font)
    label_search_hlname.grid(row=5, column=0, padx=10, pady=10)
    entry_search_hlname = customtkinter.CTkEntry(frame_2, width=300)
    entry_search_hlname.grid(row=5, column=1, padx=10, pady=10)
    btn_searchname = customtkinter.CTkButton(frame_2, text="SEARCH", width=160, height=40, command=search2)
    btn_searchname.grid(row=7, column=1, padx=10, pady=10)
    viewhs = customtkinter.CTkButton(frame_2, text="View all Health Staff Records", font=font, width=160, height=40,command=record2)
    viewhs.grid(row=7, column=2, padx=10, pady=10)

    label_top = customtkinter.CTkLabel(frame_2, text="Search Non-Health Staff With ID", font=font_title)
    label_top.grid(row=8, column=0, columnspan=3, pady=10)
    label_search_nhlname = customtkinter.CTkLabel(frame_2, text="NHID", font=font)
    label_search_nhlname.grid(row=9, column=0, padx=10, pady=10)
    entry_search_nhlname = customtkinter.CTkEntry(frame_2, width=300)
    entry_search_nhlname.grid(row=9, column=1, padx=10, pady=10)
    btn_searchname = customtkinter.CTkButton(frame_2, text="SEARCH", width=160, height=40, command=search3)
    btn_searchname.grid(row=11, column=1, padx=10, pady=10)
    viewnhs = customtkinter.CTkButton(frame_2, text="View all Non-Health Staff Records", font=font, width=160,
                                      height=40,command=record3)
    viewnhs.grid(row=11, column=2, padx=10, pady=10)


# Delete Record
def delete_record():
    del_record = customtkinter.CTkToplevel(window)
    del_record.geometry("700x750")
    del_record.title("Delete Record")
    del_record.iconbitmap("pic.ico")

    my_bg = ImageTk.PhotoImage(Image.open("window.png"))
    lbl = customtkinter.CTkLabel(del_record, image=my_bg, text="")
    lbl.place(x=0, y=0, relwidth=1, relheight=1)

    def del1():
        pid = entry_delete_lname.get()
        sql = f"delete  FROM Patients where PID='{pid}'"
        my_cursor.execute(sql)
        my_connect.commit()
        messagebox.showinfo("Delete Record", "Record Successfully Deleted!")

    def del2():
        hid = entry_delete_hlname.get()
        sql = f"delete  FROM H_Staff where HID='{hid}'"
        my_cursor.execute(sql)
        my_connect.commit()
        messagebox.showinfo("Delete Record", "Record Successfully Deleted!")

    def del3():
        nhid = entry_delete_nhlname.get()
        sql = f"delete  FROM NonH_Staff where Last_name='{nhid}'"
        my_cursor.execute(sql)
        my_connect.commit()
        messagebox.showinfo("Delete Record", "Record Successfully Deleted!")

    frame_2 = customtkinter.CTkFrame(del_record, width=700, height=700, bg_color="#29b491", fg_color="#29b491")
    frame_2.pack(side="left")

    # Registration frame window
    label_top = customtkinter.CTkLabel(frame_2, text="Delete Patient With ID", font=font_title)
    label_top.grid(row=0, column=0, columnspan=8, pady=10, padx=40)
    label_deletelname = customtkinter.CTkLabel(frame_2, text="PID", font=font)
    label_deletelname.grid(row=1, column=0, padx=40, pady=10)
    entry_delete_lname = customtkinter.CTkEntry(frame_2, width=300)
    entry_delete_lname.grid(row=1, column=1, padx=40, pady=10)
    btn_deletename = customtkinter.CTkButton(frame_2, text="DELETE", width=160, height=40, command=del1)
    btn_deletename.grid(row=3, column=1, padx=10, pady=10)

    label_top = customtkinter.CTkLabel(frame_2, text="Delete Health Staff With HID", font=font_title)
    label_top.grid(row=4, column=0, columnspan=3, pady=10)
    label_delete_hlname = customtkinter.CTkLabel(frame_2, text="HID", font=font)
    label_delete_hlname.grid(row=5, column=0, padx=10, pady=10)
    entry_delete_hlname = customtkinter.CTkEntry(frame_2, width=300)
    entry_delete_hlname.grid(row=5, column=1, padx=10, pady=10)
    btn_deletename = customtkinter.CTkButton(frame_2, text="DELETE", width=160, height=40, command=del2)
    btn_deletename.grid(row=7, column=1, padx=10, pady=10)

    label_top = customtkinter.CTkLabel(frame_2, text="Delete Non-Health Staff With NHID", font=font_title)
    label_top.grid(row=8, column=0, columnspan=3, pady=10)
    label_search_nhlname = customtkinter.CTkLabel(frame_2, text="NHID", font=font)
    label_search_nhlname.grid(row=9, column=0, padx=10, pady=10)
    entry_delete_nhlname = customtkinter.CTkEntry(frame_2, width=300)
    entry_delete_nhlname.grid(row=9, column=1, padx=10, pady=10)
    btn_delete_name = customtkinter.CTkButton(frame_2, text="DELETE", width=160, height=40, command=del3)
    btn_delete_name.grid(row=11, column=1, padx=10, pady=10)


# Book Appointment
def book_app():
    b_app = customtkinter.CTkToplevel(window)
    b_app.geometry("600x400")
    b_app.title("Book Appointments")
    b_app.iconbitmap("pic.ico")

    my_bg = ImageTk.PhotoImage(Image.open("app.png"))
    lbl = customtkinter.CTkLabel(b_app, image=my_bg, text="")
    lbl.place(x=0, y=0, relwidth=1, relheight=1)

    frame_2 = customtkinter.CTkFrame(b_app, width=700, height=700, bg_color="#29b491", fg_color="#29b491")
    frame_2.pack(side="left")

    def confirm():
        date = cal.get_date()
        id = entry_forid.get()
        sql = f"SELECT First_Name, Middle_name, Last_name,Age,Phone_Number FROM Patients where PID = '{id}'"
        my_cursor.execute(sql)
        myresult = my_cursor.fetchall()
        if not myresult:
            messagebox.showerror("Book appointment", "Patient not in records. Can not book")



        else:
            messagebox.showinfo("Book Appointment", f"Your appointment for {date} is confirmed!")

        book_app()

    def get_date():
        global date
        global date_pick

        def cal_done():
            global date
            # date = cal.selection_get()

            # window.quit()
            lbl_date.configure(text="Selected Date is: " + cal.get_date(), font=font)
            top.withdraw()
            confirm_btn.configure(state="normal", command=confirm)

        top = customtkinter.CTkToplevel(b_app)
        top.title("Select Date")
        top.iconbitmap("pic.ico")
        top.geometry("600x400")
        global cal
        cal = Calendar(top, selectmode="day", locale="en_US", disabledforground="red", cursor=
        "hand2", background=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1],
                       selectbackground=customtkinter.ThemeManager.theme["CTkButton"]["fg_color"][1])
        cal.pack(fill="both", expand=True, padx=10, pady=10)
        # date = cal.selection_get()
        cal_btn = customtkinter.CTkButton(top, text="Select", font=font, command=cal_done)
        cal_btn.pack()

        # window.mainloop()

        # print("Your appointment date is", date)
        # return date

    # Registration frame window
    label_top = customtkinter.CTkLabel(frame_2, text="Book an Appointment", font=font_title)
    label_top.grid(row=0, column=0, columnspan=3, pady=10, padx=50)

    label_forid = customtkinter.CTkLabel(frame_2, text="Enter Patient ID", font=font)
    label_forid.grid(row=1, column=0, padx=120, pady=10)
    entry_forid = customtkinter.CTkEntry(frame_2, width=300)
    entry_forid.grid(row=2, column=0, padx=120, pady=10)

    label_docspec = customtkinter.CTkLabel(frame_2, text="Select Specialist", font=font)
    label_docspec.grid(row=3, column=0, padx=120, pady=10)
    combo_docspec = customtkinter.CTkCombobox(frame_2, width=300,
                                              values=["Consulting Doctor", "Dentist(Teeth)", "Pediatrician(Children)",
                                                      "Dermatologist(Skin)", "Ophthalmologist(Eye)", "Therapist",
                                                      "Pharmacist", "Dietitian(Food)"])
    combo_docspec.grid(row=4, column=0)

    label_date = customtkinter.CTkLabel(frame_2, text="Select a Date", font=font)
    label_date.grid(row=5, column=0, pady=10, padx=120)
    button_date = customtkinter.CTkButton(frame_2, text="Pick Date", font=font, width=300, command=get_date)
    button_date.grid(row=6, column=0)

    lbl_date = customtkinter.CTkLabel(frame_2, text="")
    lbl_date.grid(row=7, column=0, padx=120, pady=10)

    confirm_btn = customtkinter.CTkButton(frame_2, text="Confirm", font=font, width=300, state="disabled")
    confirm_btn.grid(row=8, column=0)


# Buttons on Main Page
button_1 = customtkinter.CTkButton(master=frame, width=300, height=50,
                                   text="REGISTER NEW PATIENTS", font=font, command=reg_patients)
button_1.grid(row=0, column=0, padx=130, pady=50)
button_1.grid_propagate(0)
button_2 = customtkinter.CTkButton(master=frame, width=300, height=50,
                                   text="REGISTER NEW HEALTH STAFF", font=font, command=reg_health)
button_2.grid(row=0, column=1, padx=130, pady=50)
button_2.grid_propagate(0)

button_3 = customtkinter.CTkButton(master=frame, width=300, height=50,
                                   text="REGISTER NON-HEALTH STAFF", font=font, command=reg_nonhealth)
button_3.grid(row=0, column=2, padx=130, pady=50)
button_3.grid_propagate(0)

button_4 = customtkinter.CTkButton(master=frame, width=300, height=50,
                                   text="SEARCH AND VIEW RECORDS", font=font, command=searcd)
button_4.grid(row=1, column=0, padx=40, pady=40)
button_4.grid_propagate(0)

button_5 = customtkinter.CTkButton(master=frame, width=300, height=50,
                                   text="DELETE A RECORD", font=font, command=delete_record)
button_5.grid(row=1, column=1, padx=40, pady=40)
button_5.grid_propagate(0)

button_6 = customtkinter.CTkButton(master=frame, width=300, height=50,
                                   text="BOOK AN APPOINTMENT", font=font, command=book_app)
button_6.grid(row=1, column=2, padx=40, pady=40)
button_6.grid_propagate(0)

window.mainloop()
