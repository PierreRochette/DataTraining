import json 
import Calc_funcs.income_taxation as income_taxation

with open("clients.json", "r") as file : 
    data = json.load(file)



personnal_income_taxation_data = []

i = 0 
while i < len(data) - 1 :  

    family_quotient = income_taxation.total_shares(
        income_taxation.children_shares(data[i]["number_of_children"]), 
        income_taxation.mariage_shares(data[i]["married"])
    )

    income_tax = income_taxation.income_taxation(
        family_quotient, 
        data[i]["annual_income"]
    )

    tax_data = {
        "name" : data[i]["name"], 
        "gender" : data[i]["gender"], 
        "annual_income" : data[i]["annual_income"], 
        "income_taxatiion" : income_tax
    }

    personnal_income_taxation_data.append(tax_data)

    i += 1 

print(personnal_income_taxation_data)

