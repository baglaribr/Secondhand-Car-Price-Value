import datetime
# parent class
class CarValuation():
    "Car model and crash info"
    def __init__(self,brand,model_year,recorded_crash,painted_part,replaced_part,new_car_price):
        self.brand = brand
        self.model_year = model_year
        self.recorded_crash = recorded_crash
        self.painted_part = painted_part
        self.replaced_part = replaced_part
        self.new_car_price = new_car_price

    def crash_record(self):
        
        """
            recorded crash number and crash fix type (paint or part replacement)
        """
        return "Number of recorded crash: {}\nPainted part: {}\nReplaced part: {}\n".format(self.recorded_crash, self.painted_part, self.replaced_part)

    def __str__(self):
        return "Brand is {} Car Value is {} TL".format(self.brand, self.value)
# child class 
class Value(CarValuation):
    # inheritance
    def __init__(self,brand,model_year,recorded_crash,painted_part,replaced_part,new_car_price):
        super().__init__(brand,model_year,recorded_crash,painted_part,replaced_part,new_car_price)
    
    def value(self):
        # secondhand price calculation
        year = datetime.datetime.now().year
        value = self.new_car_price - 500*self.painted_part - 1000*self.replaced_part - 500*self.recorded_crash - (year-self.model_year)*12000
        return "Mean sale price: {} TL".format(value)

    
    
c1 = Value("Hyundai Getz", 2005, 2, 3, 3,450000) 
c2 = Value("Toyota Corolla", 2017, 1, 2, 0, 630000)