import tkinter as tk
from tkinter import *
from datetime import *
import tkinter.messagebox

####################################### class User ########################################

class User:
    def __init__(self, fullName, username, password):
        self.fullName = fullName
        self.username = username
        self.password = password
        self.curruser = int()
    def getName(self):
        return self.fullName
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def setCurruser(self, x):
        self.curruser = x
    def getCurruser(self):
        return self.curruser

class Company:
    def __init__(self):
        self.user_list = []
    def add(self, user):
        self.user_list.append(user)
    def seeCompany(self):
        return self.user_list

infile = open("users.txt","r")
users = infile.readlines()
infile.close()

new_company = Company()
for i in range(len(users)):
    fullName, username, password = users[i].split(",") ##split and add items into class
    password = password.replace("\n", "") ##take '\n' out, because they also compare '\n'
    new_company.add(User(fullName,username,password))

users = new_company.seeCompany()

##for i in range(len(users)):
##    print("Full name:"+users[i].getName(), users[i].getUsername(), users[i].getPassword())

currentUser = [0]

####################################### class Item #######################################

class Item:
    def __init__(self, name, cost, price, stock):
        self.name = name
        self.cost = cost
        self.price = price
        self.stock = stock
    def getName(self):
        return self.name
    def getCost(self):
        return self.cost
    def getPrice(self):
        return self.price
    def getStock(self):
        return self.stock
    def incStock(self):
        self.stock += 1
    def decStock(self):
        if self.stock > 0:
            self.stock -= 1
    def setStock(self, x):
        if x >= 0:
            self.stock = x

class Storage:
    def __init__(self):
        self.item_list = []
    def add(self, item):
        self.item_list.append(item)
    def seeStorage(self):
        return self.item_list

##create an item (7 items)
##pen = Item("Pen",5,10,10)
##pencil = Item("Pencil",4,7,10)
##tape = Item("Correction tape",18,25,10)
##rubber = Item("Rubber",3,5,10)
##highlighter = Item("Highlighter",10,15,10)
##sharpener = Item("Sharpener",55,70,10)
##stapler = Item("Stapler",35,45,10)
##clip = Item("Paperclips",45,55,10)
##calculator = Item("Calculator",380,430,10)

##open file, get all products' info from the file
infile = open("products.txt", "r")
items = infile.readlines()
infile.close()

##new storage
new_storage = Storage()

for i in range(len(items)):
    name, cost, price, stock = items[i].split(",") ##split and add items into class
    cost = int(cost)
    price = int(price)
    stock = int(stock)
    new_storage.add(Item(name,cost,price,stock))

items = new_storage.seeStorage()

####################################### class iCash ########################################

