
# Initializes the list of tuples (surname, gender). Will be reused later in the "create_data()" func. 
# Returns a list of (name, gender) tuples. 

def surnames_data() :

    variable_list = []

    open_file =  open("CreateData/surnames.txt", "r")
    for line in open_file : 
        file_line = line.strip()
        surname, gender = file_line.split(",")
        variable_list.append((surname, gender))
    open_file.close()

    return variable_list

def emails_data() : 

    variable_list = []

    open_file =  open("CreateData/emails.txt", "r")
    for line in open_file : 
        file_line = line.strip()
        variable_list.append((file_line))
    open_file.close()

    return variable_list

# Create random data. Should be stocked into a variable. 
# Returns JSON formated DATAS. 

def create_data() : 

    from CreateData.client_class import Client
    import CreateData.createdatafuncs as cd 
    import random

    data = {}
    identifiant = {}
    name = {}
    gender = {}
    age = {}
    number_of_children = {}
    is_married = {}
    annual_income = {}
    annual_income_tax = {}
    
    i = 0 
    while i <= 200 : 
        new_client = Client()
        identifiant[str(i)] = i
        name[str(i)] = new_client.name
        gender[str(i)] = new_client.gender
        age[str(i)] = new_client.age
        number_of_children[str(i)] = new_client.number_of_children
        is_married[str(i)] = new_client.is_married
        annual_income[str(i)] = new_client.annual_income
        annual_income_tax[str(i)] = new_client.annual_income_taxation

        i += 1

    data = {
        'identifiant' : identifiant, 
        'name' : name, 
        'gender' : gender, 
        'age' : age,
        'number_of_children' : number_of_children,
        'is_married' : is_married,
        'annual_income' : annual_income,
        'annual_income_tax' : annual_income_tax
        
    }

    return data


# Write data on a JSON File. Be sure to specify the path correctly. 

def json_dump(filename, variable_name) :

    import json

    with open(filename, "w") as json_file :
        json.dump(variable_name, json_file, indent=4)

    return None

# Collect JSON Data. 

def json_collect(filename) : 
    import json
    with open(filename, "r") as json_file : 
        data = json.load(json_file)

        return data