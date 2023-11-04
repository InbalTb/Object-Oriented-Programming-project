from ExceptionProcess import ExceptionProcess

class Customer:
    def __init__(self, customer_parameters):
        self.customer_id = customer_parameters[0]
        self.name = customer_parameters[1]
        self.address = customer_parameters[2]
        self.phone_number = customer_parameters[3].strip()
        self.gender = customer_parameters[4].strip()

        ExceptionProcess.CheckSTR(self.customer_id, Customer)
        ExceptionProcess.CheckSTR(self.name, Customer)
        ExceptionProcess.CheckSTR(self.address, Customer)
        ExceptionProcess.CheckSTR(self.phone_number, Customer)
        digits_in_phone_number = 10
        if len(self.phone_number) != digits_in_phone_number:
            print(f"invalid phone number {self.phone_number}")

        if self.gender not in ['F', 'M']:
            self.gender = 'F'

    def isVIPcustomer(self):
        return False

    def print_me(self):
        print(f"----{self.customer_id}----")
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"phone_number: {self.phone_number}")
        print(f"gender: {self.gender}")

    def __str__(self):
        return f"{self.customer_id}, {self.name}, {self.address}, {self.phone_number}, " \
               f"{self.gender}"

    def __repr__(self):
        return self.__str__()
