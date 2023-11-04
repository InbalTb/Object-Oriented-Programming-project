from ExceptionVehicle import ExceptionVehicle


class ExceptionProcess:
    @staticmethod
    def CheckIntNumbers(var, minimum, maximum, source):
        if type(var) != int:
            raise ExceptionVehicle(f"{var} is not an integer ", 5, source)

        if minimum != None and var < minimum:
            raise ExceptionVehicle(f"{var} is out of range - smaller than allowed: {minimum}", 4, source)

        if maximum != None and var > maximum:
            raise ExceptionVehicle(f"{var} is out of range - larger than allowed: {maximum}", 4, source)

    @staticmethod
    def CheckSTR(var, source):
        if type(var) != str:
            raise ExceptionVehicle(f"{var} is not a string ", 5, source)

        if len(var) == 0:
            raise ExceptionVehicle(f"Empty string", 5, source)

    @staticmethod
    def CheckList(var, source):
        if type(var) != list:
            raise ExceptionVehicle(f"{var} is not a list ", 5, source)

        if len(var) == 0:
            raise ExceptionVehicle(f"Empty list", 5, source)
