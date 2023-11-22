# Instanciation of a Client CLass to create Client Datas. 

class Client: 
    def __init__(self) :
        import Calc_funcs.income_taxation as it 
        import CreateData.createdatafuncs as cd 
        import random

        surname_gender = cd.surnames_data()[random.randint(0, len(cd.surnames_data()) - 1)]        
        self.name = surname_gender[0]
        self.age = random.randint(18,99)
        self.gender = surname_gender[1]
        self.annual_income = random.randint(0, 1000000)
        self.number_of_children = random.randint(0,4)
        self.is_married = random.choice([True, False])
        self.annual_income_taxation = it.income_taxation(
            self.is_married, 
            self.number_of_children, 
            self.annual_income
        )