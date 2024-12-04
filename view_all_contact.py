def view_all_contact(all_contact):
    if all_contact != []:
        for contact in all_contact:
            print(f"name: {contact['name']} | email: {contact['email']} | number: {contact['number']} | address: {contact['adress']}")
    else:
        print("No contact found in contact book")