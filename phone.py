class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("\nContact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
            return
        print("\nContact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(i, ".", contact.name, "-", contact.phone)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("\nNo matching contacts found.")
            return
        print("\nSearch Results:")
        for i, contact in enumerate(results, start=1):
            print(i, ".", contact.name, "-", contact.phone)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nUpdating contact details:")
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("\nContact updated successfully.")
                return
        print("\nContact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("\nContact deleted successfully.")
                return
        print("\nContact not found.")

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            name = input("\nEnter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("\nEnter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            name = input("\nEnter the name of the contact to update: ")
            manager.update_contact(name)
        elif choice == '5':
            name = input("\nEnter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            print("\nThank you for using the Contact Manager!")
            break
        else:
            print("\nInvalid choice. Please try again.")

main()
