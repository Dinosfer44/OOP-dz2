class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        print (f"Марка автомобиля: {self.make}, модель: {self.model}, год: {self.year}")
class Car(Vehicle):
    def __init__(self, make, model, year,):
        super().__init__(make, model, year)
    def start_engine(self):
        print (f"{self.make} {self.model} {self.year}-го года завелся!")
class Bycicle (Vehicle):
    def __init__(self, make, model, year, ):
        super().__init__(make, model, year)
    def ring_bell(self):
        print ("Звонок велосипела звенит!")


mashina = Vehicle ("Мерседес", "Ешка", "2024")
mashina.get_info()
vot = Car ("Мерседес", "Ешка", "2024")
vot.start_engine()
velik = Bycicle ("", "", "")
velik.ring_bell()