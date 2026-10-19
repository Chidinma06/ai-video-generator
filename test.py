python -m venv venv
def business_name():
    getfromuser = input("what is your business name?")
    return getfromuser
resultfromuser = business_name()
print(f"you are welcome to {resultfromuser}")