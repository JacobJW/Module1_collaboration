# Module3 Lab
class Vehicle():
    'Contains type, year, make, model, doors, roof'
    def __init__(self,name):
        self.name = name
        self.type = 'unknown'

class Automobile(Vehicle):
    'Subclass of vehicle'
    def __init__(self,name):
        super().__init__(name)
        self.type = 'automobile'
        self.year = '1901'
        self.make = 'unknown'
        self.model = 'unknown'
        self.doors = '0'
        self.roof = 'n/a'
    def __str__(self):
        return ('Vehicle: %s\nType: Automobile\nYear: %s\nMake: %s\nModel: %s\nDoor Count: %s\nRoof Type: %s') % (self.name,self.year,self.make,self.model,self.doors,self.roof)

def add_car(car,year,make,model,doors,roof):
    car = Automobile(car) # create an automobile object
    car.year = year
    car.make = make
    car.model = model
    car.doors = doors
    car.roof = roof
    return(car) # return object

def car_entry():
    'Gets input needed to add a car record'
    name = input('Enter the name of your vehicle: ')
    year = input('Enter the production year: ')
    make = input('Enter the make: ')
    model = input('Enter the model: ')
    doors = input('How many doors in the vehicle?: ')
    roof = input('What type of roof does the vehicle have? n/a, sun roof, etc:')

    print(add_car(name,year,make,model,doors,roof))


car_entry(); # Run the entry program