from contact_manager import add_contact, view_contacts, remove_contact, search_contact

while True:
    print("\n\nWelcome to Contact Book Manager")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. remove Contact")
    print("4. Search Contact")
    print("5.Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Contact name:")
        email = input("Email :")
        phoeNo = int(input("Phonenumber: "))
        address = input("Address: ")
        add_contact(name, email, phoeNo, address)
        print("Contact Add Successfully")

    elif choice == "2":
        view_contacts()
    elif choice =="3":
        index =int(input("enter the index of the contact you want to remove"))
        remove_contact(index)
        print("Contact Remove Successfully")
    elif choice=="4":
        query=input("Enter the search query: ")
        search_contact(query)

    else:
        print("Thank You For Uning Contact Book Manager")
        break







