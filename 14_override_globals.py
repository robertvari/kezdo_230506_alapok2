NAME = "Csaba"

def print_name():
    print(NAME)

def change_name(new_name):
    global NAME
    NAME = new_name

change_name("Kriszta")
print_name()