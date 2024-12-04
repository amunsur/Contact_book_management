from save_all_contact import save_all_contact 

def add_contact(all_contact):
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    number = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()


    if not number.isdigit():
        print("Error: Phone number must contain only digits.")
        return all_contact


    for contact in all_contact:
        if contact['number'] == int(number):
            print("This phone number already exists in your contact list.")
            return all_contact


    contact = {
        "name": name,
        "email": email,
        "number": int(number),  
        "address": address  
    }

    all_contact.append(contact)
    save_all_contact(all_contact)  

    print("Contact added successfully!")
    return all_contact
