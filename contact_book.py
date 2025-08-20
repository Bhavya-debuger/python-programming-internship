def display_menu():
    print("\nContact Book")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search by Name")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(contacts):
    search_name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact(contacts):
    del_name = input("Enter name to delete: ")
    for contact in contacts:
        if contact['name'].lower() == del_name.lower():
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")

def main():
    contacts = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()