def calculate_age():
    try:
        birth_year = input("Enter your birth year: ")
        birth_year = int(birth_year)
        current_year = 2024  # replace with the current year
        age = current_year - birth_year
        print("You are " + str(age) + " years old.")
    except ValueError:
        print("Please enter an int")
calculate_age()

def helloWorld():
	print("Hello World")


helloWorld()

