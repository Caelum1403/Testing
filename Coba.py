def collect_user_info():
    # Asking for user's name
    name = input("What is your name? ")
    
    # Asking for user's age
    age = input("How old are you? ")
    
    # Asking for user's school
    school = input("Which school do you attend? ")
    
    # Displaying the collected information
    print("\nThank you for providing your information!")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"School: {school}")

# Calling the function to execute
collect_user_info()