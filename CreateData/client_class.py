# Instanciation of a Client CLass to create Client Datas. 

class Client: 
    def __init__(self, name, age, gender, annual_income, 
                 number_of_children, is_married
                 ) :
        import Calc_funcs.income_taxation as it 
        self.name = name
        self.age = age
        self.gender = gender
        self.annual_income = annual_income
        self.number_of_children = number_of_children
        self.is_married = is_married
        self.annual_income_taxation = it.income_taxation(
            self.is_married, 
            self.number_of_children, 
            self.annual_income
        )