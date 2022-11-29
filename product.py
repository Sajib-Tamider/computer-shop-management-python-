from email import message
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Employee Management")
        self.root.focus_force()


        #=========variables ===========

        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        self.var_searchby = StringVar(),
        self.var_txt = StringVar(),



        #=================================

        product_Frame = Frame(self.root, bd =2, relief = RIDGE, bg = "white")
        product_Frame.place(x=10,y= 10, width = 450, height = 480)

        # =================title =============
        product_title = Label(product_Frame, text = "Manage Product Details", font = ("goudy old style", 18, "bold"), bg = "#007ACC", fg  = "white")
        product_title.pack(side = TOP, fill = X)


        lbl_category = Label(product_Frame, text = "Category", font = ("goudy old style", 18, "bold"), bg  = "white")
        lbl_category.place(x=30, y=40)

        lbl_supplier = Label(product_Frame, text = "Supplier", font = ("goudy old style", 18, "bold"), bg  = "white")
        lbl_supplier.place(x=30, y=90)

        lbl_product_name = Label(product_Frame, text = "Name", font = ("goudy old style", 18, "bold"), bg  = "white")
        lbl_product_name.place(x=30, y=140)

        lbl_price = Label(product_Frame, text = "Price", font = ("goudy old style", 18, "bold"), bg  = "white")
        lbl_price.place(x=30, y=190)

        lbl_quantity = Label(product_Frame, text = "Quantity", font = ("goudy old style", 18, "bold"), bg  = "white")
        lbl_quantity.place(x=30, y=230)

        lbl_status = Label(product_Frame, text = "Status", font = ("goudy old style", 18, "bold"), bg  = "white")
        lbl_status.place(x=30, y=280)


        # txt_category = Label(product_Frame, text = "Manage Product Details", font = ("goudy old style", 18, "bold"), bg = "#007ACC", fg  = "white")
        # txt_category.pack(side = TOP, fill = X)

        #================options ====================

        cmb_cat = ttk.Combobox(product_Frame,textvariable = self.var_cat, values=("Select"), state="readonly", justify= CENTER,font=("times new roman",15))
        cmb_cat.place(x=150,y=40,width = 200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame,textvariable = self.var_sup, values=("Select"), state="readonly", justify= CENTER,font=("times new roman",15))
        cmb_sup.place(x=150,y=90,width = 200)
        cmb_sup.current(0)

        txt_name = Entry(product_Frame,textvariable = self.var_name, font=("times new roman",15), bg = "lightyellow")
        txt_name.place(x=150,y=140,width = 200)

        txt_price = Entry(product_Frame,textvariable = self.var_price, font=("times new roman",15), bg = "lightyellow")
        txt_price.place(x=150,y=190,width = 200)


        txt_quantity = Entry(product_Frame,textvariable = self.var_qty, font=("times new roman",15), bg = "lightyellow")
        txt_quantity.place(x=150,y=230,width = 200)


        cmb_status = ttk.Combobox(product_Frame,textvariable = self.var_status, values=("Active","Inactive"), state="readonly", justify= CENTER,font=("times new roman",15))
        cmb_status.place(x=150,y=280,width = 200)
        cmb_status.current(0)

        #===============Buttons =================

        btn_save = Button(product_Frame, text = "Save", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#007ACC", fg="white")
        btn_save.place(x=10, y=400, width = 100, height=30)

        btn_update = Button(product_Frame, text = "Update", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#439D4A", fg="white")
        btn_update.place(x=120, y=400, width = 100, height=30)

        btn_delete = Button(product_Frame, text = "Delete", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#FF5131", fg="white")
        btn_delete.place(x=230, y=400, width = 100, height=30)

        btn_clear = Button(product_Frame, text = "Clear", font=("goudy old style",14,"bold"),cursor= "hand2", bg= "#5D7A88", fg="white")
        btn_clear.place(x=340, y=400, width = 100, height=30)


        #===============SearchFrame================#

        SearchFrame = LabelFrame(self.root, text = "Search Product", font = ("times new roamn", 12,"bold"), bd=2, relief=RIDGE,bg = "white")
        SearchFrame.place(x=480,y=10, width=600,height=80)

        #=========Option seciton=========#

        cmb_search = ttk.Combobox(SearchFrame,values=("Select","Category","Supplier","Name"), textvariable=self.var_searchby, state="readonly", justify= CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10, width=180)
        cmb_search.current(0)

        text_search = Entry(SearchFrame,textvariable=self.var_txt,font=("goudy old style",15), bg="lightblue")
        text_search.place(x=200,y=10)

        btn_search = Button(SearchFrame, text = "Search", font=("times new roman",14,"bold"),cursor= "hand2", bg= "#007ACC", fg="white")
        btn_search.place(x=410, y=8, width = 148, height=28)


        ## ======== Product  details ========###

        prod_frame = Frame(self.root, bd = 3, relief = RIDGE)
        prod_frame.place(x=480, y=100, width = 600, height = 390)

        scrolly = Scrollbar(prod_frame, orient = VERTICAL)
        scrollx = Scrollbar(prod_frame, orient = HORIZONTAL)

        self.product_table = ttk.Treeview(prod_frame, columns = ("eid", "name", "email", "gender", "contact","dob","doj", "utype", "address", "salary"), yscrollcommand = scrolly.set, xscrollcommand= scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)

        scrollx.config(command= self.product_table.xview)
        scrolly.config(command = self.product_table.yview)


        self.product_table.heading("eid", text = "P ID")
        self.product_table.heading("name", text = "Name")
        self.product_table.heading("email", text = "Email")
        self.product_table.heading("gender", text = "Gender")
        self.product_table.heading("contact", text = "Contact")
        self.product_table.heading("dob", text = "DOB")
        self.product_table.heading("doj", text = "DOJ")
        self.product_table.heading("utype", text = "Type")
        self.product_table.heading("address", text = "Address")
        self.product_table.heading("salary", text = "Salary")

        self.product_table["show"] = "headings"

        self.product_table.column("eid",width = 90)
        self.product_table.column("name",width = 100 )
        self.product_table.column("email", width = 100)
        self.product_table.column("gender", width = 100)
        self.product_table.column("contact", width = 100)
        self.product_table.column("dob", width = 100)
        self.product_table.column("doj", width = 100)
        self.product_table.column("utype", width = 100)
        self.product_table.column("address", width = 100)
        self.product_table.column("salary", width = 100)


        self.product_table.pack(fill = BOTH, expand = 1)





if __name__=="__main__":
    root = Tk()
    obj =productClass(root)
    root.mainloop()