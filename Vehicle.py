from ExceptionProcess import ExceptionProcess


class Vehicle:
    @staticmethod
    def check_valid_licence(licence_plate):
        max_digits_in_license_plate = 8
        ExceptionProcess.CheckIntNumbers(licence_plate, 0, 10 ** max_digits_in_license_plate - 1, Vehicle)

    def __init__(self, vehicle_parameters):
        self.licence_plate = int(vehicle_parameters[0])
        self.vehicle_type = vehicle_parameters[1]
        self.manufacturer = vehicle_parameters[2]
        self.model = vehicle_parameters[3]
        self.year = int(vehicle_parameters[4])
        self.price = int(vehicle_parameters[5])

        ExceptionProcess.CheckSTR(self.vehicle_type, Vehicle)
        ExceptionProcess.CheckSTR(self.manufacturer, Vehicle)
        ExceptionProcess.CheckSTR(self.model, Vehicle)
        self.check_valid_licence(self.licence_plate)
        ExceptionProcess.CheckIntNumbers(self.price, 1000, 3000000, Vehicle)
        ExceptionProcess.CheckIntNumbers(self.year, 1000, 9999, Vehicle)

    def print_me(self):
        print(f"----{self.licence_plate}----")
        print(f"type: {self.vehicle_type}")
        print(f"manufacturer: {self.manufacturer}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")
        print(f"price: {self.price} NIS")

    def __str__(self):
        return f"{self.licence_plate}, {self.vehicle_type}, {self.manufacturer}, {self.model}, " \
               f"{self.year}, {self.price}"

    def __repr__(self):
        return self.__str__()

    def IsCollector(self):
        return False
