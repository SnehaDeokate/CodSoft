contacts = {}

def add_contact(name, phone_number, email, address):
    contacts[name] = {
        'Phone Number': phone_number,
        'Email': email,
        'Address': address
    }
    print(f"Contact {name} added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()

def search_contact(search_term):
    results = [name for name in contacts if search_term.lower() in name.lower() or search_term in contacts[name]['Phone Number']]
    if not results:
        print("No matching contacts found.")
        return
    for name in results:
        print(f"Name: {name}")
        for key, value in contacts[name].items():
            print(f"  {key}: {value}")
        print()

def update_contact(name, phone_number=None, email=None, address=None):
    if name not in contacts:
        print("Contact not found.")
        return
    if phone_number:
        contacts[name]['Phone Number'] = phone_number
    if email:
        contacts[name]['Email'] = email
    if address:
        contacts[name]['Address'] = address
    print(f"Contact {name} updated successfully.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term)
        elif choice == '4':
            name = input("Enter contact name to update: ")
            phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            update_contact(name, phone_number if phone_number else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