class iCash(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('iCash')
        self.geometry('680x386')
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LogInPage, HomePage, PurchasePage, SellPage, StockPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LogInPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        #### FOR DIFF ######
        frame.updateInterface()
        ###################
        frame.tkraise()

####################################### LOG IN PAGE #######################################

class LogInPage(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        greeting_msg = Label(self, text="Welcome to iCash", font=("Source Code Pro", 40, "bold")).place(x=150,y=100)
        user_lbl = Label(self, text="Username:", font=("Source Code Pro", 20)).place(x=190,y=160)
        self.user_entry = Entry(self)
        self.user_entry.place(x=310, y=160)
        
        pass_lbl = Label(self, text="Password:", font=("Source Code Pro", 20)).place(x=190,y=190)
        self.pass_entry = Entry(self)
        self.pass_entry.place(x=310, y=190)

        self.log_button = Button (self, text = "Log in", font=("Source Code Pro", 20), command = lambda: self.login() and self.clear() and
                                  controller.show_frame(HomePage))
        self.log_button.place(x=310, y=220)

    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        if (username == "" or password == ""):
            return 0
        else:
            for i in range (len(users)):
                if (username == users[i].getUsername() and password == users[i].getPassword() ):
                    currentUser[0] = i
                    return 1
            return 0
    
    def clear(self):
        self.user_entry.delete(0,'end')
        self.pass_entry.delete(0,'end')
        return 1
    
    ########### FOR DIFF #########
    def updateInterface(self):
        pass
    #############################
    
####################################### HOME PAGE #######################################

class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        now=datetime.now()

        frame1 = Frame(self) ##button menu zone
        frame1.pack()
        
        home_button = Button(frame1, text='Home',width=12, command=lambda: controller.show_frame(HomePage)).grid(row=1, column=0)
        purc_button = Button(frame1, text='Purchase',width=12, command=lambda: controller.show_frame(PurchasePage)).grid(row=1, column=1)
        sell_button = Button(frame1, text='Sell',width=12, command=lambda: controller.show_frame(SellPage)).grid(row=1, column=2)
        stock_button = Button(frame1, text='Stock',width=12, command=lambda: controller.show_frame(StockPage)).grid(row=1, column=3)
        logout_button = Button(frame1, text='Log out',width=12, command=lambda: controller.show_frame(LogInPage)).grid(row=1, column=4)
        
        frame2 = Frame(self) ##user info zone
        frame2.pack(side = LEFT, expand = 1)
        
        rect_frame = LabelFrame(frame2, text='info', font=('arial',20))
        rect_frame.grid(row=0)
        
        name_lbl1 = Label(rect_frame, text='Name:').grid(row=0, column=0, sticky='E', padx=5, pady=2)
        self.name_lbl2 = Label(rect_frame, text="-")
        self.name_lbl2.grid(row=0, column=1, columnspan=9, sticky="W", pady=3)
        
        user_lbl1 = Label(rect_frame, text='User:').grid(row=1, column=0, sticky='E', padx=5, pady=2)
        self.user_lbl2 = Label(rect_frame, text="-")
        self.user_lbl2.grid(row=1, column=1, columnspan=9, sticky="W", pady=2)
        
        date_lbl1 = Label(rect_frame, text='Date:').grid(row=2, column=0, sticky="E", padx=5, pady=2)
        date_lbl2= Label(rect_frame, text=now.strftime('%x')).grid(row=2, column=1, columnspan=9, sticky="W", pady=2)

        frame3 = Frame(self)
        frame3.pack()

        self.updateInterface()
        
    def changelabel(self):
        self.name_lbl2.config(text=str(users[currentUser[0]].getName()))
        self.user_lbl2.config(text=str(users[currentUser[0]].getUsername()))

    ########### FOR DIFF #########
    def updateInterface(self):
        self.changelabel()
    #############################

####################################### PURCHASE PAGE #######################################
comp_name = "Midtown Stationary"

class PurchasePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        frame1 = Frame(self) ##button menu zone
        frame1.pack()
    
        home_button = Button(frame1, text='Home',width=12, command=lambda: controller.show_frame(HomePage)).grid(row=1, column=0)
        purc_button = Button(frame1, text='Purchase',width=12, command=lambda: controller.show_frame(PurchasePage)).grid(row=1, column=1)
        sell_button = Button(frame1, text='Sell',width=12, command=lambda: controller.show_frame(SellPage)).grid(row=1, column=2)
        stock_button = Button(frame1, text='Stock',width=12, command=lambda: controller.show_frame(StockPage)).grid(row=1, column=3)
        logout_button = Button(frame1, text='Log out',width=12, command=lambda: controller.show_frame(LogInPage)).grid(row=1, column=4)

        frame2 = Frame(self) ##supplier information zone
        frame2.pack()

        po_lbl = Label(frame2, text='PO No:')
        po_lbl.pack(side=LEFT)
        self.po_ent = Entry(frame2, width=10)
        self.po_ent.pack(side=LEFT)
        sup_lbl = Label(frame2, text='Supplier Name:')
        sup_lbl.pack(side=LEFT)
        self.sup_ent = Entry(frame2)
        self.sup_ent.pack(side=LEFT)
        tax_lbl = Label(frame2, text='Tax Id:')
        tax_lbl.pack(side=LEFT)
        self.tax_ent = Entry(frame2)
        self.tax_ent.pack()

        frame3 = Frame(self) ##layout for selecting product 
        frame3.pack(expand=1) ## top horizontal header layout
        
        product = Label(frame3, text='PRODUCT', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=0)
        cost = Label(frame3, text='COST', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=1)
        quantity = Label(frame3, text='QTY', bd=1, relief="solid", bg='green', width=5).grid(row=0, column=2)
        sub_total = Label(frame3, text='AMOUNT', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=3)

        self.qty_ordered = [0,0,0,0,0,0,0,0,0] ##quantity that is ordered per product (index[0]-[8])
        self.amount = [0,0,0,0,0,0,0,0,0] ##total price for each product (index[0]-[8])
        
        ##pen (a)
        a_product = Label(frame3, text=items[0].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=1, column=0, padx=5)
        a_cost = Label(frame3, text=items[0].getCost(), bd=1, relief="solid", width=12).grid(row=1, column=1, padx=5)
        
        self.a_qty = Label(frame3, text=self.qty_ordered[0], bd=1, relief="solid", width=5)
        self.a_qty.grid(row=1, column=2, padx=5)
        
        self.a_amount = Label(frame3, text=self.amount[0], bd=1, relief="solid", width=12)
        self.a_amount.grid(row=1, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(0)).grid(row=1, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(0)).grid(row=1, column=5)

        ##pencil (b)
        b_product = Label(frame3, text=items[1].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=2, column=0, padx=5)
        b_cost = Label(frame3, text=items[1].getCost(), bd=1, relief="solid", width=12).grid(row=2, column=1, padx=5)
        
        self.b_qty = Label(frame3, text=self.qty_ordered[1], bd=1, relief="solid", width=5)
        self.b_qty.grid(row=2, column=2, padx=5)
        
        self.b_amount = Label(frame3, text=self.amount[1], bd=1, relief="solid", width=12)
        self.b_amount.grid(row=2, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(1)).grid(row=2, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(1)).grid(row=2, column=5)

        ##Correction tape (c)
        c_product = Label(frame3, text=items[2].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=3, column=0, padx=5)
        c_cost = Label(frame3, text=items[2].getCost(), bd=1, relief="solid", width=12).grid(row=3, column=1, padx=5)
        
        self.c_qty = Label(frame3, text=self.qty_ordered[2], bd=1, relief="solid", width=5)
        self.c_qty.grid(row=3, column=2, padx=5)
        
        self.c_amount = Label(frame3, text=self.amount[2], bd=1, relief="solid", width=12)
        self.c_amount.grid(row=3, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(2)).grid(row=3, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(2)).grid(row=3, column=5)

        ##Rubber (d)
        d_product = Label(frame3, text=items[3].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=4, column=0, padx=5)
        d_cost = Label(frame3, text=items[3].getCost(), bd=1, relief="solid", width=12).grid(row=4, column=1, padx=5)
        
        self.d_qty = Label(frame3, text=self.qty_ordered[3], bd=1, relief="solid", width=5)
        self.d_qty.grid(row=4, column=2, padx=5)
        
        self.d_amount = Label(frame3, text=self.amount[3], bd=1, relief="solid", width=12)
        self.d_amount.grid(row=4, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(3)).grid(row=4, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(3)).grid(row=4, column=5)

        ##Highlighter (e)
        e_product = Label(frame3, text=items[4].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=5, column=0, padx=5)
        e_cost = Label(frame3, text=items[4].getCost(), bd=1, relief="solid", width=12).grid(row=5, column=1, padx=5)
        
        self.e_qty = Label(frame3, text=self.qty_ordered[4], bd=1, relief="solid", width=5)
        self.e_qty.grid(row=5, column=2, padx=5)
        
        self.e_amount = Label(frame3, text=self.amount[4], bd=1, relief="solid", width=12)
        self.e_amount.grid(row=5, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(4)).grid(row=5, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(4)).grid(row=5, column=5)

        ##Sharpener (f)
        f_product = Label(frame3, text=items[5].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=6, column=0, padx=5)
        f_cost = Label(frame3, text=items[5].getCost(), bd=1, relief="solid", width=12).grid(row=6, column=1, padx=5)
        
        self.f_qty = Label(frame3, text=self.qty_ordered[5], bd=1, relief="solid", width=5)
        self.f_qty.grid(row=6, column=2, padx=5)
        
        self.f_amount = Label(frame3, text=self.amount[5], bd=1, relief="solid", width=12)
        self.f_amount.grid(row=6, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(5)).grid(row=6, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(5)).grid(row=6, column=5)

        ##Stapler (g)
        g_product = Label(frame3, text=items[6].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=7, column=0, padx=5)
        g_cost = Label(frame3, text=items[6].getCost(), bd=1, relief="solid", width=12).grid(row=7, column=1, padx=5)
        
        self.g_qty = Label(frame3, text=self.qty_ordered[6], bd=1, relief="solid", width=5)
        self.g_qty.grid(row=7, column=2, padx=5)
        
        self.g_amount = Label(frame3, text=self.amount[6], bd=1, relief="solid", width=12)
        self.g_amount.grid(row=7, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(6)).grid(row=7, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(6)).grid(row=7, column=5)

        ##Paperclips (h)
        h_product = Label(frame3, text=items[7].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=8, column=0, padx=5)
        h_cost = Label(frame3, text=items[7].getCost(), bd=1, relief="solid", width=12).grid(row=8, column=1, padx=5)
        
        self.h_qty = Label(frame3, text=self.qty_ordered[7], bd=1, relief="solid", width=5)
        self.h_qty.grid(row=8, column=2, padx=5)
        
        self.h_amount = Label(frame3, text=self.amount[7], bd=1, relief="solid", width=12)
        self.h_amount.grid(row=8, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(7)).grid(row=8, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(7)).grid(row=8, column=5)

        ##Calculator (i)
        i_product = Label(frame3, text=items[8].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=9, column=0, padx=5)
        i_cost = Label(frame3, text=items[8].getCost(), bd=1, relief="solid", width=12).grid(row=9, column=1, padx=5)
        
        self.i_qty = Label(frame3, text=self.qty_ordered[7], bd=1, relief="solid", width=5)
        self.i_qty.grid(row=9, column=2, padx=5)
        
        self.i_amount = Label(frame3, text=self.amount[8], bd=1, relief="solid", width=12)
        self.i_amount.grid(row=9, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(8)).grid(row=9, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(8)).grid(row=9, column=5)
        
        total_lbl = Label(frame3, text='Total').grid(row=10, column=1)
        self.total_qty = Label(frame3, text=sum(self.qty_ordered))
        self.total_qty.grid(row=10, column=2)
        self.total_amount = Label(frame3, text=sum(self.amount))
        self.total_amount.grid(row=10, column=3)
        save = Button(frame3, text=' Save ', command=self.save).grid(row=10, column=4, columnspan=2)
        
    def clear(self):
        self.po_ent.delete(0,'end')
        self.sup_ent.delete(0,'end')
        self.tax_ent.delete(0,'end')
        
##        print("After:\n\t%-15s    %4s    %5s    %5s\n" %("Description", "Cost", "Price", "Stock"))
##        for i in range (9):
##            print("\t%-15s    %4d    %5d    %5d\n" %(items[i].getName(),  items[i].getCost(), items[i].getCost(), items[i].getStock()))
##        print(self.qty_ordered)
##        print(self.amount)
        
    def save(self):
##        print("type", type(int(self.po_ent.get())))
##        temp = int(self.po_ent.get())
        if type(int(self.po_ent.get())) not in  [int]:
            raise ValueError ("The PO number must be an integer ONLY")
        po = ("- PO No: "+ str(self.po_ent.get())) ##show info in message box
        sup_name = ("- Supplier Name: "+ str(self.sup_ent.get()))
        tax = ("- Tax Id: "+ str(self.tax_ent.get()))
        total = ("- Total: "+str(sum(self.amount))+"baht")
        summary = (po+"\n"+sup_name+"\n"+tax+"\n"+total)
        tkinter.messagebox.showinfo('Save Purchase', str(summary))

        ##save purchase-info into file
        file_name = "PO_"+str(self.po_ent.get())+".txt"
        outfile = open(file_name,"w")

        ##New layout for text file save out
        outfile.write("Midtown Stationary \t\t\t\tPurchase Order\n--My books. My stationary. My store.--\n\n")
        now=datetime.now()
        border1="--------------------------------"
        border2="---------------"
        outfile.write("%3s%6s\n%32s%14s%15s\n| Name     | %-17s |%9sDate | %8s    |\n| Tax id   | %-17s |%9sPO#  | %8s    |\n%32s%14s%15s\n\n"
                      %(" ","Vendor",border1," ",border2,self.sup_ent.get()[:17:]," ",now.strftime('%x'),self.tax_ent.get()," ",self.po_ent.get(),border1," ",border2))
        border = "---------------------------------------------------------"
        outfile.write("%4s%57s\n%4s| No. |     Description     | QTY |  Price  |   Amount  |\n%4s%57s\n"%(" ",border, " "," ",border))
        for i in range(9):
            outfile.write("%4s|  %d  | %-20s|%3d  |  %5d  |   %5d   |\n"%(" ", (i+1), items[i].getName(), self.qty_ordered[i], items[i].getCost(), self.amount[i]))
        outfile.write("%4s%57s\n%38s|  Total  |   %5d   |\n%38s-----------------------"%(" ",border, " ",sum(self.amount)," "))

        ##reset self.qty_ordered[] & self.amount[] list to 0
        for i in range(9):
            x = items[i].getStock()
            x += self.qty_ordered[i]
            items[i].setStock(x)
            self.qty_ordered[i] = self.amount[i] = 0
            self.stockValueSet(i)

        ##save stock-info into file
        file = open("products.txt","w")
        for i in range(len(items)):
            text = items[i].getName() + "," + str(items[i].getCost()) + "," + str(items[i].getPrice()) + "," + str(items[i].getStock())
            file.write(text + "\n")
            self.stockValueSet(i)
        file.close()
        
        self.clear()

    def stockValueSet(self, i): ##show new stock & value
        if i==0:
            self.a_qty.config(text=self.qty_ordered[i])
            self.a_amount.config(text=self.amount[i])
        elif i==1:
            self.b_qty.config(text=self.qty_ordered[i])
            self.b_amount.config(text=self.amount[i])
        elif i==2:
            self.c_qty.config(text=self.qty_ordered[i])
            self.c_amount.config(text=self.amount[i])
        elif i==3:
            self.d_qty.config(text=self.qty_ordered[i])
            self.d_amount.config(text=self.amount[i])
        elif i==4:
            self.e_qty.config(text=self.qty_ordered[i])
            self.e_amount.config(text=self.amount[i])
        elif i==5:
            self.f_qty.config(text=self.qty_ordered[i])
            self.f_amount.config(text=self.amount[i])
        elif i==6:
            self.g_qty.config(text=self.qty_ordered[i])
            self.g_amount.config(text=self.amount[i])
        elif i==7:
            self.h_qty.config(text=self.qty_ordered[i])
            self.h_amount.config(text=self.amount[i])
        elif i==8:
            self.i_qty.config(text=self.qty_ordered[i])
            self.i_amount.config(text=self.amount[i])
        
        self.total_qty.config(text=sum(self.qty_ordered))
        self.total_amount.config(text=sum(self.amount))
        
    def plus1(self, i):
        self.qty_ordered[i] += 1
        self.amount[i] = items[i].getCost()*self.qty_ordered[i]
        self.stockValueSet(i)

    def minus1(self, i):
        if self.qty_ordered[i]>0:
            self.qty_ordered[i] -= 1
            self.amount[i] = items[i].getCost()*self.qty_ordered[i]
            self.stockValueSet(i)

    ########### FOR DIFF #############
    def updateInterface(self):
        pass
    #############################
    
####################################### SELL PAGE #######################################
    
class SellPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        
        frame1 = Frame(self) ##button menu zone
        frame1.pack()
    
        home_button = Button(frame1, text='Home',width=12, command=lambda: controller.show_frame(HomePage)).grid(row=1, column=0)
        purc_button = Button(frame1, text='Purchase',width=12, command=lambda: controller.show_frame(PurchasePage)).grid(row=1, column=1)
        sell_button = Button(frame1, text='Sell',width=12, command=lambda: controller.show_frame(SellPage)).grid(row=1, column=2)
        stock_button = Button(frame1, text='Stock',width=12, command=lambda: controller.show_frame(StockPage)).grid(row=1, column=3)
        logout_button = Button(frame1, text='Log out',width=12, command=lambda: controller.show_frame(LogInPage)).grid(row=1, column=4)

        frame2 = Frame(self) ##customer information zone
        frame2.pack()

        invoice_lbl = Label(frame2, text='Invoice No:')
        invoice_lbl.pack(side=LEFT)
        self.invoice_ent = Entry(frame2, width=5)
        self.invoice_ent.pack(side=LEFT)
        customer_lbl = Label(frame2, text='Customer Name:')
        customer_lbl.pack(side=LEFT)
        self.customer_ent = Entry(frame2)
        self.customer_ent.pack(side=LEFT)
        tax_lbl = Label(frame2, text='Tax Id:')
        tax_lbl.pack(side=LEFT)
        self.tax_ent = Entry(frame2)
        self.tax_ent.pack()

        frame3 = Frame(self) ##layout for selecting product 
        frame3.pack(expand=1) ## top horizontal header layout
        
        product = Label(frame3, text='PRODUCT', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=0)
        price = Label(frame3, text='PRICE', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=1)
        quantity = Label(frame3, text='QTY', bd=1, relief="solid", bg='green', width=5).grid(row=0, column=2)
        sub_total = Label(frame3, text='AMOUNT', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=3)

        self.qty_ordered = [0,0,0,0,0,0,0,0,0] ##quantity that is ordered per product (index[0]-[8])
        self.amount = [0,0,0,0,0,0,0,0,0] ##total price for each product (index[0]-[8])
        
        ##pen (a)
        a_product = Label(frame3, text=items[0].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=1, column=0, padx=5)
        a_price = Label(frame3, text=items[0].getPrice(), bd=1, relief="solid", width=12).grid(row=1, column=1, padx=5)
        
        self.a_qty = Label(frame3, text=self.qty_ordered[0], bd=1, relief="solid", width=5)
        self.a_qty.grid(row=1, column=2, padx=5)
        
        self.a_amount = Label(frame3, text=self.amount[0], bd=1, relief="solid", width=12)
        self.a_amount.grid(row=1, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(0)).grid(row=1, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(0)).grid(row=1, column=5)

        ##pencil (b)
        b_product = Label(frame3, text=items[1].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=2, column=0, padx=5)
        b_price = Label(frame3, text=items[1].getPrice(), bd=1, relief="solid", width=12).grid(row=2, column=1, padx=5)
        
        self.b_qty = Label(frame3, text=self.qty_ordered[1], bd=1, relief="solid", width=5)
        self.b_qty.grid(row=2, column=2, padx=5)
        
        self.b_amount = Label(frame3, text=self.amount[1], bd=1, relief="solid", width=12)
        self.b_amount.grid(row=2, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(1)).grid(row=2, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(1)).grid(row=2, column=5)

        ##Correction tape (c)
        c_product = Label(frame3, text=items[2].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=3, column=0, padx=5)
        c_price = Label(frame3, text=items[2].getPrice(), bd=1, relief="solid", width=12).grid(row=3, column=1, padx=5)
        
        self.c_qty = Label(frame3, text=self.qty_ordered[2], bd=1, relief="solid", width=5)
        self.c_qty.grid(row=3, column=2, padx=5)
        
        self.c_amount = Label(frame3, text=self.amount[2], bd=1, relief="solid", width=12)
        self.c_amount.grid(row=3, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(2)).grid(row=3, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(2)).grid(row=3, column=5)

        ##Rubber (d)
        d_product = Label(frame3, text=items[3].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=4, column=0, padx=5)
        d_price = Label(frame3, text=items[3].getPrice(), bd=1, relief="solid", width=12).grid(row=4, column=1, padx=5)
        
        self.d_qty = Label(frame3, text=self.qty_ordered[3], bd=1, relief="solid", width=5)
        self.d_qty.grid(row=4, column=2, padx=5)
        
        self.d_amount = Label(frame3, text=self.amount[3], bd=1, relief="solid", width=12)
        self.d_amount.grid(row=4, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(3)).grid(row=4, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(3)).grid(row=4, column=5)

        ##Highlighter (e)
        e_product = Label(frame3, text=items[4].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=5, column=0, padx=5)
        e_price = Label(frame3, text=items[4].getPrice(), bd=1, relief="solid", width=12).grid(row=5, column=1, padx=5)
        
        self.e_qty = Label(frame3, text=self.qty_ordered[4], bd=1, relief="solid", width=5)
        self.e_qty.grid(row=5, column=2, padx=5)
        
        self.e_amount = Label(frame3, text=self.amount[4], bd=1, relief="solid", width=12)
        self.e_amount.grid(row=5, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(4)).grid(row=5, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(4)).grid(row=5, column=5)

        ##Sharpener (f)
        f_product = Label(frame3, text=items[5].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=6, column=0, padx=5)
        f_price = Label(frame3, text=items[5].getPrice(), bd=1, relief="solid", width=12).grid(row=6, column=1, padx=5)
        
        self.f_qty = Label(frame3, text=self.qty_ordered[5], bd=1, relief="solid", width=5)
        self.f_qty.grid(row=6, column=2, padx=5)
        
        self.f_amount = Label(frame3, text=self.amount[5], bd=1, relief="solid", width=12)
        self.f_amount.grid(row=6, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(5)).grid(row=6, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(5)).grid(row=6, column=5)

        ##Stapler (g)
        g_product = Label(frame3, text=items[6].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=7, column=0, padx=5)
        g_price = Label(frame3, text=items[6].getPrice(), bd=1, relief="solid", width=12).grid(row=7, column=1, padx=5)
        
        self.g_qty = Label(frame3, text=self.qty_ordered[6], bd=1, relief="solid", width=5)
        self.g_qty.grid(row=7, column=2, padx=5)
        
        self.g_amount = Label(frame3, text=self.amount[6], bd=1, relief="solid", width=12)
        self.g_amount.grid(row=7, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(6)).grid(row=7, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(6)).grid(row=7, column=5)

        ##Paperclips (h)
        h_product = Label(frame3, text=items[7].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=8, column=0, padx=5)
        h_price = Label(frame3, text=items[7].getPrice(), bd=1, relief="solid", width=12).grid(row=8, column=1, padx=5)
        
        self.h_qty = Label(frame3, text=self.qty_ordered[7], bd=1, relief="solid", width=5)
        self.h_qty.grid(row=8, column=2, padx=5)
        
        self.h_amount = Label(frame3, text=self.amount[7], bd=1, relief="solid", width=12)
        self.h_amount.grid(row=8, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(7)).grid(row=8, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(7)).grid(row=8, column=5)

        ##Calculator (i)
        i_product = Label(frame3, text=items[8].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=9, column=0, padx=5)
        i_price = Label(frame3, text=items[8].getPrice(), bd=1, relief="solid", width=12).grid(row=9, column=1, padx=5)
        
        self.i_qty = Label(frame3, text=self.qty_ordered[7], bd=1, relief="solid", width=5)
        self.i_qty.grid(row=9, column=2, padx=5)
        
        self.i_amount = Label(frame3, text=self.amount[8], bd=1, relief="solid", width=12)
        self.i_amount.grid(row=9, column=3, padx=5)
        
        plus = Button(frame3, text='+', command=lambda:self.plus1(8)).grid(row=9, column=4)
        minus = Button(frame3, text='-', command=lambda:self.minus1(8)).grid(row=9, column=5)
        
        total_lbl = Label(frame3, text='Total').grid(row=10, column=1)
        self.total_qty = Label(frame3, text=sum(self.qty_ordered))
        self.total_qty.grid(row=10, column=2)
        self.total_amount = Label(frame3, text=sum(self.amount))
        self.total_amount.grid(row=10, column=3)
        save = Button(frame3, text=' Save ', command=self.save).grid(row=10, column=4, columnspan=2)
        
    def clear(self):
        self.invoice_ent.delete(0,'end')
        self.customer_ent.delete(0,'end')
        self.tax_ent.delete(0,'end')
        
##        print("After:\n\t%-15s    %4s    %5s    %5s\n" %("Description", "Cost", "Price", "Stock"))
##        for i in range (9):
##            print("\t%-15s    %4d    %5d    %5d\n" %(items[i].getName(),  items[i].getCost(), items[i].getPrice(), items[i].getStock()))
##        print(self.qty_ordered)
##        print(self.amount)
        
    def save(self):
        invoice = ("- Invoice No: "+ str(self.invoice_ent.get())) ##show info in message box
        customer_name = ("- Customer Name: "+ str(self.customer_ent.get()))
        tax = ("- Tax Id: "+ str(self.tax_ent.get()))
        total = ("- Total: "+str(sum(self.amount))+"baht")
        summary = (invoice+"\n"+customer_name+"\n"+tax+"\n"+total)
        tkinter.messagebox.showinfo('Save Sell', str(summary))

        ##save sale-info into file
##        file_name = "Invoice_"+str(self.invoice_ent.get())+".txt"
##        outfile = open(file_name,"w")
##        outfile.write("Midtown Stationary \t\t\t\t\tInvoice\n--My books. My stationary. My store.--\n\n")
##        outfile.write("Bill To\n"+"Name: "+str(self.customer_ent.get())+"\n"+"Tax Id: "+str(self.tax_ent.get())+"\n\n"+"\t-------------------------------------------------\n\n")
##        outfile.write("\t%-15s    %5s    %8s    %6s\n" %("Description", "Price", "Quantity", "Amount"))
##        for i in range (9):
##            outfile.write("\t%-15s    %5d    %8d    %6d\n" %(items[i].getName(), items[i].getPrice(), self.qty_ordered[i], self.amount[i])) ##start editing here
##        outfile.write("\n\t%24s    %8d    %6d\n\n\t-------------------------------------------------\n" %("Total: ", sum(self.qty_ordered), sum(self.amount)))       
##        outfile.close()

        ##New layout for text file save out
        file_name = "Invoice_"+str(self.invoice_ent.get())+".txt"
        outfile = open(file_name,"w")
        outfile.write("Midtown Stationary \t\t\t\t\tInvoice\n--My books. My stationary. My store.--\n\n")
        now=datetime.now()
        border1="--------------------------------"
        border2="---------------"
        outfile.write("%3s%8s\n%32s%14s%15s\n| Name     | %-17s |%9sDate | %8s    |\n| Tax id   | %-17s |%9sPO#  | %8s    |\n%32s%14s%15s\n\n"
                      %(" ","Customer",border1," ",border2,self.customer_ent.get()[:17:]," ",now.strftime('%x'),self.tax_ent.get()," ",self.invoice_ent.get(),border1," ",border2))
        border = "---------------------------------------------------------"
        outfile.write("%4s%57s\n%4s| No. |     Description     | QTY |  Price  |   Amount  |\n%4s%57s\n"%(" ",border, " "," ",border))
        for i in range(9):
            outfile.write("%4s|  %d  | %-20s|%3d  |  %5d  |   %5d   |\n"%(" ", (i+1), items[i].getName(), self.qty_ordered[i], items[i].getPrice(), self.amount[i]))
        outfile.write("%4s%57s\n%38s|  Total  |   %5d   |\n%38s-----------------------"%(" ",border, " ",sum(self.amount)," "))
        outfile.close()

        ##reset self.qty_ordered[] & self.amount[] list to 0
        for i in range(9):
            x = items[i].getStock()
            x -= self.qty_ordered[i]
            items[i].setStock(x)
            self.qty_ordered[i] = self.amount[i] = 0
            self.stockValueSet(i)

        ##save stock-info into file
        file = open("products.txt","w")
        for i in range(len(items)):
            text = items[i].getName() + "," + str(items[i].getCost()) + "," + str(items[i].getPrice()) + "," + str(items[i].getStock())
            file.write(text + "\n")
            self.stockValueSet(i)
        file.close()
        
        self.clear()

    def stockValueSet(self, i): ##show new stock & value
        if i==0:
            self.a_qty.config(text=self.qty_ordered[i])
            self.a_amount.config(text=self.amount[i])
        elif i==1:
            self.b_qty.config(text=self.qty_ordered[i])
            self.b_amount.config(text=self.amount[i])
        elif i==2:
            self.c_qty.config(text=self.qty_ordered[i])
            self.c_amount.config(text=self.amount[i])
        elif i==3:
            self.d_qty.config(text=self.qty_ordered[i])
            self.d_amount.config(text=self.amount[i])
        elif i==4:
            self.e_qty.config(text=self.qty_ordered[i])
            self.e_amount.config(text=self.amount[i])
        elif i==5:
            self.f_qty.config(text=self.qty_ordered[i])
            self.f_amount.config(text=self.amount[i])
        elif i==6:
            self.g_qty.config(text=self.qty_ordered[i])
            self.g_amount.config(text=self.amount[i])
        elif i==7:
            self.h_qty.config(text=self.qty_ordered[i])
            self.h_amount.config(text=self.amount[i])
        elif i==8:
            self.i_qty.config(text=self.qty_ordered[i])
            self.i_amount.config(text=self.amount[i])
        
        self.total_qty.config(text=sum(self.qty_ordered))
        self.total_amount.config(text=sum(self.amount))
        
    def plus1(self, i):
        x = 0
        x = self.qty_ordered[i] + 1
        if x <= items[i].getStock():
            self.qty_ordered[i] += 1
            self.amount[i] = items[i].getPrice()*self.qty_ordered[i]
            self.stockValueSet(i)

    def minus1(self, i):
        if self.qty_ordered[i]>0:
            self.qty_ordered[i] -= 1
            self.amount[i] = items[i].getPrice()*self.qty_ordered[i]
            self.stockValueSet(i)

    ########### FOR DIFF #############
    def updateInterface(self):
        pass
    #############################

####################################### STOCK PAGE #######################################

class StockPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        frame1 = Frame(self) ##menu bar
        frame1.pack()
        
        home_button = Button(frame1, text='Home',width=12, command=lambda: controller.show_frame(HomePage)).grid(row=1, column=0)
        purc_button = Button(frame1, text='Purchase',width=12, command=lambda: controller.show_frame(PurchasePage)).grid(row=1, column=1)
        sell_button = Button(frame1, text='Sell',width=12, command=lambda: controller.show_frame(SellPage)).grid(row=1, column=2)
        stock_button = Button(frame1, text='Stock',width=12, command=lambda: controller.show_frame(StockPage)).grid(row=1, column=3)
        logout_button = Button(frame1, text='Log out',width=12, command=lambda: controller.show_frame(LogInPage)).grid(row=1, column=4)

        frame3 = Frame(self)
        frame3.pack(side = LEFT)
        label = Label(frame3, text="Current stock")
        label.pack()
        
        frame2 = Frame(self) ##layout for selecting product 
        frame2.pack(expand=1) ## top horizontal header layout

        product = Label(frame2, text='PRODUCT', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=0)
        price = Label(frame2, text='COST', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=1)
        quantity = Label(frame2, text='QTY', bd=1, relief="solid", bg='green', width=5).grid(row=0, column=2)
        sub_total = Label(frame2, text='VALUE', bd=1, relief="solid", bg='green', width=12).grid(row=0, column=3)

        ##pen (a)
        a_product = Label(frame2, text=items[0].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=1, column=0, padx=5)
        a_price = Label(frame2, text=items[0].getCost(), bd=1, relief="solid", width=12).grid(row=1, column=1, padx=5)
        
        self.a_stock = Label(frame2, text=items[0].getStock(), bd=1, relief="solid", width=5)
        self.a_stock.grid(row=1, column=2, padx=5)
        
        self.a_value = Label(frame2, text=( items[0].getCost() * items[0].getStock() ), bd=1, relief="solid", width=12)
        self.a_value.grid(row=1, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(0)).grid(row=1, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(0)).grid(row=1, column=5)

        ##pencil (b)
        b_product = Label(frame2, text=items[1].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=2, column=0, padx=5)
        b_price = Label(frame2, text=items[1].getCost(), bd=1, relief="solid", width=12).grid(row=2, column=1, padx=5)
        
        self.b_stock = Label(frame2, text=items[1].getStock(), bd=1, relief="solid", width=5)
        self.b_stock.grid(row=2, column=2, padx=5)
        
        self.b_value = Label(frame2, text=( items[1].getCost() * items[1].getStock() ), bd=1, relief="solid", width=12)
        self.b_value.grid(row=2, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(1)).grid(row=2, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(1)).grid(row=2, column=5)

        ##Correction tape (c)
        c_product = Label(frame2, text=items[2].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=3, column=0, padx=5)
        c_price = Label(frame2, text=items[2].getCost(), bd=1, relief="solid", width=12).grid(row=3, column=1, padx=5)
        
        self.c_stock = Label(frame2, text=items[2].getStock(), bd=1, relief="solid", width=5)
        self.c_stock.grid(row=3, column=2, padx=5)
        
        self.c_value = Label(frame2, text=( items[2].getCost() * items[2].getStock() ), bd=1, relief="solid", width=12)
        self.c_value.grid(row=3, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(2)).grid(row=3, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(2)).grid(row=3, column=5)

        ##Rubber (d)
        d_product = Label(frame2, text=items[3].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=4, column=0, padx=5)
        d_price = Label(frame2, text=items[3].getCost(), bd=1, relief="solid", width=12).grid(row=4, column=1, padx=5)
        
        self.d_stock = Label(frame2, text=items[3].getStock(), bd=1, relief="solid", width=5)
        self.d_stock.grid(row=4, column=2, padx=5)
        
        self.d_value = Label(frame2, text=( items[3].getCost() * items[3].getStock() ), bd=1, relief="solid", width=12)
        self.d_value.grid(row=4, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(3)).grid(row=4, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(3)).grid(row=4, column=5)

        ##Highlighter (e)
        e_product = Label(frame2, text=items[4].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=5, column=0, padx=5)
        e_price = Label(frame2, text=items[4].getCost(), bd=1, relief="solid", width=12).grid(row=5, column=1, padx=5)
        
        self.e_stock = Label(frame2, text=items[4].getStock(), bd=1, relief="solid", width=5)
        self.e_stock.grid(row=5, column=2, padx=5)
        
        self.e_value = Label(frame2, text=( items[4].getCost() * items[4].getStock() ), bd=1, relief="solid", width=12)
        self.e_value.grid(row=5, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(4)).grid(row=5, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(4)).grid(row=5, column=5)

        ##Sharpener (f)
        f_product = Label(frame2, text=items[5].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=6, column=0, padx=5)
        f_price = Label(frame2, text=items[5].getCost(), bd=1, relief="solid", width=12).grid(row=6, column=1, padx=5)
        
        self.f_stock = Label(frame2, text=items[5].getStock(), bd=1, relief="solid", width=5)
        self.f_stock.grid(row=6, column=2, padx=5)
        
        self.f_value = Label(frame2, text=( items[5].getCost() * items[5].getStock() ), bd=1, relief="solid", width=12)
        self.f_value.grid(row=6, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(5)).grid(row=6, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(5)).grid(row=6, column=5)

        ##Stapler (g)
        g_product = Label(frame2, text=items[6].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=7, column=0, padx=5)
        g_price = Label(frame2, text=items[6].getCost(), bd=1, relief="solid", width=12).grid(row=7, column=1, padx=5)
        
        self.g_stock = Label(frame2, text=items[6].getStock(), bd=1, relief="solid", width=5)
        self.g_stock.grid(row=7, column=2, padx=5)
        
        self.g_value = Label(frame2, text=( items[6].getCost() * items[6].getStock() ), bd=1, relief="solid", width=12)
        self.g_value.grid(row=7, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(6)).grid(row=7, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(6)).grid(row=7, column=5)

        ##Paperclips (h)
        h_product = Label(frame2, text=items[7].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=8, column=0, padx=5)
        h_price = Label(frame2, text=items[7].getCost(), bd=1, relief="solid", width=12).grid(row=8, column=1, padx=5)
        
        self.h_stock = Label(frame2, text=items[7].getStock(), bd=1, relief="solid", width=5)
        self.h_stock.grid(row=8, column=2, padx=5)
        
        self.h_value = Label(frame2, text=( items[7].getCost() * items[7].getStock() ), bd=1, relief="solid", width=12)
        self.h_value.grid(row=8, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(7)).grid(row=8, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(7)).grid(row=8, column=5)

        ##Calculator (i)
        i_product = Label(frame2, text=items[8].getName(), bd=1, relief="solid", anchor=W, width=12).grid(row=9, column=0, padx=5)
        i_price = Label(frame2, text=items[8].getCost(), bd=1, relief="solid", width=12).grid(row=9, column=1, padx=5)
        
        self.i_stock = Label(frame2, text=items[8].getStock(), bd=1, relief="solid", width=5)
        self.i_stock.grid(row=9, column=2, padx=5)
        
        self.i_value = Label(frame2, text=( items[8].getCost() * items[8].getStock() ), bd=1, relief="solid", width=12)
        self.i_value.grid(row=9, column=3, padx=5)
        
        plus = Button(frame2, text='+', command=lambda:self.plus1(8)).grid(row=9, column=4)
        minus = Button(frame2, text='-', command=lambda:self.minus1(8)).grid(row=9, column=5)

        total = 0
        for i in range(len(items)):
            total +=( items[i].getCost()*items[i].getStock() )
        
        total_lbl = Label(frame2, text='Total').grid(row=10, column=2)

        self.total_value = Label(frame2, text=total)
        self.total_value.grid(row=10, column=3)
        
        save = Button(frame2, text='Refresh', command=self.save).grid(row=10, column=4, columnspan=2)

    def stockValueSet(self, i): ##show new stock & value
        if i==0:
            self.a_stock.config(text=items[i].getStock())
            self.a_value.config(text=items[i].getCost()*items[i].getStock())
        elif i==1:
            self.b_stock.config(text=items[i].getStock())
            self.b_value.config(text=items[i].getCost()*items[i].getStock())
        elif i==2:
            self.c_stock.config(text=items[i].getStock())
            self.c_value.config(text=items[i].getCost()*items[i].getStock())
        elif i==3:
            self.d_stock.config(text=items[i].getStock())
            self.d_value.config(text=items[i].getCost()*items[i].getStock())
        elif i==4:
            self.e_stock.config(text=items[i].getStock())
            self.e_value.config(text=items[i].getCost()*items[i].getStock())
        elif i==5:
            self.f_stock.config(text=items[i].getStock())
            self.f_value.config(text=items[i].getCost()*items[i].getStock())
        elif i==6:
            self.g_stock.config(text=items[i].getStock())
            self.g_value.config(text=items[i].getCost()*items[i].getStock())
        elif i==7:
            self.h_stock.config(text=items[i].getStock())
            self.h_value.config(text=items[i].getCost()*items[i].getStock())
        elif i==8:
            self.i_stock.config(text=items[i].getStock())
            self.i_value.config(text=items[i].getCost()*items[i].getStock())
        total = 0
        for i in range(len(items)):
            total += (items[i].getCost()*items[i].getStock())
        self.total_value.config(text=total)
        
    def plus1(self, i):
        items[i].incStock() ##increase quantity by 1
        self.stockValueSet(i)
        
    def minus1(self, i):
        items[i].decStock() ##decrease quantity by 1
        self.stockValueSet(i)

    def save(self):
        file = open("products.txt","w")
        for i in range(len(items)):
            text = items[i].getName() + "," + str(items[i].getCost()) + "," + str(items[i].getPrice()) + "," + str(items[i].getStock())
            file.write(text + "\n")
        file.close()

    def changelable(self):
        self.a_stock.config(text=items[0].getStock())
        self.a_value.config(text=items[0].getCost()*items[0].getStock())
        self.b_stock.config(text=items[1].getStock())
        self.b_value.config(text=items[1].getCost()*items[1].getStock())
        self.c_stock.config(text=items[2].getStock())
        self.c_value.config(text=items[2].getCost()*items[2].getStock())
        self.d_stock.config(text=items[3].getStock())
        self.d_value.config(text=items[3].getCost()*items[3].getStock())
        self.e_stock.config(text=items[4].getStock())
        self.e_value.config(text=items[4].getCost()*items[4].getStock())
        self.f_stock.config(text=items[5].getStock())
        self.f_value.config(text=items[5].getCost()*items[5].getStock())
        self.g_stock.config(text=items[6].getStock())
        self.g_value.config(text=items[6].getCost()*items[6].getStock())
        self.h_stock.config(text=items[7].getStock())
        self.h_value.config(text=items[7].getCost()*items[7].getStock())
        self.i_stock.config(text=items[8].getStock())
        self.i_value.config(text=items[8].getCost()*items[8].getStock())
        total = 0
        for i in range(len(items)):
            total += (items[i].getCost()*items[i].getStock())
        self.total_value.config(text=total)

    ########### FOR DIFF #########
    def updateInterface(self):
        self.changelable()
    #############################

app = iCash()
app.mainloop()


