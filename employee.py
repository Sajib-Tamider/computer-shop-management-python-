from email import message
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Employee Management")
        self.root.focus_force()


        #=======All variables ====================#

        self.var_searchby = StringVar(),
        self.var_txt = StringVar(),

        self.var_emp_id = StringVar(),
        self.var_gender = StringVar(),
        self.var_contact = StringVar(),
        self.var_name = StringVar(),
        self.var_dob = StringVar(),
        self.var_doj = StringVar(),
        self.var_email = StringVar(),
        self.var_utype = StringVar(),
        
        self.var_pass = StringVar(),
        self.var_sal = StringVar(),
        self.text_address = StringVar(),
        self.var_add = StringVar(),

        #===============SearchFrame================#

        SearchFrame = LabelFrame(self.root, text = "Search Employee", font = ("times new roamn", 12,"bold"), bd=2, relief=RIDGE,bg = "white")
        SearchFrame.place(x=250,y=20, width=600,height=70)

        #=========Option seciton=========#

        cmb_search = ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact"), textvariable=self.var_searchby, state="readonly", justify= CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10, width=180)
        cmb_search.current(0)

        text_search = Entry(SearchFrame,textvariable=self.var_txt,font=("goudy old style",15), bg="lightblue")
        text_search.place(x=200,y=10)

        btn_search = Button(SearchFrame, text = "Search", font=("times new roman",14,"bold"),cursor= "hand2", bg= "#007ACC", fg="white")
        btn_search.place(x=410, y=8, width = 148, height=28)


        #=======title ==============#

        below_search_title = Label(self.root, text="Employee Details", font=("goudy old style", 15), bg= "#007ACC", fg= "white")
        below_search_title.place(x=50, y=100, width= 1000)

        #=========Employee contact ===========#

        #===========Row1===================#

        lbl_emp_id = Label(self.root, text="Emp-Id",font=("times new roman", 15), bg= "white")
        lbl_emp_id.place(x=50,y=150)

        lbl_gender = Label(self.root, text="Gender",font=("times new roman", 15), bg= "white")
        lbl_gender.place(x=390,y=150)

        lbl_contact = Label(self.root, text="Contact",font=("times new roman", 15), bg= "white")
        lbl_contact.place(x=750,y=150)

        txt_emp_id = Entry(self.root, textvariable=self.var_emp_id,font=("times new roman", 15), bg= "#ADD8E6")
        txt_emp_id.place(x=150,y=150,width= 170)

        # txt_gender = Entry(self.root, textvariable=self.var_gender,font=("times new roman", 15), bg= "white")
        # txt_gender.place(x=500,y=150,width= 170)

        txt_gender_cmb = ttk.Combobox(self.root,values=("Select","Male","Female","Others"), textvariable=self.var_gender, state="readonly", justify= CENTER,font=("times new roman",15))
        txt_gender_cmb.place(x=500,y=150, width=170)
        txt_gender_cmb.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact,font=("times new roman", 15), bg= "#ADD8E6")
        txt_contact.place(x=850,y=150,width= 200)




        #===========Row2===================#

        lbl_emp_name = Label(self.root, text="Name",font=("times new roman", 15), bg= "white")
        lbl_emp_name.place(x=50,y=190)

        lbl_dob = Label(self.root, text="D.O.B",font=("times new roman", 15), bg= "white")
        lbl_dob.place(x=390,y=190)

        lbl_doj = Label(self.root, text="D.O.J",font=("times new roman", 15), bg= "white")
        lbl_doj.place(x=750,y=190)

        txt_emp_name = Entry(self.root, textvariable=self.var_name,font=("times new roman", 15), bg= "#ADD8E6")
        txt_emp_name.place(x=150,y=190,width= 170)



        txt_dob = Entry(self.root, textvariable=self.var_dob,font=("times new roman", 15), bg= "#ADD8E6")
        txt_dob.place(x=500,y=190,width= 170)

        # txt_gender_cmb = ttk.Combobox(self.root,values=("Select","Male","Female","Others"), textvariable=self.var_gender, state="readonly", justify= CENTER,font=("times new roman",15))
        # txt_gender_cmb.place(x=500,y=200, width=170)
        # txt_gender_cmb.current(0)

        txt_doj = Entry(self.root, textvariable=self.var_doj,font=("times new roman", 15), bg= "#ADD8E6")
        txt_doj.place(x=850,y=190,width= 200)


        #===========Row3===================#

        lbl_emp_email = Label(self.root, text="Email",font=("times new roman", 15), bg= "white")
        lbl_emp_email.place(x=50,y=230)

        lbl_password = Label(self.root, text="Password",font=("times new roman", 15), bg= "white")
        lbl_password.place(x=390,y=230)

        lbl_utype = Label(self.root, text="User Type",font=("times new roman", 15), bg= "white")
        lbl_utype.place(x=750,y=230)

        txt_emp_email = Entry(self.root, textvariable=self.var_email,font=("times new roman", 15), bg= "#ADD8E6")
        txt_emp_email.place(x=150,y=230,width= 170)

        txt_password = Entry(self.root, textvariable=self.var_pass,font=("times new roman", 15), bg= "#ADD8E6")
        txt_password.place(x=500,y=230,width= 170)

        txt_utype_cmb = ttk.Combobox(self.root,values=("Select","Admin","Employee"), textvariable=self.var_utype, state="readonly", justify= CENTER,font=("times new roman",15))
        txt_utype_cmb.place(x=850,y=230,width= 200)
        txt_utype_cmb.current(0)


        # #================== Row4 ====================#

        lbl_address= Label(self.root, text="Address",font=("times new roman", 15), bg= "white")
        lbl_address.place(x=50,y=270)

        lbl_salary = Label(self.root, text="Salary",font=("times new roman", 15), bg= "white")
        lbl_salary.place(x=500,y=270)

        self.txt_address = Text(self.root, font=("times new roman", 15), bg= "#ADD8E6")
        self.txt_address.place(x=150,y=270,width= 300,height = 60 )

        txt_salary = Entry(self.root, textvariable = self.var_sal,font=("times new roman", 15), bg= "#ADD8E6")
        txt_salary.place(x=600,y=270,width= 170)


        # #======== buttons ============#

        btn_save = Button(self.root, text = "Save", command = self.add, font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#007ACC", fg="white")
        btn_save.place(x=500, y=305, width = 110, height=28)

        btn_update = Button(self.root, text = "Update", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#439D4A", fg="white")
        btn_update.place(x=620, y=305, width = 110, height=28)

        btn_delete = Button(self.root, text = "Delete", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#FF5131", fg="white")
        btn_delete.place(x=740, y=305, width = 110, height=28)

        btn_clear = Button(self.root, text = "Clear", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#5D7A88", fg="white")
        btn_clear.place(x=860, y=305, width = 110, height=28)



        ## ======== Employeee details ========###

        emp_frame = Frame(self.root, bd = 3, relief = RIDGE)
        emp_frame.place(x=0, y=350, relwidth = 1, height = 150)

        scrolly = Scrollbar(emp_frame, orient = VERTICAL)
        scrollx = Scrollbar(emp_frame, orient = HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns = ("eid", "name", "email", "gender", "contact","dob","doj", "utype", "address", "salary"), yscrollcommand = scrolly.set, xscrollcommand= scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)

        scrollx.config(command= self.EmployeeTable.xview)
        scrolly.config(command = self.EmployeeTable.yview)


        self.EmployeeTable.heading("eid", text = "EMP ID")
        self.EmployeeTable.heading("name", text = "Name")
        self.EmployeeTable.heading("email", text = "Email")
        self.EmployeeTable.heading("gender", text = "Gender")
        self.EmployeeTable.heading("contact", text = "Contact")
        self.EmployeeTable.heading("dob", text = "DOB")
        self.EmployeeTable.heading("doj", text = "DOJ")
        self.EmployeeTable.heading("utype", text = "Type")
        self.EmployeeTable.heading("address", text = "Address")
        self.EmployeeTable.heading("salary", text = "Salary")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid",width = 90)
        self.EmployeeTable.column("name",width = 100 )
        self.EmployeeTable.column("email", width = 100)
        self.EmployeeTable.column("gender", width = 100)
        self.EmployeeTable.column("contact", width = 100)
        self.EmployeeTable.column("dob", width = 100)
        self.EmployeeTable.column("doj", width = 100)
        self.EmployeeTable.column("utype", width = 100)
        self.EmployeeTable.column("address", width = 100)
        self.EmployeeTable.column("salary", width = 100)


        self.EmployeeTable.pack(fill = BOTH, expand = 1)




#===============================================================================
    # def add(self):
    #     con = sqlite3.connect(database= r'ims.db')
    #     cur = con.cursor()

    #     try:
    #         if self.var_emp_id.get()==" ":
    #             messagebox.showerror("Error", "Employee ID Must be required", parent = root)

    #         else:
    #             cur.execute("Select * from employee where eid = ?",(self.var_emp_id.get(),))


    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error to : {str(ex)}")    

# #===========================================================================#
    def add(self):
        con = sqlite3.connect(database= r'ims.db')
        cur = con.cursor()
        try: 
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent = self.root)
            
            else:
                cur.execute("Select * from employee where eid = ?", (self.var_emp_id.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "This Employee ID already assigned, try another one", parent = self.root)

                else: 
                    cur.execute("Insert into employee (eid, name, email, gender, contact, dob, doj, utype, address, salary) values(?,?,?,?,?,?,?,?,?,?)",(
                                    self.var_emp_id.get(),
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_utype.get(),
                                    self.text_address.get('1.0',END),
                                    self.var_sal.get(),
                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent = self.root)



        except Exception as ex: 
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent = self.root)

         


if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()