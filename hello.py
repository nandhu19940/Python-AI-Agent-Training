name = input("What is your name? ")
age = input("what is your age? ")
try:
    agetenyears = int(age) + 10
    print (f"Hello {name} you will be {agetenyears} years old after 10 years")
except ValueError as e:
    print(f"enter valid number for age")
