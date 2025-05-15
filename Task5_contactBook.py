contacts = {}

def addContacts():
    name = input("Enter your name :- ").strip()
    phone = input("Enter your phone number :- ").strip()
    email = input("Enter your email address :- ").strip()
    address = input("Enter your address :- ").strip()

    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully")

def viewContacts():
    if not contacts:
        print("No Contacts found.")
    else:
        print("---------- Contacf List ----------")
        for name,info in contacts.items():
            print(f"\nName : {name}")
            print(f"Phone : {info['phone']}")
            print(f"Email : {info['email']}")
            print(f"Address : {info['address']}")
        print()

def searchContact():
    name = input("Enter the Name to search :- ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\n Name : {name}")
        print(f"Phone : {info['phone']}")
        print(f"Email : {info['email']}")
        print(f"Address : {info['address']}")
    else:
        print("No Contact found.")

def updateContact():
    name = input("Enter the Name to update the details :- ").strip()
    if name in contacts:
        print("Leave blank to keep the current value.")
        phone = input(f"New Phone No. (current : {contacts[name]["phone"]}): ").strip()
        email = input(f"New Email Address. (current : {contacts[name]["email"]}): ").strip()
        address = input(f"New Address. (current : {contacts[name]["address"]}): ").strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address

        print("Contact updated successfully")
    else:
        print("No Contact found.")

def deleteContact():
    name = input("Enter the Name to delete :- ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("No Contact found.")

def contactBook():
    while True:
        print("------------------- Contact Book ------------------")
        print("1. Add Contact")
        print("2. View all Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print('-'*48)

        choice = input("Enter your choice (1-6) :- ")
        if choice == '1':
            addContacts()
        elif choice == '2':
            viewContacts()
        elif choice == '3':
            searchContact()
        elif choice == '4':
            updateContact()
        elif choice == '5':
            deleteContact()
        elif choice == '6':
            print("Thanks for using Contact Book")
            break
        else:
            print("Invalid Choice.")
            print("Please try again.")

contactBook()
