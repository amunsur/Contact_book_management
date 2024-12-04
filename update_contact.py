from save_all_contact import save_all_contact

def update_contact_by_number(all_contact):
    number_to_update = input("\nEnter the number of the contact you want to update: ")

    for contact in all_contact:
        if int(contact['number']) == number_to_update:
            print(f"\n number found: {contact}")

            print("\nHere are the fields that you can update")
            print("1. name")
            print("2. email")
            print("3. number")
            print("4. adress")
        

            field_choice = input("\nWhich field would you like to update? Select: ").strip()

            field_to_update = {
                "1": "name",
                "2": "emailr",
                "3": "number",
                "4": "adress",
            }

            if field_choice in field_to_update:
                field = field_to_update[field_choice]

                new_value = input(f"Enter the new value for {field}: ").strip()

                if field == "name":
                    new_value = str(new_value)
                elif field == "email":
                    new_value = str(new_value)
                elif field == "number":
                    new_value = int(new_value)
                elif field == "address":
                    new_value = str(new_value)

                contact[field] = new_value
                print(f"\nUpdated {field} of contact with number {number_to_update} to {new_value}.")

                save_all_contact(all_contact)
                return all_contact

            else:
                print("\nInvalid choice. Please choose a valid number between 1 to 4.")
                return all_contact

    print(f"\ncontact with number {number_to_update} not found.")
