name = input("what is your name? ")
while True:
    age = input("what is your age? ")
    try:
        age_tenyears = int(age) + 10
        break
    except ValueError:
        print(f"enter valid number for age")
print(f"Hello {name} you will be {age_tenyears} years old after 10 years")