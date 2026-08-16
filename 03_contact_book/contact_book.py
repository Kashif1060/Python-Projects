contacts = {}

print("===== CONTACT BOOK =====")


while True:
  print("\n1. Add Contact")
  print("2. Search Contact")
  print("3. Update Contact")
  print("4. Exit")

  choice = input("Enter your choice: ").strip()

  if choice == "1":
    name = input("Enter contact name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if name == "" or phone == "" or email == "":
      print("All information is required.")

    else:
      contacts[name] = {
          "phone": phone,
          "email": email
      }
      print("Contact added successfully.")

  elif choice == "2":
    search_name = input("Enter contact name to search: ").strip().title()

    if search_name in contacts:
      print("\nContact found!")
      print("Name:", search_name)
      print("Phone:", contacts[search_name]["phone"])
      print("Email:", contacts[search_name]["email"])
    else:
      print("Contact not found.")

  elif choice == "3":
        update_name = input(
            "Enter contact name to update: "
        ).strip().title()

        if update_name in contacts:
            phone = input("Enter new phone number: ").strip()
            email = input("Enter new email address: ").strip()

            if phone == "" or email == "":
                print("All information is required.")

            else:
                contacts[update_name]["phone"] = phone
                contacts[update_name]["email"] = email

                print("Contact updated successfully.")

        else:
            print("Contact not found.")

  elif choice == "4":
    print("Contact Book closed.")
    break

  else:
    print("Invalid choice. Enter 1, 2, 3, or 4.")
