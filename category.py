from email import message
from platform import release
from tkinter import*
from tkinter import messagebox
from tokenize import String
from turtle import width
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Employee Management")
        self.root.focus_force()


        #+======= variables ======#
        self.var_cat_id = StringVar()
        self.var_name = StringVar()


#==========Title =====================#

        lbl_title = Label(self.root, text = "Manage Product Category", font = ("goudy old style", 30, "bold"), bg = "#007ACC", fg = "white", border = 2, relief=RIDGE)
        lbl_title.pack(side = TOP, fill = X, padx = 10, pady = 20)

        lbl_name = Label(self.root, text = "Enter category Name", font = ("goudy old style", 30), bg = "white")
        lbl_name.place(x=50, y=100)

        txt_name = Entry(self.root, textvariable =self.var_name, font= ("goudy old style", 18) , bg = "lightyellow")
        txt_name.place(x=50, y= 170)

        btn_add =Button(self.root, text = "ADD", font= ("goudy old style", 15) , bg = "#007ACC", fg = "white", cursor = "hand2")
        btn_add.place(x=350, y= 170, width = 150, height = 30)


        btn_delete =Button(self.root, text = "Delete", font= ("goudy old style", 15) , bg = "#007ACC", fg = "white", cursor = "hand2")
        btn_delete.place(x=520, y= 170, width = 150, height = 30)
    

        ## ======== Employeee details ========###

        cat_frame = Frame(self.root, bd = 3, relief = RIDGE)
        cat_frame.place(x=680, y=100, width = 400, height = 100)

        scrolly = Scrollbar(cat_frame, orient = VERTICAL)
        scrollx = Scrollbar(cat_frame, orient = HORIZONTAL)

        self.category_table = ttk.Treeview(cat_frame, columns = ("cid", "name"), yscrollcommand = scrolly.set, xscrollcommand= scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)

        scrollx.config(command= self.category_table.xview)
        scrolly.config(command = self.category_table.yview)


        self.category_table.heading("cid", text = "C ID")
        self.category_table.heading("name", text = "Name")

        self.category_table["show"] = "headings"

        self.category_table.column("cid",width = 90)
        self.category_table.column("name",width = 100 )
        self.category_table.pack(fill = BOTH, expand = 1)



#==============imagesss =================#
        self.im1 = Image.open("images/imac2020.jpg")
        self.im1 = self.im1.resize((500,270), Image.ANTIALIAS)
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image = self.im1, bd = 2, relief= RAISED)
        self.lbl_im1.place(x= 50, y=220)




        self.im2 = Image.open("images/ROG_TYTAN_CG8480.jpg")
        self.im2 = self.im2.resize((500,270), Image.ANTIALIAS)
        self.im2 = ImageTk.PhotoImage(self.im2)

        self.lbl_im2 = Label(self.root, image = self.im2, bd = 2, relief= RAISED)
        self.lbl_im2.place(x= 580, y=220)







if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()