from email.mime import image
from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass

class CMS:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1350x700+0+0")
       self.root.title("Computer Shop Management System | Developed By SAM")
       self.root.config(bg = "white")
       #========== title =======#
       self.icon_title = PhotoImage(file = "images/logo2.png")
       title = Label(self.root, text = "Computer Shop Management system",image = self.icon_title,compound= LEFT,font = ("times new roman", 40, "bold"),bg = "#00599F", fg = "white", anchor= "w", padx = 20).place(x=0,y=0,relwidth=1, height = 70)

       #======== btn logout =====
       btn_logout = Button(self.root, text = "Logout", font = ("times new roman", 20, "bold"), bg = "yellow", padx = 10, pady= 10, cursor="hand2").place(x=1150,y= 10, height = 50, width = 150)

       #=========== clock ========

       self.btn_clock = Label(self.root, text = "Welcome to SAM Shop \t\t Date : DD-MM-YYYY\t\t Time: HH-MM-SS", font = ("times new roman", 15), bg = "#49616A", fg= "white")
       self.btn_clock.place(x=0, y=70, relwidth=1, height = 30)



       #=======Left Menu =======

       self.MenuLogo = Image.open("images/image1.png")
       self.MenuLogo = self.MenuLogo.resize((200,180))
       self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

       LeftMenu = Frame(self.root, bd = 2, relief= RIDGE, bg = "white")
       LeftMenu.place(x=0,y=102,width=200, height = 565)

       lbl_menuLogo = Label(LeftMenu, image = self.MenuLogo)
       lbl_menuLogo.pack(side = TOP, fill = X)

       
       self.employee_icon = PhotoImage(file = "images/indicator.png")
       self.supplier_icon = PhotoImage(file = "images/supplier.png")
       self.category_icon = PhotoImage(file = "images/category.png")
       self.product_icon = PhotoImage(file = "images/product.png")
       self.sale_icon = PhotoImage(file = "images/sale.png")
       self.exit_icon = PhotoImage(file = "images/exit.png")
       lbl_LeftBtn = Label(LeftMenu, text = "MENU", font = ("times new roman", 15), bg = "#005CA4", fg= "white").pack(side=TOP, fill = X)

       Btn_Employee = Button (LeftMenu, text = "Employee",command = self.employee,image = self.employee_icon, compound=LEFT,padx =1, anchor="w", cursor= "hand2", font = ("times new roman", 20,"bold"), bg = "white", fg= "black", bd = 3).pack(side=TOP, fill = X)
       Btn_Supplier = Button (LeftMenu, text = "Supplier",command = self.supplier,image = self.employee_icon, compound=LEFT,padx = 1, anchor="w", cursor= "hand2", font = ("times new roman", 20,"bold"), bg = "white", fg= "black", bd = 3).pack(side=TOP, fill = X)
       Btn_Category = Button (LeftMenu, text = "Category",command = self.category, image = self.employee_icon, compound=LEFT,padx = 1, anchor="w", cursor= "hand2", font = ("times new roman", 20,"bold"), bg = "white", fg= "black", bd = 3).pack(side=TOP, fill = X)
       Btn_Product = Button (LeftMenu, text = "Product",command = self.product, image = self.employee_icon, compound=LEFT,padx = 1, anchor="w", cursor= "hand2", font = ("times new roman", 20,"bold"), bg = "white", fg= "black", bd = 3).pack(side=TOP, fill = X)
       Btn_Sales = Button (LeftMenu, text = "Sales",command = self.sales, image = self.employee_icon, compound=LEFT,padx = 1, anchor="w", cursor= "hand2", font = ("times new roman", 20,"bold"), bg = "white", fg= "black", bd = 3).pack(side=TOP, fill = X)
       Btn_Exit = Button (LeftMenu, text = "Exit",image = self.employee_icon, compound=LEFT,padx = 1, anchor="w", cursor= "hand2", font = ("times new roman", 20,"bold"), bg = "white", fg= "black", bd = 3).pack(side=TOP, fill = X)




       #======== content section ======#
       self.lbl_employee = Label(self.root, text = "Total Employee \n [ 0 ] ",bd= 5, relief = RIDGE, font = ("times new roman", 20, "bold"),bg ="#49616A", fg= "white" )
       self.lbl_employee.place( x= 300,y=120, height = 150, width = 300)

       self.lbl_supplier = Label(self.root, text = "Total Supplier \n [ 0 ] ",bd= 5, relief = RIDGE, font = ("times new roman", 20, "bold"),bg ="#49616A", fg= "white" )
       self.lbl_supplier.place( x= 650,y=120, height = 150, width = 300)

       self.lbl_category = Label(self.root, text = "Total Category \n [ 0 ] ",bd= 5, relief = RIDGE, font = ("times new roman", 20, "bold"),bg ="#49616A", fg= "white" )
       self.lbl_category.place( x= 1000,y=120, height = 150, width = 300)

       self.lbl_product = Label(self.root, text = "Total Product \n [ 0 ] ",bd= 5, relief = RIDGE, font = ("times new roman", 20, "bold"),bg ="#49616A", fg= "white" )
       self.lbl_product.place( x= 300,y=300, height = 150, width = 300)

       self.lbl_sales = Label(self.root, text = "Total Sales \n [ 0 ] ",bd= 5, relief = RIDGE, font = ("times new roman", 20, "bold"),bg ="#49616A", fg= "white" )
       self.lbl_sales.place( x= 650,y=300, height = 150, width = 300)


       #======== footer section ===========#

       btn_footer = Label(self.root, text = "SAM- Computer Shop | Developed by ST \n For any query contact 01778647982", font = ("times new roman", 12), bg = "#49616A", fg= "white").pack(side = BOTTOM, fill = X )


    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)


    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)



if __name__=="__main__":
    root = Tk()
    obj = CMS(root)
    root.mainloop()