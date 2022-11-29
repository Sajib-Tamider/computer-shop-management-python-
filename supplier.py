from email import message
from tkinter import*
from tkinter import messagebox
from turtle import width
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Employee Management")
        self.root.focus_force()


        #=======All variables ====================#

        self.var_searchby = StringVar(),
        self.var_txt = StringVar(),

        self.var_sup_invoice = StringVar(),
        self.var_name = StringVar(),
        self.var_contact = StringVar(),
        

        #===============SearchFrame================#

        # SearchFrame = LabelFrame(self.root, text = "Search Employee", font = ("times new roamn", 12,"bold"), bd=2, relief=RIDGE,bg = "white")
        # #SearchFrame.place(x=250,y=20, width=600,height=70)

        #=========Option seciton=========#

        # cmb_search = ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact"), textvariable=self.var_searchby, state="readonly", justify= CENTER,font=("times new roman",15))
        # cmb_search.place(x=10,y=10, width=180)
        # cmb_search.current(0)

        lbl_search = Label(self.root, text = "Invoice No", bg = "white", font = ("goudy old style", 15, "bold"))
        lbl_search.place(x = 650, y = 50)

        text_search = Entry(self.root,textvariable=self.var_txt,font=("goudy old style",15), bg="lightblue")
        text_search.place(x=750,y=50, width = 150)

        btn_search = Button(self.root, text = "Search", font=("times new roman",14,"bold"),cursor= "hand2", bg= "#007ACC", fg="white")
        btn_search.place(x=910, y=50, width = 140, height=28)


        #=======title ==============#

        below_search_title = Label(self.root, text="Supplier Details", font=("goudy old style", 15,"bold"), bg= "#007ACC", fg= "white")
        below_search_title.place(x=50, y=10, width= 1000)

        #=========Employee contact ===========#

        #===========Row1===================#

        lbl_supplier_invoice = Label(self.root, text="Invoice No. ",font=("times new roman", 15), bg= "white")
        lbl_supplier_invoice.place(x=50,y=50)

        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice,font=("times new roman", 15), bg= "#ADD8E6")
        txt_supplier_invoice.place(x=150,y=50,width= 170)





        #===========Row2===================#

        lbl_emp_name = Label(self.root, text="Name",font=("times new roman", 15), bg= "white")
        lbl_emp_name.place(x=50,y=95)

        txt_emp_name = Entry(self.root, textvariable=self.var_name,font=("times new roman", 15), bg= "#ADD8E6")
        txt_emp_name.place(x=150,y=95,width= 170)


        #===========Row3===================#

        lbl_contact = Label(self.root, text="Contact",font=("times new roman", 15), bg= "white")
        lbl_contact.place(x=50,y=135)

        txt_contact = Entry(self.root, textvariable=self.var_contact,font=("times new roman", 15), bg= "#ADD8E6")
        txt_contact.place(x=150,y=135,width= 170)



        # #================== Row4 ====================#

        lbl_description= Label(self.root, text="Description",font=("times new roman", 15), bg= "white")
        lbl_description.place(x=50,y=170)

        self.txt_description = Text(self.root, font=("times new roman", 15), bg= "#ADD8E6")
        self.txt_description.place(x=150,y=170,width= 300,height = 60 )



        # #======== buttons ============#

        btn_save = Button(self.root, text = "Save", command = self.add, font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#007ACC", fg="white")
        btn_save.place(x=50, y=360, width = 130, height=28)

        btn_update = Button(self.root, text = "Update", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#439D4A", fg="white")
        btn_update.place(x=160, y=360, width = 130, height=28)

        btn_delete = Button(self.root, text = "Delete", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#FF5131", fg="white")
        btn_delete.place(x=270, y=360, width = 130, height=28)

        btn_clear = Button(self.root, text = "Clear", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#5D7A88", fg="white")
        btn_clear.place(x=380, y=360, width = 130, height=28)



        ## ======== Employeee details ========###

        emp_frame = Frame(self.root, bd = 3, relief = RIDGE)
        emp_frame.place(x=650, y=90, width = 400, height = 400)

        scrolly = Scrollbar(emp_frame, orient = VERTICAL)
        scrollx = Scrollbar(emp_frame, orient = HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns = ("invoice", "name", "contact", "desc"), yscrollcommand = scrolly.set, xscrollcommand= scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)

        scrollx.config(command= self.supplierTable.xview)
        scrolly.config(command = self.supplierTable.yview)


        self.supplierTable.heading("invoice", text = "Invoice No")
        self.supplierTable.heading("name", text = "Name")
        self.supplierTable.heading("contact", text = "Email")
        self.supplierTable.heading("desc", text = "Gender")

        self.supplierTable["show"] = "headings"

        self.supplierTable.column("invoice",width = 90)
        self.supplierTable.column("name",width = 100 )
        self.supplierTable.column("contact", width = 100)
        self.supplierTable.column("desc", width = 100)


        self.supplierTable.pack(fill = BOTH, expand = 1)




#===============================================================================
    # def add(self):
    #     con = sqlite3.connect(database= r'ims.db')
    #     cur = con.cursor()

    #     try:
    #         if self.var_sup_invoice.get()==" ":
    #             messagebox.showerror("Error", "Employee ID Must be required", parent = root)

    #         else:
    #             cur.execute("Select * from employee where eid = ?",(self.var_sup_invoice.get(),))


    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error to : {str(ex)}")    

# #===========================================================================#
    def add(self):
        con = sqlite3.connect(database= r'ims.db')
        cur = con.cursor()
        try: 
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No must be required", parent = self.root)
            
            else:
                cur.execute("Select * from supplier where invoice = ?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "This Invoice already assigned, try another one", parent = self.root)

                else: 
                    cur.execute("Insert into supplier (invoice, name, contact, desc) values(?,?,?,?)",(
                                    self.var_sup_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_description.get('1.0', END),
                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent = self.root)



        except Exception as ex: 
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent = self.root)

         


if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()