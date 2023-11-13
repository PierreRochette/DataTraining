def children_quotient(element) : 

    if element == 0 : 
        number = 0
    elif 1 <= element <= 2 : 
        number = 0.5 * element
    else : 
        number = element - 1 
        
    return number