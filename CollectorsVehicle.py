import Vehicle
from ExceptionProcess import ExceptionProcess


class CollectorsVehicle(Vehicle.Vehicle):
    def __init__(self, vehicle_parameters):
        super().__init__(vehicle_parameters)
        self.KM = int(vehicle_parameters[6])
        self.Old_owners = int(vehicle_parameters[7])
        self.Test = vehicle_parameters[8]
        ExceptionProcess.CheckIntNumbers(self.KM, 0, None, CollectorsVehicle)
        ExceptionProcess.CheckIntNumbers(self.Old_owners, 0, None, CollectorsVehicle)
        ExceptionProcess.CheckSTR(self.Test, CollectorsVehicle)

    def print_me(self):
        super().print_me()
        print(f"KM: {self.KM}")
        print(f"Old_owners: {self.Old_owners}")
        print(f"Test: {self.Test}")

    def __str__(self):
        vehicle_str = super().__str__()
        return vehicle_str + f", {self.KM}, {self.Old_owners}, {self.Test}"

    def IsCollector(self):
        return True
