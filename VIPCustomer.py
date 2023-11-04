import Customer
from ExceptionProcess import ExceptionProcess

class VIPCustomer(Customer.Customer):
    def __init__(self, customer_parameters):
        super().__init__(customer_parameters)
        self.startDate = customer_parameters[5]
        self.birthDate = customer_parameters[6]
        _joiningPresent = customer_parameters[7]
        ExceptionProcess.CheckSTR(self.startDate, VIPCustomer)
        ExceptionProcess.CheckSTR(self.birthDate, VIPCustomer)
        ExceptionProcess.CheckSTR(_joiningPresent, VIPCustomer)
        self.joiningPresent = _joiningPresent.upper() == "TRUE"

    def __str__(self):
        customer_str = super().__str__()
        return customer_str + f"{self.startDate}, {self.birthDate}, {self.joiningPresent}"

    def getPresent(self):
        if self.joiningPresent == True:
            print("Congratulations here is your present")
            self.joiningPresent = False
        else:
            print("present your got already You")

    def isVIPcustomer(self):
        return True

