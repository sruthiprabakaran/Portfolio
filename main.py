
from tkinter import *
from tkinter import messagebox
import datetime
import math , random , os
class Bill:
    
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Page")
        
        title = Label(self.root,text="Billing Page",bd=12,relief=GROOVE,bg="gray",fg="white",font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)

        labelframe = LabelFrame(root, text="Daily Load",bd=10,relief=GROOVE,font=("Times New Roman",15,"bold"),bg="cyan",fg="white")
        labelframe.place(x=500,y=100,relwidth=1)

        #========variables=============================================

        self.cust_name = StringVar()
        self.cust_phone = StringVar()
        x=random.randint(1000,9999)
        self.cust_bill = StringVar()
        self.cust_bill.set(str(x))
        self.search = StringVar()
        self.Vegie_stock = StringVar()
        self.Vegie_qnty = StringVar()

        self.carrot_available = IntVar()
        self.onion_available = IntVar()
        self.tomato_available = IntVar()
        self.cabbage_available = IntVar()
        self.cauliflr_available = IntVar()
        self.chilli_available = IntVar()
        self.potato_available = IntVar()
        self.beans_available = IntVar()


        self.carrot = IntVar()
        self.onion = IntVar()
        self.tomato = IntVar()
        self.cabbage = IntVar()
        self.cauliflr = IntVar()
        self.chilli = IntVar()
        self.potato = IntVar()
        self.beans = IntVar()

        self.tot_amount = StringVar()
        self.tot_tax = StringVar()



        #===========customer details frame===============================================================================

        customer = LabelFrame(root, text="Customer Details", bd=10,relief=GROOVE, font=("Times new roman",15,"bold"),bg="indigo",fg="white")
        customer.place(x=0,y=180,relwidth=1)

        cname = Label(customer, text="Customer Name",font=("times new roman",15,"bold"),bg="indigo",fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_entry = Entry(customer,textvariable = self.cust_name, bd =8,bg="indigo",fg="white").grid(row=0,column=1)

        cphone = Label(customer, text="Customer Mobile",font=("times new roman",15,"bold"),bg="indigo",fg="white").grid(row=0,column=2,padx=20,pady=5)
        cphone_entry = Entry(customer,textvariable=self.cust_phone ,bd =8,bg="indigo",fg="white").grid(row=0,column=3)

        cbill = Label(customer, text="Customer Bill No",font=("times new roman",15,"bold"),bg="indigo",fg="white").grid(row=0,column=4,padx=20,pady=5)
        cbill_entry = Entry(customer,textvariable=self.cust_bill , bd =8,bg="indigo",fg="white").grid(row=0,column=5)

        csearch = Button(customer,text="Search",font=("Times new roman",10,"bold"),bg="gray",fg="white",command=self.find_bill).grid(row=0,column=6,padx=4,pady=2)

        stock = Button(customer,text="Stock",font=("Times new roman",10,"bold"),bg="gray",fg="white",command=self.new_entry).grid(row=0,column=7,padx=4,pady=2)
        

        customer.pack(fill=X)
        #===============Availability frame==================================================================

        stockinmarket = LabelFrame(root, text="Available Stock",relief=GROOVE,bd=10,font=("Times New Roman",15,"bold"),bg="indigo",fg="white")
        stockinmarket.place(x=0,y=140,width=350,height=500)

        Vegie_lbl=Label(stockinmarket ,text="Vegetable",font=("times new roman",20,"bold"),bg="indigo",fg="white").grid(row=0,column=0,padx=20,pady=5)
        Vegie_qnty = Label(stockinmarket, text="Quantity", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=0, column=1, padx=20, pady=5)

        Carrot_lbl = Label(stockinmarket, text="Carrot",font=("times new roman",20,"bold"),bg="indigo",fg="white").grid(row=1,column=0,padx=20,pady=5)
        Carrot_entry = Entry(stockinmarket,width=10,textvariable=self.carrot_available , bd =8,bg="indigo",fg="white").grid(row=1,column=1)

        Onion_lbl = Label(stockinmarket, text="Onion", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=2, column=0, padx=20, pady=5)
        Onion_entry = Entry(stockinmarket,width=10, textvariable=self.onion_available, bd=8, bg="indigo", fg="white").grid(row=2, column=1)

        Tomato_lbl = Label(stockinmarket, text="Tomato", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=3, column=0, padx=20, pady=5)
        Tomato_entry = Entry(stockinmarket,width=10, textvariable=self.tomato_available, bd=8, bg="indigo", fg="white").grid(row=3, column=1)

        Cabbage_lbl = Label(stockinmarket, text="Cabbage", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=4, column=0, padx=20, pady=5)
        Cabbage_entry = Entry(stockinmarket,width=10, textvariable=self.cabbage_available, bd=8, bg="indigo", fg="white").grid(row=4, column=1)

        Cauliflr_lbl = Label(stockinmarket, text="CauliFlower", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=5, column=0, padx=20, pady=5)
        Cauliflr_entry = Entry(stockinmarket,width=10, textvariable=self.cauliflr_available, bd=8, bg="indigo", fg="white").grid(row=5, column=1)

        Chilli_lbl = Label(stockinmarket, text="Chilli", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=6, column=0, padx=20, pady=5)
        Chilli_entry = Entry(stockinmarket,width=10, textvariable=self.chilli_available, bd=8, bg="indigo", fg="white").grid(row=6, column=1)

        Potato_lbl = Label(stockinmarket, text="Potato", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=7, column=0, padx=20, pady=5)
        Potato_entry = Entry(stockinmarket,width=10, textvariable=self.potato_available, bd=8, bg="indigo", fg="white").grid(row=7, column=1)

        Beans_lbl = Label(stockinmarket, text="Beans", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=8, column=0, padx=20, pady=5)
        Beans_entry = Entry(stockinmarket,width=10, textvariable=self.beans_available, bd=8, bg="indigo", fg="white").grid(row=8, column=1)

        # ===============Vegetables==================================================================

        Vegetable = LabelFrame(root, text="Vegetables", relief=GROOVE, bd=10,font=("Times New Roman", 15, "bold"), bg="indigo", fg="white")
        Vegetable.place(x=350, y=140, width=350, height=500)
        Vegie_lbl = Label(Vegetable, text="Vegetable", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=0, column=0, padx=20, pady=5)
        Vegie_qnty = Label(Vegetable, text="Quantity", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=0, column=1, padx=20, pady=5)

        Carrot_qnty = Label(Vegetable, text="Carrot", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=1, column=0, padx=20, pady=5)
        Carrot_qnty_entry = Entry(Vegetable, width=10, textvariable=self.carrot, bd=8, bg="indigo", fg="white").grid(row=1, column=1)

        Onion_qnty = Label(Vegetable, text="Onion", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=2, column=0, padx=20, pady=5)
        Onion_qnty_entry = Entry(Vegetable, width=10, textvariable=self.onion, bd=8, bg="indigo", fg="white").grid(row=2,column=1)

        Tomato_qnty = Label(Vegetable, text="Tomato", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=3, column=0, padx=20, pady=5)
        Tomato_qnty_entry = Entry(Vegetable, width=10, textvariable=self.tomato, bd=8, bg="indigo", fg="white").grid(row=3, column=1)

        Cabbage_qnty = Label(Vegetable, text="Cabbage", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=4, column=0, padx=20, pady=5)
        Cabbage_qnty_entry = Entry(Vegetable, width=10, textvariable=self.cabbage, bd=8, bg="indigo", fg="white").grid(row=4, column=1)

        Cauliflr_qnty = Label(Vegetable, text="CauliFlower", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=5, column=0, padx=20, pady=5)
        Cauliflr_qnty_entry = Entry(Vegetable, width=10, textvariable=self.cauliflr, bd=8, bg="indigo", fg="white").grid(row=5, column=1)

        Chilli_qnty = Label(Vegetable, text="Chilli", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=6, column=0, padx=20, pady=5)
        Chilli_qnty_entry = Entry(Vegetable, width=10, textvariable=self.chilli, bd=8, bg="indigo", fg="white").grid(row=6, column=1)

        Potato_qnty = Label(Vegetable, text="Potato", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=7, column=0, padx=20, pady=5)
        Potato_qnty_entry = Entry(Vegetable, width=10, textvariable=self.potato, bd=8, bg="indigo", fg="white").grid(row=7, column=1)

        Beans_qnty = Label(Vegetable, text="Beans", font=("times new roman", 20, "bold"), bg="indigo",fg="white").grid(row=8, column=0, padx=20, pady=5)
        Beans_qnty_entry = Entry(Vegetable, width=10, textvariable=self.beans, bd=8, bg="indigo", fg="white").grid(row=8,column=1)

        #=============Customer bill frame===============================================================

        bill = Frame(self.root,bd=10,relief=GROOVE)
        bill.place(x=700,y=140,width=836,height=500)
        billtitle=Label(bill, text="Customer Bill",font=("Times New Roman",15,"bold"),bd=12,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(bill, orient=VERTICAL)
        self.txtarea = Text(bill,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        self.Bill_design()

        #===============Bill amount and tax frame=================================================================

        billmenu = LabelFrame(root,text="Total Bill amount",relief=GROOVE,bd=10,font=("Times New Roman",15,"bold"),bg="indigo",fg="white")
        billmenu.place(x=0,y=640,width=600,height=165)

        Amount_lbl = Label(billmenu, text="Amount", font=("times new roman", 15, "bold"), bg="indigo", fg="white").grid(row=0, column=0, padx=20, pady=5)
        Amount_entry = Entry(billmenu,textvariable=self.tot_amount, bd=8, bg="indigo", fg="white").grid(row=0, column=1)

        Tax = Label(billmenu, text="Tax", font=("times new roman", 15, "bold"), bg="indigo",fg="white").grid(row=0, column=2, padx=20, pady=5)
        Tax_entry = Entry(billmenu,textvariable=self.tot_tax , bd=8, bg="indigo", fg="white").grid(row=0, column=3)

        #==============Options frame====================================================================

        printbill = LabelFrame(root,text="",relief=GROOVE,bd=10,font=("Times New Roman",15,"bold"),bg="indigo",fg="white")
        printbill.place(x=600,y=640,width=936,height=165)
        Total = Button(printbill,text="Total",font=("Times new roman",20,"bold"),bg="gray",fg="white",width=11,command=self.total).grid(row=1,column=0,padx=4,pady=10)
        Gen_bill = Button(printbill,text="Generate Bill",font=("Times new roman",20,"bold"),bg="gray",fg="white",width=11,command=self.Bill_area).grid(row=1,column=1,padx=4,pady=2)
        clear = Button(printbill,text="clear",font=("Times new roman",20,"bold"),bg="gray",fg="white",width=11,command=self.clear_bill).grid(row=1,column=2,padx=4,pady=2)
        exit = Button(printbill,text="exit",font=("Times new roman",20,"bold"),bg="gray",fg="white",width=11,command=self.bill_exit).grid(row=1,column=3,padx=4,pady=2)


    def total(self):
        self.tot_vegetable_price = float(
            (self.carrot.get() * 12) + (self.onion.get() * 30) + (self.tomato.get() * 25) + (self.cabbage.get() * 30) + (self.cauliflr.get() * 28) + (self.chilli.get() * 50)
            + (self.potato.get() * 40) + (self.beans.get() * 60)
        )

        self.tot_amount.set(str( self.tot_vegetable_price))
        self.tot_tax.set( self.tot_vegetable_price*0.05)

    def Bill_design(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, "\t\t\t\t\t Welcome to Clint Groceries")
        self.txtarea.insert(END, f"\n Bill No:{self.cust_bill.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.cust_name.get()}")
        self.txtarea.insert(END, f"\n Customer Phone: {self.cust_phone.get()}")
        self.txtarea.insert(END, f"\n ==================================================================================================")
        self.txtarea.insert(END, f"\n \tProducts\t\t\t\t\tQuantity\t\t\t\t\tPrice")
        self.txtarea.insert(END, f"\n ==================================================================================================")


    def Bill_area(self):
        self.Bill_design()
        if self.cust_name.get() == "" or self.cust_phone=="":
            messagebox.showerror("Error","Enter proper customer details")
        elif self.tot_amount.get() == "0.0":
            messagebox.showerror("Error","No items purchased")
        else:
            if self.carrot.get()!=0:
                self.txtarea.insert(END, f"\n Carrot\t\t\t\t\t\t{self.carrot.get()}\t\t\t\t\t{float(self.carrot.get()*12)}")
            if self.onion.get()!=0:
                self.txtarea.insert(END, f"\n Onion\t\t\t\t\t\t{self.onion.get()}\t\t\t\t\t{float(self.onion.get()*30)}")
            if self.tomato.get()!=0:
                self.txtarea.insert(END, f"\n Tomato\t\t\t\t\t\t{self.tomato.get()}\t\t\t\t\t{float(self.tomato.get()*30)}")
            if self.cabbage.get()!=0:
                self.txtarea.insert(END, f"\n Cabbage\t\t\t\t\t\t{self.cabbage.get()}\t\t\t\t\t{float(self.cabbage.get()*30)}")
            if self.cauliflr.get()!=0:
                self.txtarea.insert(END, f"\n Caluliflower\t\t\t\t\t\t{self.cauliflr.get()}\t\t\t\t\t{float(self.cauliflr.get()*30)}")
            if self.chilli.get()!=0:
                self.txtarea.insert(END, f"\n Chilli\t\t\t\t\t\t{self.chilli.get()}\t\t\t\t\t{float(self.chilli.get()*30)}")
            if self.potato.get()!=0:
                self.txtarea.insert(END, f"\n Potato\t\t\t\t\t\t{self.potato.get()}\t\t\t\t\t{float(self.potato.get()*30)}")
            if self.beans.get()!=0:
                self.txtarea.insert(END, f"\n Beans\t\t\t\t\t\t{self.beans.get()}\t\t\t\t\t{float(self.beans.get()*30)}")

        self.txtarea.insert(END,f"\n---------------------------------------------------------------------------------------------------")
        self.txtarea.insert(END,f"\n Total Bill: {self.tot_amount.get()}")
        self.txtarea.insert(END,f"\n Total Tax: {self.tot_tax.get()}")
        self.txtarea.insert(END,f"\n---------------------------------------------------------------------------------------------------")
        self.save_bill()


    def save_bill(self):
        option=messagebox.askyesno("Save","Do you want to save Bill?")
        if option >0 :
            self.bill_data = self.txtarea.get("1.0",END)
            f1 = open("bills/"+str(self.cust_bill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Message",f"Bill No : {self.cust_bill} saved successfully")
        else: return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i. split('.')[0] == self. cust_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present == "no":
            messagebox.showinfo("Error","Invalid Bill no")

    def clear_bill(self):
        op = messagebox.askyesno("Clear", "Do you want to clear current bill?")
        if op > 0:
            self.cust_name.set("")
            self.cust_phone.set("")
            x = random.randint(1000, 9999)
            self.cust_bill.set("")
            self.cust_bill.set(str(x))
            self.search.set("")

            self.carrot.set(0)
            self.onion.set(0)
            self.tomato.set(0)
            self.cabbage.set(0)
            self.cauliflr.set(0)
            self.chilli.set(0)
            self.potato.set(0)
            self.beans.set(0)

            self.tot_amount.set("")
            self.tot_tax.set("")
            self.Bill_design()

        else:return

    def bill_exit(self):
        op = messagebox.askyesno("Close","Do you want to close this application?")
        if op>0:
            self.root.destroy()
        else:return

    def new_entry(self):
       add=Toplevel()
       #message="child window"
       Label(add,text="Grocery Stock",bd=2,relief=GROOVE,bg="gray",fg="white",font=("Times New ROman",30,"bold"),pady=2).pack(fill=X)

       labelframe2 = LabelFrame(add, text="Update stock",font=("Times New Roman",15,"bold"),bg="indigo",fg="white")
       labelframe2.place(x=0,y=80,relwidth=1)

       now = datetime.datetime.now()
       d=now.strftime("%Y-%m-%d")
       Date=Label(labelframe2,text=d,bg="indigo",fg="white",font=("Times new roman",15,"bold")).pack()

       self.entry = LabelFrame(add, text="",font=("Times New Roman",15,"bold"),bg="indigo",fg="white")
       self.entry.place(x=0,y=160,relwidth=2)

           
       L1 = Label(self.entry, text="Vegetable",font=("times new roman",15,"bold"),bg="indigo",fg="white").grid(row=1,column=0,padx=20,pady=5)
       #L1.pack( side = "left")
       E1 = Entry(self.entry,textvariable = self.Vegie_stock, bd =10,bg="indigo",fg="white").grid(row=1,column=1)
       #E1.pack(side = "right")
       L2 = Label(self.entry, text="Quantity(Kg)",font=("times new roman",15,"bold"),bg="indigo",fg="white").grid(row=1,column=2,padx=40,pady=5)
       E2 = Entry(self.entry,textvariable = self.Vegie_qnty, bd =10,bg="indigo",fg="white").grid(row=1,column=3)

       #another=Button(add,text="+",font=("times new roman",15,"bold"),bg="red",fg="white",command=self.new_vegetable).grid(row=0,column=0,padx=50,pady=5)


       #def stock(self):
       stock_frame = Frame(add, bd=10, relief=GROOVE)
       stock_frame.place(x=350, y=240, width=836, height=1000)
       stocktitle = Label(stock_frame, text="Stocks Available", font=("Times New Roman", 15, "bold"), bd=12, relief=GROOVE).pack(fill=X)
       scrol_y = Scrollbar(stock_frame, orient=VERTICAL)
       self.txtarea = Text(stock_frame, yscrollcommand=scrol_y.set)
       scrol_y.pack(side=RIGHT, fill=Y)
       scrol_y.config(command=self.txtarea.yview)
       self.txtarea.pack(fill=BOTH, expand=1)
       self.stock_area()




       #def new_vegetable(self):
       #self.stock()

    def stock_area(self):
        self.txtarea.insert(END,f"Vegetable\t\t\t\t\t\tQuantity")
        self.txtarea.insert(END,f"{self.Vegie_stock}\t\t\t\t\t\t{self.Vegie_qnty}")



    
        

       

root = Tk()
label = Bill(root)
root.mainloop()

