def print_user_data(name, password, email=None, address=None):
    print(f"-"*20)
    print(f"Name: {name}")
    print(f"Password: {password}")
    if email:
        print(f"Email: {email}")

    if address:
        print(f"Address: {address}")

    print(f"-"*20)

print_user_data("Csaba", "testpas123", "csaba@gmail.com")