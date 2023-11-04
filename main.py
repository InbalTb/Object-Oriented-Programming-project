import Store, Vehicle, Customer, gui
from ExceptionVehicle import ExceptionVehicle

def main():
    try:
        store = Store.Store("vehicles.csv", "customers.csv")
        store.print_customers()
        store.print_vehicles()
        new_vehicle = Vehicle.Vehicle([12345678, "car", "Tesla", "Model A", 2021, 186853])
        store.add_vehicle(new_vehicle)
        store.remove_vehicle(new_vehicle.licence_plate)
        store.print_vehicles_list(store.get_all_by_manufacturer("Kia"))
        vlist = store.get_all_by_manufacturer("BMW")
        if len(vlist) > 0:
            store.print_vehicles_list(vlist)
        store.print_vehicles_list(store.get_all_by_price_under(15000))
        most_expensive_vehicle = store.get_most_expensive_vehicle()
        if most_expensive_vehicle != None:
            most_expensive_vehicle.print_me()
        new_customer = Customer.Customer(["12345", "Bimba", "Tel-Aviv", "0503836701", "F"])
        store.add_customer(new_customer)
        new_customer.print_me()
        store.remove_customer("12345")
        store.print_vehicles_list(store.get_all_collector())
        vlist = store.get_all_by_KM_under(15000)
        if len(vlist) > 0:
            store.print_vehicles_list(vlist)
        store.print_customer_list(store.get_all_VIP())
        store.print_customer_list(store.get_all_entitled())
        gui.creategui(store)

    except ExceptionVehicle as e:
        print(f"error: {e}")
    except:
        print('Exception!!!')
        raise
    else:
        print("\nmain finished with no errors")

main()
