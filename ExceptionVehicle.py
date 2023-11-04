class ExceptionVehicle(Exception):
    def __init__(self, messege, level, source):
        self.messege = messege
        self.level = level
        self.source = source.__name__

    def __str__(self):
        return f"{self.messege}, Level of severity is {self.level}, source object: {self.source}"

    def __repr__(self):
        return self.__str__()






