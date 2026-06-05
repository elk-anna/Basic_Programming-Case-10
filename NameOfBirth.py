def create_username(full_name, birth_year):
    first_name = full_name.split()[0].lower()
    last_two_digits = str(birth_year)[-2:]

    username = first_name + last_two_digits
    return username

print(create_username("Leanne Jeira", 2006))
