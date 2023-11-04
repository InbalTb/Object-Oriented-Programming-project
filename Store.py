import csv
from Vehicle import Vehicle
from CollectorsVehicle import CollectorsVehicle
from Customer import Customer
from VIPCustomer import VIPCustomer
from ExceptionProcess import ExceptionProcess


class Store:
    def __init__(self, vehicle_csv_filename, customers_csv_filename):
        self.vehicles = csv_with_title_to_object_list_vehicle(vehicle_csv_filename)
        self.customers = csv_with_title_to_object_list_customer(customers_csv_filename)

    def get_manufacturers(self):
        vset = set()
        for v in self.vehicles:
            vset.add(v.manufacturer)
        return list(vset)

    def print_vehicles(self):
        for v in self.vehicles:
            print(v)

    def get_vehicle(self, licence_plate):
        Vehicle.check_valid_licence(licence_plate)
        for v in self.vehicles:
            if v.licence_plate == licence_plate:
                return v
        return None

    def add_vehicle(self, vehicle):
        v = self.get_vehicle(vehicle.licence_plate)
        if v == None:
            self.vehicles.append(vehicle)
            return True
        return False

    def remove_vehicle(self, licence_plate):
        Vehicle.check_valid_licence(licence_plate)
        v = self.get_vehicle(licence_plate)
        if v != None:
            self.vehicles.remove(v)
            return True
        return False

    def get_all_by_manufacturer(self, manufacturer):
        ExceptionProcess.CheckSTR( manufacturer, Store)
        manufacturer_list = []
        for v in self.vehicles:
            if v.manufacturer == manufacturer:
                manufacturer_list.append(v)
        return manufacturer_list

    def get_all_by_price_under(self, max_price):
        ExceptionProcess.CheckIntNumbers(max_price, 0, None, Store)
        vehicles_list = []
        for v in self.vehicles:
            if v.price < max_price:
                vehicles_list.append(v)
        return vehicles_list

    def print_vehicles_list(self, vehicles_list):
        ExceptionProcess.CheckList(vehicles_list, Store)
        for item in vehicles_list:
            item.print_me()

    def get_most_expensive_vehicle(self):
        temp = 0
        most_expensive_vehicle = None
        for v in self.vehicles:
            if temp < v.price:
                temp = v.price
                most_expensive_vehicle = v

        return most_expensive_vehicle

    def print_customers(self):
        for c in self.customers:
            print(c)

    def print_customer_list(self, customer_list):
        ExceptionProcess.CheckList(customer_list, Store)
        for c in customer_list:
            c.print_me()

    def get_customer(self, customer_id):
        ExceptionProcess.CheckSTR(customer_id, Store)
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def add_customer(self, customer):
        c = self.get_customer(customer.customer_id)
        if c == None:
            self.customers.append(customer)
            return True
        return False

    def remove_customer(self, customer_id):
        ExceptionProcess.CheckSTR(customer_id, Store)
        c = self.get_customer(customer_id)
        if c != None:
            self.customers.remove(c)
            return True
        return False

    def get_all_collector(self):
        vlist = []
        for v in self.vehicles:
            if v.IsCollector() == True:
                vlist.append(v)
        return vlist

    def get_all_by_KM_under(self, KM):
        ExceptionProcess.CheckIntNumbers(KM, 1, None, Store)
        vlist = []
        for v in self.get_all_collector():
            if v.KM < KM:
                vlist.append(v)
        return vlist

    def get_all_VIP(self):
        viplist= []
        for c in self.customers:
            if c.isVIPcustomer() == True:
                viplist.append(c)
        return viplist

    def get_all_entitled(self):
        entitledlist = []
        for vip in self.get_all_VIP():
            if vip.joiningPresent == True:
                entitledlist.append(vip)
        return entitledlist


def row_to_object_vehicle(row):
    if len(row) > 6:
        return CollectorsVehicle(row)
    else:
        return Vehicle(row)

def row_to_object_customer(row):
    if len(row) > 5:
        return VIPCustomer(row)
    else:
        return Customer(row)

def csv_with_title_to_object_list_vehicle(csv_filename):
    list = []

    with open(csv_filename, newline='') as csvfile:
        read = csv.reader(csvfile)
        # skip first line - titles
        next(read)

        for row in read:
            temp = row_to_object_vehicle(row)
            list.append(temp)

        return list

def csv_with_title_to_object_list_customer(csv_filename):
    list = []

    with open(csv_filename, newline='') as csvfile:
        read = csv.reader(csvfile)
        # skip first line - titles
        next(read)

        for row in read:
            temp = row_to_object_customer(row)
            list.append(temp)

        return list


