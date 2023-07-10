"""
User Input
"""

first_name = input("Enter your first name: ")
days = int(input("how many days until your birthday: "))
weeks = days / 7
output = f"Hello there, {first_name}.  Your birthday is in {round(weeks, 2)} weeks."
print(output)
