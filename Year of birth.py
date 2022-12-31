from datetime import datetime

def main():
    # Get the current year
    current_year = datetime.now().year

    # Get the age from the user
    age = int(input("Enter your age: "))

    # Calculate the year of birth
    year_of_birth = current_year - age

    # Print a message indicating the year of birth
    print(f"You were born in {year_of_birth}.")

if __name__ == "__main__":
    main()
