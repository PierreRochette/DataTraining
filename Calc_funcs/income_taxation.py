def children_shares(element) : 

    if element == 0 : 
        number = 0
    elif 1 <= element <= 2 : 
        number = 0.5 * element
    else : 
        number = element - 1 
        
    return number

def mariage_shares(element) : 
    if element == False : 
        number = 1
    else : 
        number = 2

    return number

def total_shares(a, b) : 
    
    return a + b

def income_taxation(quotient, income) : 

    taxable_income = income / quotient

    if taxable_income <= 10777 : 
        result = 0
    elif 10778 <= taxable_income <= 27478 : 
        result = (27478 - taxable_income) * 0.11
    elif 27479 <= taxable_income <= 78750 : 
        result = (78750 - taxable_income) * 0.3 + 1837
    elif 78751 <= taxable_income <= 168994 : 
        result = (168994 - taxable_income) * 0.41 + 17164.3
    elif taxable_income > 168994 : 
        result = (taxable_income - 168995) * 0.45 + 54237.7

    result *= quotient

    return int(result)

