import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ExceptionVehicle import ExceptionVehicle
from Vehicle import Vehicle

class App:
    def _add_label(self, master, text, size):
        l = tk.Label(master, justify='center', text=text, font=("d Bold", size))
        l.pack(side="top", fill="x")
        return l

    def _add_button(self, master, command, text):
        label_text = f"Last function: '{text}'"
        b = tk.Button(master, justify='center', command=lambda: (self._lbl_function_set_text(label_text), command()), text=text)
        b.pack(side="top", fill="x")

    def _add_combo(self, master, values):
        n = tk.StringVar()
        c = ttk.Combobox(master, width=27, textvariable=n)
        c['values'] = values
        c.pack(side="top", fill="x")
        return c

    def _add_enrty(self, master, default_value):
        e = tk.Entry(master)
        e.pack(side="top", fill="x")
        if default_value != None:
            e.insert(-1, default_value)
        return e

    def _resize_window(self, root):
        width = 400
        height = 700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

    def __init__(self, root, store):
        self.store = store
        root.title("Inbal's Store - buy a car")
        self._resize_window(root)

        self.lbl_function = self._add_label(root, "(Selected function)", 10)
        self._add_label(root, "Print info", 18)

        buttons = ((self.print_all_customers, 'Print all customers'),
                   (self.print_all_vehicles, "Print all vehicles"),
                   (self.print_all_collector_vehicles, 'Print all collector vehicles'),
                   (self.print_all_vip_customers, 'Print all VIP customers'),
                   (self.print_all_entitled, "Print all entitled"),
                   )
        for b in buttons:
            self._add_button(root, command=b[0], text=b[1])

        self._add_label(root, "Search info", 18)

        manufacturers_list = self.store.get_manufacturers()
        c = self._add_combo(root, manufacturers_list)
        self._add_button(root, command=lambda c=c: self.print_vehicle_by_manufacturer(c.get()), text="Print by manufacturer")

        button_with_entry = (
            (self.print_all_vehicles_under_km, "Get all vehicles under KM", "KM"),
            (self.print_all_vehicles_under_price, "Get all vehicles under price", "price"),
            (self.print_customer_by_id, "Get customer", "Customer ID"),
            (self.get_and_remove_customer, "Get and remove customer", "Customer ID"),
            (self.remove_vehicle, "Remove vehicle", "License plate"),
            (self.add_vehicle, "Add vehicle", '12345678, "car", "Tesla", "Model A", 2021, 186853'),
        )
        for be in button_with_entry:
            f = tk.Frame(master=root, bd=1, relief=tk.SUNKEN)
            e = self._add_enrty(f, be[2])
            self._add_button(f, command=lambda be=be, e=e: be[0](e.get()), text=be[1])
            f.pack(side="top", fill="x", pady=7)

        f = tk.Frame(master=root, bd=1, relief=tk.SUNKEN)
        e = self._add_enrty(f, "")
        self._entry_disabled_set_text(e, "License plate")
        self._add_button(f, command=lambda e=e: self.get_all_expensive_vehicles(e), text="Get the most expensive vehicle")
        f.pack(side="top", fill="x", pady=10)

    def print_all_customers(self):
        self.store.print_customers()

    def print_all_vehicles(self):
        self.store.print_vehicles()

    def print_all_collector_vehicles(self):
        ac = self.store.get_all_collector()
        if ac:
            self.store.print_vehicles_list(ac)

    def print_all_vip_customers(self):
        av = self.store.get_all_VIP()
        if av:
            self.store.print_customer_list(av)

    def print_all_entitled(self):
        ae = self.store.get_all_entitled()
        if ae:
            self.store.print_customer_list(ae)

    def print_all_vehicles_under_price(self, value):
        try:
            price = int(value)
            self.store.print_vehicles_list(self.store.get_all_by_price_under(price))
        except ExceptionVehicle as e:
            messagebox.showinfo("Error", e.messege)
        except ValueError as ve:
            messagebox.showinfo("Error", "Invalid input, Enter an integer only!")

    def print_all_vehicles_under_km(self, value):
        try:
            km = int(value)
            self.store.print_vehicles_list(self.store.get_all_by_KM_under(km))
        except ExceptionVehicle as e:
            messagebox.showinfo("Error", e.messege)
        except ValueError as ve:
            messagebox.showinfo("Error", "Invalid input, Enter an integer only!")

    def print_vehicle_by_manufacturer(self, value):
        try:
            manufacturer = value
            self.store.print_vehicles_list(self.store.get_all_by_manufacturer(manufacturer))
        except ExceptionVehicle as e:
            messagebox.showinfo("Error", e.messege)

    def _lbl_function_set_text(self, text):
        self.lbl_function.config(text=text)

    def _entry_disabled_set_text(self, entry, text):
        entry.configure(state='normal')
        entry.delete("0", "end")
        entry.insert(-1, text)
        entry.configure(state='disabled')

    def get_all_expensive_vehicles(self, entry):
        mev = self.store.get_most_expensive_vehicle()
        if mev:
            self._entry_disabled_set_text(entry, str(mev))

    def _print_customer(self, id_customer):
        try:
            c = self.store.get_customer(id_customer)
            if c:
                c.print_me()
                return c

            messagebox.showinfo("Error", f"Customer with id '{id_customer}' not found")
        except ExceptionVehicle as e:
            messagebox.showinfo("Error", e.messege)

    def print_customer_by_id(self, value):
        id_customer = value
        self._print_customer(id_customer)

    def get_and_remove_customer(self, value):
        id_customer = value
        c = self._print_customer(id_customer)
        if c:
            self.store.remove_customer(id_customer)

    def remove_vehicle(self, value):
        try:
            license_plate = int(value)
            self.store.remove_vehicle(license_plate)
        except ExceptionVehicle as e:
            messagebox.showinfo("Error", e.messege)
        except ValueError as ve:
            messagebox.showinfo("Error", "Invalid input, Enter an integer only!")

    def add_vehicle(self, value):
        try:
            vehicle_str = value
            new_vehicle = Vehicle(vehicle_str.split(','))
            self.store.add_vehicle(new_vehicle)
        except ExceptionVehicle as e:
            messagebox.showinfo("Error", e.messege)
        except ValueError as ve:
            messagebox.showinfo("Error", "Invalid Vehicle comma delimited input")

def creategui(store):
    root = tk.Tk()
    App(root, store)
    root.mainloop()