from tinydb import TinyDB, Query

db = TinyDB('students.json')
User = Query()
def addRecord():
    #Adding record
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    db.insert({'Name': name, 'age': age})

def searchRecord():
    #Searching for a record.
    studentSearch = input("Enter name: ")
    student = db.search(User.Name == studentSearch)
    print(student)

def showAll():
    #Show all records
    for item in db:
        print(item)

while True:
    menu = input(""" Choose option
                1. Add new record
                2. Search for record
                3. Show all records 
                >>> """)
    if menu == "1":
        addRecord()
    elif menu == "2":
        searchRecord()
    elif menu == "3":
        showAll()
    elif menu == "END":
        print("Thank you for using the system.")
        break
    else: 
        print("Option not found")


