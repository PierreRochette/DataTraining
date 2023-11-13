### THIS PART OF THE PROGRAMMM IS DESTINATED TO BE RUNNED ONLY ONCE
### I KNOW I COULD HAVE DONE THIS IN A MORE EFFICIENT WAY, BUT I 
### WANTED TO PRACTICE PPO & JSON WRITING WITH PYTHON. 

import CreateData.createdatafuncs as cd

# Calling the create_data() function and saving the array it returns on data. 

data = cd.create_data()

# Writing the data collected on a JSON file. 

cd.json_dump("clients.json", data)