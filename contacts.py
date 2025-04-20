contacts = []

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts.append({"name": name, "number": number})
        print("Contact added successfully!")

    elif choice == "2":
        search = input("Enter name to search: ")
        found = False
        for c in contacts:
            if c["name"] == search:
                print(f"Found: {c['name']} - {c['number']}")
                found = True
                break
        if not found:
            print("Contact not found")

    elif choice == "3":
        if not contacts:
            print("No contacts available")
        else:
            print("\nAll contacts:")
            for c in contacts:
                print(f"{c['name']} - {c['number']}")

    elif choice == "4":
        delet = input("Enter name to delete: ")
        found = False
        for c in contacts:
            if c["name"] == delet:
                contacts.remove(c)
                print("Contact deleted successfully")
                found = True
                break
        if not found:
            print("Contact not found")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1-5")
