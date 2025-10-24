import json
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the JSON file."""
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {} # Return an emoty dictionary if file is missing or empty
    
def save_contacts(contacts):
    """Saves the contacts dictionary to the JSON file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def view_contacts(contacts):
    """Displays all contacts."""
    print("\n--- Your Contacts ---")
    if not contacts:
        print("Your contact book is empty.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    print("---------------------\n")

def add_contacts(contacts):
    """Adds a new contacts."""
    name = input("Enter the contact's name: ")
    if name in contacts:
        print("A contact with this name already exists.")
        return 
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts):
    """Searches for a contact by name."""
    search_name = input("Enter the name you are searhing for: ")

    if search_name in contacts:
        details = contacts[search_name]
        print("\n--- Contact Found ---")
        print(f"Name: {search_name}, Phone: {details['phone']}, Email: {details['email']}")
        print("---------------------\n")
    else:
        print(f"No contact found with this name '{search_name}'.\n")

def main():
    """Main function to run the contact book app."""
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Add a new Contact")
        print("3. Search for a contact")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            print("Exiting the application...")
            break
        else:
            print("Invalid Choice: Please try again.")

if __name__ == "__main__":
    main()