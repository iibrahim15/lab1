def calculate_age():
    birth_year = input("Enter your birth year: ")
    birth_year = int(birth_year)
    current_year = 2024 
    age = current_year - birth_year
    print("You are " + str(age) + " years old.")
