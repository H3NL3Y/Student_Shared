def create_username(fname, sname, year):
    fnameLetter = fname[0]
    username = fnameLetter+sname+year.upper()
    return username


fname = input("Enter first name: ")
sname = input("Enter second name: ")
year = input("Enter year of birth: ")
username = create_username(fname, sname, year)

print(f"Your new username is {username}")
