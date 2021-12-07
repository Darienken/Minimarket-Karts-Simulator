import tkinter as tk
from tkinter.constants import BOTH
import model


#<!----------Main Class--------->
class minimarket_app(tk.Frame):
	#<!-----initizialing frame------------->
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		options={
		"height":1000,
		"width":2000,
		}
		self.config(**options)
		self.widgets()

	#<!-----------Creating widgets--------------->
	def widgets(self):
		
		#Vars
		self.customers=tk.IntVar()
		self.waiting_customers=tk.IntVar()
		self.avaible_carts=tk.IntVar()
		self.avaible_carts.set(25)
		
		#Labels
		tk.Label(self, text="Customers:", font="500").place(x=400,y=50)
		tk.Label(self, textvariable=self.customers, font="500").place(x=400,y=75)
		tk.Label(self, text="Waiting Customers:", font="500").place(x=400,y=120)
		tk.Label(self, textvariable=self.waiting_customers, font="500").place(x=400,y=146)
		tk.Label(self, text="Carts:", font="500").place(x=895,y=50)
		tk.Label(self, text="25", font="500").place(x=917,y=75)
		tk.Label(self, text="Available Carts:", font="500").place(x=830,y=110)
		tk.Label(self, textvariable=self.avaible_carts, font="500").place(x=919,y=137)
		
		
		#Butttons
		tk.Button(self, text="Add Customer", command=lambda:self.add_customer(), font="500").place(x=405,y=600)
		tk.Button(self, text="End Shop", command=lambda:self.end_shop(), font="500").place(x=560,y=600)
		tk.Button(self, text="Pay", command=lambda:self.pay(), font="500").place(x=700,y=600)
		tk.Button(self, text="No Buy", command=lambda:self.no_buy(), font="500").place(x=800,y=600)
		tk.Button(self, text="Retire", command=lambda:self.retire(), font="500").place(x=900,y=600)
		
		

		#Box One
		tk.Label(self, text="Box One:", font="500").place(x=400,y=300)
				
		#Box Two
		tk.Label(self, text="Box Two:", font="500").place(x=650,y=300)
		
		
		#Box Three
		tk.Label(self, text="Box Three:", font="500").place(x=870,y=300)
		
		
	#Func to add customers
	def add_customer(self):
		#Add customers
		if self.customers.get() >= 25 or self.avaible_carts.get() <= 0:
			self.waiting_customers.set(self.waiting_customers.get()+1)
		else:
			self.customers.set(self.customers.get()+1)
			#Append customers to list
			model.customers_li.append(self.customers.get())
		#Lower the avaible carts
		if self.customers.get() <= 25 and self.avaible_carts.get() > 0:
			self.avaible_carts.set(self.avaible_carts.get()-1)
	
	#Func to end shop
	def end_shop(self):
		#Remove Costumers
		if self.customers.get() <= 25 and self.customers.get() > 0:#and self.waiting_customers.get() == 0:
			self.customers.set(self.customers.get()-1)
			box1_li, box2_li, box3_li=model.append_costumer()
			tk.Label(self, text=box1_li, font="500").place(x=300,y=400)
			tk.Label(self, text=box2_li, font="500").place(x=600,y=400)
			tk.Label(self, text=box3_li, font="500").place(x=900,y=400)
		
	
	#Func to no buy
	def no_buy(self):
		#Remove Waiting Costumers if there is
		if self.waiting_customers.get() > 0:
			self.waiting_customers.set(self.waiting_customers.get()-1)
			box1_no_buy, box2_no_buy, box3_no_buy=model.no_buyers()
			tk.Label(self, text=box1_no_buy, font="500").place(x=300,y=500)
			tk.Label(self, text=box2_no_buy, font="500").place(x=600,y=500)
			tk.Label(self, text=box3_no_buy, font="500").place(x=900,y=500)
	
	#Func to pay
	def pay(self):
		total_costumers,box1_li, box2_li, box3_li=model.delete_customers()
		#Set avaible carts plus
		self.avaible_carts.set(self.avaible_carts.get()+total_costumers)
		if self.waiting_customers.get() > 0:
			#Set customers
			if self.avaible_carts.get() > self.waiting_customers.get():
				self.customers.set(self.customers.get()+self.waiting_customers.get())
			else:
				self.customers.set(self.customers.get()+self.avaible_carts.get())
			#Set avaible carts and waiting costumers (less)
			if self.avaible_carts.get() > self.waiting_customers.get():
				self.avaible_carts.set(self.avaible_carts.get()-self.waiting_customers.get())
				self.waiting_customers.set(0)
			elif self.waiting_customers.get() > self.avaible_carts.get():
				self.waiting_customers.set(self.waiting_customers.get()-self.avaible_carts.get())
				self.avaible_carts.set(0)
			else:
				self.avaible_carts.set(0)
				self.waiting_customers.set(0)
				
		tk.Label(self, text=box1_li, font="500").place(x=300,y=400)
		tk.Label(self, text=box2_li, font="500").place(x=600,y=400)
		tk.Label(self, text=box3_li, font="500").place(x=900,y=400)
	
	def retire(self):
		box1_no_buy, box2_no_buy, box3_no_buy=model.retire()
		tk.Label(self, text=box1_no_buy, font="500").place(x=300,y=500)
		tk.Label(self, text=box2_no_buy, font="500").place(x=600,y=500)
		tk.Label(self, text=box3_no_buy, font="500").place(x=900,y=500)

#<!------Setting root and Running app-------->
if __name__=='__main__':
	app=tk.Tk()
	minimarket_app(app).pack(expand=True, fill="both")
	app.title("MiniMarket App")
	app.iconbitmap("C:/Users/Vivi/OneDrive/Escritorio/Didackmon_User001/thewise king hacka/Python/Graphic Applications/GUIs with classes/MiniMarket_Simulator/imgs/minimark.ico")
	app.mainloop()