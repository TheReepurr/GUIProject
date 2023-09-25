import tkinter as tk
from tkinter import messagebox

class PizzaMate:
    def __init__(self, root):
        self.root = root
        self.root.title('PizzaMate')

        # Welcome Screen
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack()
        tk.Label(self.welcome_frame, text='Welcome to PizzaMate!').pack()
        tk.Button(self.welcome_frame, text='Start Order', command=self.start_order).pack()

    def start_order(self):
        self.welcome_frame.pack_forget()

        # Pizza Selection Screen
        self.selection_frame = tk.Frame(self.root)
        self.selection_frame.pack()
        tk.Label(self.selection_frame, text='Select your pizza').pack()
        self.pizza_var = tk.StringVar()
        self.pizza_var.set('Margherita')
        pizza_options = ['Margherita', 'Pepperoni', 'BBQ Chicken', 'Hawaiian']
        for option in pizza_options:
            tk.Radiobutton(self.selection_frame, text=option, variable=self.pizza_var, value=option).pack()
        tk.Button(self.selection_frame, text='Next', command=self.order_summary).pack()

    def order_summary(self):
        self.selection_frame.pack_forget()

        # Order Summary Screen
        self.summary_frame = tk.Frame(self.root)
        self.summary_frame.pack()
        tk.Label(self.summary_frame, text='Your Order').pack()
        tk.Label(self.summary_frame, text=self.pizza_var.get()).pack()
        
        # Checkout Screen
        tk.Label(self.summary_frame, text='Enter your delivery details:').pack()
        self.address_entry = tk.Entry(self.summary_frame)
        self.address_entry.pack()
        
        tk.Button(self.summary_frame, text='Place Order', command=self.place_order).pack()

    def place_order(self):
        address = self.address_entry.get()
        
        if not address:
            messagebox.showerror('Error', 'Please enter a delivery address.')
            return
        
        messagebox.showinfo('Success', f'Your {self.pizza_var.get()} pizza will be delivered to {address}.')

root = tk.Tk()
app = PizzaMate(root)
root.mainloop()
