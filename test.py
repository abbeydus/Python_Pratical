import re

def is_valid_password(password):
    # Check length
    if len(password) < 6 or len(password) > 16:
        return False
    
    # Check for at least 1 lowercase letter
    if not re.search("[a-z]", password):
        return False
    
    # Check for at least 1 uppercase letter
    if not re.search("[A-Z]", password):
        return False
    
    # Check for at least 1 digit
    if not re.search("[0-9]", password):
        return False
    
    # Check for at least 1 special character
    if not re.search("[$#@]", password):
        return False
    
    return True

# Test the function
password = input("Enter password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")