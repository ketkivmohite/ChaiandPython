# 1. Basic class and Object
# Problem : Create a Car class with attributes like brand and model .
#  Then create an instance of this class . 

class Car:
    total_car = 0 

    def __init__(self, brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"


# 2. Class Method and Self
# Problem : Add a method to the Car class that displays 
#     the full name of the car(brand and model ) 

    def full_name(self):
        return f"{self.brand}{self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
# 3. Inheritance
# Problem : Create an ELectricCar class that 
# inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model) 
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


# my_new_Car = Car("Tata","Safari")
# print(my_new_Car.brand)
# print(my_new_Car.model)
# print(my_new_Car.full_name())

# my_car = Car('Toyota','Corolla')
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_tesla = ElectricCar("Tesla","Model S", "85 kwh")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# safari = Car("Tata","Safari")
# safariThree = Car("Tata","Safari")

# print(safari.fuel_type())
# print(safari.total_car)


# print(Car.total_car)

# my_car = Car("Tata","Safari")
# # my_car.model = "City"
# Car("Tata","Nexon")
# my_car.model = "City"

# print(my_car.model)

# print(my_car.general_description())

class Battery:
    def battery_info(self):
        return "this is battery"
    

class Engine:
    def engine_info(self):
        return "this is engine"
    pass

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())







