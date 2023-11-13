import CreateData.client_class as Client

# Initializes the list of tuples (surname, gender). Will be reused later in the "create_data()" func. 

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

def create_data() : 

    import random 
    from CreateData.client_class import Client
    import CreateData.createdatafuncs as cd

    data = []

    clients_list = []

    ### For now the data created will be used in order to train to Data Analysis.
    ### For the moment, it's more about learning data analytics modules than working with big data, so I begin with ten small. 

    for i in range(10) :
        client = cd.data_()[random.randint(0, len(cd.data_()) - 1)]
        new_client = Client(client[0], random.randint(18, 99), client[1])
        clients_list.append(new_client)

    for client in clients_list : 
        client_data = {
            "name" : client.name, 
            "age" : client.age,
            "gender" : client.gender
        }
        data.append(client_data)


    return data


# Write data (or anything else) on a JSON File. Be sure to specify the path correctly. 

def json_dump(filename, variable_name) :

    import json

    with open(filename, "w") as json_file :
        json.dump(variable_name, json_file, indent=4)

    return None

