first_number = int(input('What is your 1st integer number?')) # Add validation later
operation =  input('What is the operation?')
second_number = int(input('What is your 2nd integer number?')) # Add validation later
# NOTE: Re-ordered parameters (to be more natural)

def validate_operation(operation):
    if operation == ('x'):
        return True
    elif operation == ('+'):
        return True
    elif operation == ('-'):
        return True
    elif operation == ('/'):
        return True
    else:
        return False

# This function will add the 2 inputs together
def calculation_add(first_number, second_number):
    return first_number + second_number

# This function will subtract the 2 inputs from each other
def calculation_subtract(first_number, second_number):
    return first_number - second_number

# This function will multiply the 2 inputs
def calculation_multiply(first_number, second_number):
    return first_number * second_number

# This function will divide the 2 inputs
def calculation_divide(first_number, second_number):
    return first_number / second_number

# This is for stretch goal (make more elegant by including the operator)
#def calculation(first_number, operation, second_number):
#    return first_number operation second_number

if operation == '+':
    print (calculation_add (first_number, second_number))
elif operation == '-':
    print (calculation_subtract (first_number, second_number))
elif operation == 'x':
    print (calculation_multiply (first_number, second_number))
elif operation == '/':
    print (calculation_divide (first_number, second_number))
else:
    print ('ERROR : This should never happen!')