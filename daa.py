class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return f"Contact(name={self.name}, phone_number={self.phone_number}, email={self.email})"
def quick_sort(contacts, key):
    if len(contacts) <= 1:
        return contacts

    pivot = contacts[0]
    less = [contact for contact in contacts[1:] if getattr(contact, key) <= getattr(pivot, key)]
    greater = [contact for contact in contacts[1:] if getattr(contact, key) > getattr(pivot, key)]

    return quick_sort(less, key) + [pivot] + quick_sort(greater, key)
class ContactOrganizer:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def edit_contact(self, name, new_name=None, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone_number = new_phone
                if new_email:
                    contact.email = new_email
                return True
        return False

    def search_contact(self, name):
        return [contact for contact in self.contacts if contact.name.lower() == name.lower()]

    def sort_contacts(self, key='name'):
        self.contacts = quick_sort(self.contacts, key)

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)
def main():
    organizer = ContactOrganizer()

    while True:
        print("\nContact Organizer")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Edit Contact")
        print("4. Search Contact")
        print("5. Sort Contacts")
        print("6. Display Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            organizer.add_contact(name, phone, email)
            print("Contact added successfully!")

        elif choice == '2':
            name = input("Enter name of the contact to delete: ")
            organizer.delete_contact(name)
            print("Contact deleted successfully!")

        elif choice == '3':
            name = input("Enter name of the contact to edit: ")
            new_name = input("Enter new name (leave blank to keep unchanged): ")
            new_phone = input("Enter new phone number (leave blank to keep unchanged): ")
            new_email = input("Enter new email (leave blank to keep unchanged): ")
            if organizer.edit_contact(name, new_name or None, new_phone or None, new_email or None):
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == '4':
            name = input("Enter name to search: ")
            results = organizer.search_contact(name)
            if results:
                print("Search Results:")
                for contact in results:
                    print(contact)
            else:
                print("No contacts found.")

        elif choice == '5':
            sort_key = input("Enter sorting criterion ('name', 'phone_number', or 'email'): ").strip()
            if sort_key in ['name', 'phone_number', 'email']:
                organizer.sort_contacts(sort_key)
                print(f"Contacts sorted by {sort_key}.")
            else:
                print("Invalid sorting criterion.")

        elif choice == '6':
            print("Contact List:")
            organizer.display_contacts()

        elif choice == '7':
            print("Exiting Contact Organizer. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
