name = input("What's your name? ")
birth_year = int(input("What's your birth year? "))
favorite_number = int(input("What's your favorite number? "))

age = 2026 - birth_year
doubled = favorite_number * 2

print(f"Hello, {name}! You are approximately {age} years old.")
print(f"Your favorite number doubled is {doubled}.")

print(type(name))
print(type(age))
print(type(favorite_number))