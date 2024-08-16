import re

def validate_password(password):
    if len(password) < 12:
        return "Password must be at least 12 characters long."
    
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."
    
    if not re.search(r'[^a-zA-Z0-9]', password):
        return "Password must contain at least one special character."
    
    return "Valid Password."

password = input("Enter your password: ")
validation_message = validate_password(password)

print(validation_message)
