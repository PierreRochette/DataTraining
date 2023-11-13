import CreateData.client_class as Client

# Initializes the list of tuples (surname, gender). Will be reused later in the "create_data()" func. 
# Returns a list of (name, gender) tuples. 

def data_() :

    variable_list = []

    open_file =  open("CreateData/surnames.txt", "r")
    for line in open_file : 
        file_line = line.strip()
        surname, gender = file_line.split(",")
        variable_list.append((surname, gender))
    open_file.close()

    return variable_list

# Create random data. Should be stocket to a variable. 
# Returns JSON formated DATAS. 

def create_data() : 

    import random 
    from CreateData.client_class import Client
    # Import Client Class
    import CreateData.createdatafuncs as cd
    # Can't explain why it's here for now but does not work otherwise 
    

    data = []
    # Iniialize empty list data

    clients_list = []

    # Iniialize empty list clients_list

    ### For now the data created will be used in order to train to Data Analysis.
    ### For the moment, it's more about learning data analytics modules than working with big data, so I begin with ten small. 

    for i in range(10) :
        client = cd.data_()[random.randint(0, len(cd.data_()) - 1)]
        # Choose one (surname, gender) pair tuple
        new_client = Client(
            client[0], 
            random.randint(18, 99), 
            client[1], 
            random.randint(0, 4000000), 
            random.randint(0, 5), 
            random.choice([True, False])
            )
        # Instantiate new Client objet with its parameters (indexes of client tuples)
        clients_list.append(new_client)
        # Adding the new Client object to the client list. 
        ## Doing it ten times


        # Formating client list to json datas
    for client in clients_list : 
        client_data = {
            "name" : client.name, 
            "age" : client.age,
            "gender" : client.gender,
            "annual_income" : client.annual_income, 
            "number_of_children" : client.number_of_children,
            "married" : client.married
        }
        data.append(client_data)


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