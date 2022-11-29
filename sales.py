from email import message
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class salesClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Employee Management")
        self.root.focus_force()

        self.var_invoice = StringVar()

        #=====title =================#

        lbl_title = Label(self.root, text = "View Customer Bills", font = ("goudy old style", 30, "bold"), bg = "#007ACC", fg = "white", border = 2, relief=RIDGE)
        lbl_title.pack(side = TOP, fill = X, padx = 10, pady = 20)


        lbl_invoice = Label(self.root, text = "Invoice NO", font = ("times new roman",15), bg = "white")
        lbl_invoice.place(x=40, y=100)

        
        txt_invoice = Entry(self.root, textvariable= self.var_invoice, font = ("times new roman",15), bg = "lightyellow")
        txt_invoice.place(x=160, y=100, width = 180, height = 28)

        btn_search = Button(self.root, text = "search", cursor = "hand2",font = ("times new roman", 15, "bold"), bg = "#007ACC", fg = "white")
        btn_search.place(x=360, y = 100, width = 120, height = 28)

        btn_search = Button(self.root, text = "clear", cursor = "hand2",font = ("times new roman", 15, "bold"), bg = "#007ACC", fg = "white")
        btn_search.place(x=480, y = 100, width = 120, height = 28)


        #====== Bill List ========#

        sales_Frame = Frame(self.root, bd = 3, relief = RIDGE)
        sales_Frame.place(x=50, y=140, width = 200, height = 330)

        scrolly= Scrollbar(sales_Frame, orient = VERTICAL)
        self.Sales_List = Listbox(sales_Frame, font=("goudy old style",15), bg = "white")
        scrolly.pack(side = RIGHT, fill=Y)
        scrolly.config(command = self.Sales_List.yview)
        self.Sales_List.pack(fill = BOTH, expand=1)


        #======  Bill List =========#
        bill_Frame = Frame(self.root, bd = 3, relief = RIDGE)
        bill_Frame.place(x=280, y=140, width = 410, height = 330)


        lbl_title2 = Label(bill_Frame, text = "Customer Bill Area", font = ("goudy old style", 20, "bold"), bg = "blue", fg = "white", border = 2, relief=RIDGE)
        lbl_title2.pack(side = TOP, fill = X, )

        scrolly2= Scrollbar(bill_Frame, orient = VERTICAL)
        self.bill_area = Text(bill_Frame, font=("goudy old style",15), bg = "lightyellow")
        scrolly2.pack(side = RIGHT, fill=Y)
        scrolly2.config(command = self.bill_area.yview)
        self.bill_area.pack(fill = BOTH, expand=1)



        #==============image==========#

        self.bill_photo = Image.open("images/arena.jpg")
        self.bill_photo = self.bill_photo.resize((450,285),Image.ANTIALIAS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        lbl_image = Label(self.root, image = self.bill_photo)
        lbl_image.place(x=700, y = 110)



if __name__=="__main__":
    root = Tk()
    obj =salesClass(root)
    root.mainloop()