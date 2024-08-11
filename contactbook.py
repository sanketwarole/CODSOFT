print("=>=>=>=>=>=> CONTACT BOOK <=<=<=<=<=<=")
contacts = {}

def addcontact():
    name = input("Enter the Name: ")
    phone = int(input("Enter the Phone number: "))
    email = input("Enter e-mail: ")
    address = input("Enter the address: ")

    if name in contacts:
        print("The contact already exists.")
    else:
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print("Contact added successfully.")

def delcontact():
    name = input("Enter the name to be deleted: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")

def updatecontact():
    name = input("Enter the name to update: ")
    if name in contacts:
        phone = int(input("Enter the new Phone number: "))
        email = input("Enter the new e-mail: ")
        address = input("Enter the new address: ")
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print("Contact updated successfully.")
    else:
        print("This contact does not exist.")

def searchcontact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print("Contact Found")
        print("Name:", name)
        print("Phone:", contacts[name]['phone'])
        print("Email:", contacts[name]['email'])
        print("Address:", contacts[name]['address'])
    else:
        print("Contact not found.")

def display():
    if not contacts:
        print("Contact book is empty!!")
    else:
        for name, details in contacts.items():
            print("Name:", name)
            print("Phone:", details['phone'])
            print("Email:", details['email'])
            print("Address:", details['address'])

while True:
    print("1. Add Contact\n2. Display Contact\n3. Update Contact\n4. Search Contact\n5. Delete Contact\n6. Exit\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addcontact()
    elif choice == 2:
        display()
    elif choice == 3:
        updatecontact()
    elif choice == 4:
        searchcontact()
    elif choice == 5:
        delcontact()
    elif choice == 6:
        print("Exiting!!!")
        break
    else:
        print("Invalid choice")
