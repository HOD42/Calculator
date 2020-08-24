first_number = input('What is your 1st number?')
second_number = input('What is your 2nd number?')
operation =  input('What is the operation?')

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

print ('Testing validate_operation (operation)')
print (validate_operation (operation) )