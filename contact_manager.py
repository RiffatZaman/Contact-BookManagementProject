from storage import save_contacts, load_contacts
def add_contact(name, email, phoeNo, address,):
    contacts=load_contacts()
    contact={
        'name':name,
        'email':email,
        'phoeNo':phoeNo,
        'address':address

    }
    contacts.append(contact)
    save_contacts(contacts)
def view_contacts():
    contacts=load_contacts()
    print("\n Task List :\n")
    for i, contact in enumerate (contacts, start=1):
        print(f"{i}.Name:{contact['name']},Email:{contact['email']},PhoneNo:{contact['phoeNo']},Address:{contact['address']}")
def remove_contact(index):
    contacts=load_contacts()
    if 0<index<len(contacts):
        del contacts[index-1]
        save_contacts(contacts)
    else:
        print("Invalid Index")
def search_contact(query):
    contacts=load_contacts()
    results=[]
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query.lower() in contact['address'].lower():
            results.append(contact)
            print("\n Searach Result :")
    for i, contact in enumerate(results, start=1):
        print(f"{i}.Name:{contact['name']},Email:{contact['email']},PhoneNo:{contact['phoeNo']},Address:{contact['address']}")


    else:
        print("Invalid Index")




